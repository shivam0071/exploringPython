import requests
import logging
import sys
from threading import Thread
import time
import pandas as pd
import re

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
CACHE_STATE_DATA = []
CACHE_COUNTRY_DATA = []

def clear_cache_thread():
    global CACHE_STATE_DATA, CACHE_COUNTRY_DATA
    reset_cache_timer = 0
    logging.info("CACHING DATA INITIALLY") 
    CACHE_STATE_DATA = get_state_wise_data_wiki()
    CACHE_COUNTRY_DATA = get_country_wise_data_wiki()
    while True:
        if reset_cache_timer < 1800: # refresh every one hour, todo: add hardcoded data to config files
            reset_cache_timer += 1
            time.sleep(1)
        elif reset_cache_timer == 1800:
            logging.info("REFRESHING CACHE")
            reset_cache_timer = 0
            CACHE_STATE_DATA = []
            CACHE_COUNTRY_DATA = []
            CACHE_STATE_DATA = get_state_wise_data_wiki()
            CACHE_COUNTRY_DATA = get_country_wise_data_wiki()

def get_state_wise_data_wiki():
    global CACHE_STATE_DATA
    try:
        if CACHE_STATE_DATA:
            logging.info("FETCHING FROM CACHED DATA")
            return CACHE_STATE_DATA
        table = pd.read_html("https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India")[7][0:37]
        # table = table[[1,2,3,4,5]]
        table.columns = ["S.No","location", "cases", "deaths", "recovered", "active"]
        state_data = table.to_dict('records')
        # for demo only
        # state_data = [{"active":"0","cases":"33","deaths":"0","location":"Andaman and Nicobar Islands","recovered":"33"},{"active":"1268","cases":"3679","deaths":"62","location":"Andhra Pradesh","recovered":"2349"},{"active":"3","cases":"4","deaths":"0","location":"Arunachal Pradesh","recovered":"1"},{"active":"1083","cases":"1272","deaths":"4","location":"Assam","recovered":"185"},{"active":"2084","cases":"3815","deaths":"21","location":"Bihar","recovered":"1710"},{"active":"90","cases":"293","deaths":"4","location":"Chandigarh","recovered":"199"},{"active":"382","cases":"498","deaths":"1","location":"Chhattisgarh","recovered":"115"},{"active":"2","cases":"2","deaths":"0","location":"Dadra and Nagar Haveli and Daman and Diu","recovered":"0"},{"active":"10893","cases":"19844","deaths":"473","location":"Delhi","recovered":"8478"},{"active":"28","cases":"70","deaths":"0","location":"Goa","recovered":"42"},{"active":"5822","cases":"16779","deaths":"1038","location":"Gujarat","recovered":"9919"},{"active":"1023","cases":"2091","deaths":"20","location":"Haryana","recovered":"1048"},{"active":"206","cases":"331","deaths":"5","location":"Himachal Pradesh","recovered":"120"},{"active":"1491","cases":"2446","deaths":"28","location":"Jammu and Kashmir","recovered":"927"},{"active":"349","cases":"610","deaths":"5","location":"Jharkhand","recovered":"256"},{"active":"1952","cases":"3221","deaths":"51","location":"Karnataka","recovered":"1218"},{"active":"670","cases":"1269","deaths":"9","location":"Kerala","recovered":"590"},{"active":"31","cases":"74","deaths":"0","location":"Ladakh","recovered":"43"},{"active":"0","cases":"0","deaths":"0","location":"Lakshadweep","recovered":"0"},{"active":"2897","cases":"8089","deaths":"350","location":"Madhya Pradesh","recovered":"4842"},{"active":"36040","cases":"67655","deaths":"2286","location":"Maharashtra","recovered":"29329"},{"active":"60","cases":"71","deaths":"0","location":"Manipur","recovered":"11"},{"active":"14","cases":"27","deaths":"1","location":"Meghalaya","recovered":"12"},{"active":"0","cases":"1","deaths":"0","location":"Mizoram","recovered":"1"},{"active":"43","cases":"43","deaths":"0","location":"Nagaland","recovered":"0"},{"active":"815","cases":"1948","deaths":"7","location":"Odisha","recovered":"1126"},{"active":"45","cases":"70","deaths":"0","location":"Puducherry","recovered":"25"},{"active":"231","cases":"2263","deaths":"45","location":"Punjab","recovered":"1987"},{"active":"2710","cases":"8831","deaths":"194","location":"Rajasthan","recovered":"5927"},{"active":"1","cases":"1","deaths":"0","location":"Sikkim","recovered":"0"},{"active":"9403","cases":"22333","deaths":"173","location":"Tamil Nadu","recovered":"12757"},{"active":"1188","cases":"2698","deaths":"82","location":"Telangana","recovered":"1428"},{"active":"140","cases":"313","deaths":"0","location":"Tripura","recovered":"173"},{"active":"800","cases":"907","deaths":"5","location":"Uttarakhand","recovered":"102"},{"active":"2901","cases":"7823","deaths":"213","location":"Uttar Pradesh","recovered":"4709"},{"active":"3027","cases":"5501","deaths":"317","location":"West Bengal","recovered":"2157"},{"active":"93322","cases":"190535","deaths":"5394","location":"Total","recovered":"91819"}]
        logging.info(f" India Example - {state_data[0]}")
        state_data = clean_json_data(state_data)
        CACHE_STATE_DATA = state_data
        return state_data
        # {'location': 'Andaman and Nicobar Islands', 'cases': '33', 'deaths': '0', 'recovered': '33', 'active': '0'}
    except Exception as ex:
        logging.error("Exception in State Wise Wiki API--->",ex)
        return {"ERROR": "Problem with API"}

def clean_json_data(data):
    """Removes Special Characters and Ablphabets from numbers"""
    for entry in data:
        entry['cases'] = re.sub('[^0-9]+', '',entry['cases'])
        entry['deaths'] = re.sub('[^0-9]+', '',entry['deaths'])
        entry['recovered'] = re.sub('[^0-9]+', '',entry['recovered'])
        if entry.get("active", None):  # Active not in Global
            entry["active"] = re.sub('[^0-9]+', '',entry.get("active", ""))
    return data

# to do, place this at apt place
# t1 = Thread(target = clear_cache_thread)
# logging.info("STARTING THREAD") 
# t1.start()
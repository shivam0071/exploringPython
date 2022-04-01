import concurrent.futures
import requests
import threading
import time


thread_local = threading.local()
# This creates an object that looks like a global but is specific to each individual thread

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
        # not thread safe
    return thread_local.session


def download_site(url):
    session = get_session()
    # creating session for each thread

    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
    # Downloaded 160 in 7.463363170623779 seconds with 5 threads
    # Downloaded 160 in 8.382404804229736 seconds  with 8 threads
    # Downloaded 160 in 5.410483360290527 seconds with 10 threads
    # Downloaded 160 in 23.45268154144287 seconds using request.get without session
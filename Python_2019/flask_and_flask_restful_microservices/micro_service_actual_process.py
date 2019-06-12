import os
from os import sep
from configparser import ConfigParser

BANDS = []
POKEMON = []


config_file = "config.ini"
file_path = ''

if r"/" in config_file:
  file_path = config_file
elif config_file in os.listdir():
  file_path = os.getcwd() + sep + config_file
else:
  file_path = os.getcwd() + sep + "Python_2019" + sep + "flask_and_flask_restful_microservices" + sep + config_file


config_parser = ConfigParser()

def best_bands():
  return BANDS

def best_pokemon():
  return POKEMON

def get_config_data():
  global POKEMON, BANDS
  try:
    config_parser.read(file_path)
    BANDS = config_parser.get("bands", "band_names").split(",")
    POKEMON = config_parser.get("pokemon", "pokemon_name").split(",")
    print(POKEMON, BANDS, "HERERERE")
  except Exception as ex:
    print(ex)
    return ex

def main():
  get_config_data()

if __name__ == "__main__":
  main()
from core.utils import *
import json

#=====================|=========================================================================================
# MAIN JSON OPERATORS | Used to operate over .json files
#=====================|=========================================================================================
# Reads file and returns either value, dict or list
def json_read(path, element=None, isdict=False):
  try:
    fpath = f"{gpath}/{path}"
    with open(fpath, encoding="utf-8") as json_file:
      data = json.load(json_file)
    if element is None and isdict is True: return [*data] #returns dict
    if element is None and isdict is False: return data #returns list
    return data[element] #returns element

  except json.decoder.JSONDecodeError: log.warning (f"JSON File: {path} does not have any arguments. Skipping.")

#============|==================================================================================================
# SUBSYSTEMS | Smaller functions used for special purposes
#============|==================================================================================================
# Reads second key of .json file (used to call values of objects from ID)
def json_subread(path, element, subelement):
  subdata = json_read(path, element)[0]
  return subdata[subelement]
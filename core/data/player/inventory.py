from core.file_system.parsers import loadYAML, writeYAML
from os.path import exists
import logging as log
import random

toInt = [   # keys always converted to int
    "quality"
]
toFloat = [ # keys always converted to float

]

def parseDataScript(iid: str, key: str, value_parsed: int | float | str) -> int | float | str:
    """Reads the item script used in `data` dictionary and returns equivalent value
    - IID          - easy, ID of the item
    - key          - data key to be analysed (for example 'quality')
    - value_parsed - value of said key       (for example '3..5')
    """
    if   isinstance(value_parsed, int):   return value_parsed
    elif isinstance(value_parsed, float): return value_parsed
    # if 'str', continue

    if key not in toInt + toFloat and key[-1] not in ["^", "*"]: return value_parsed # check for special handling

    vals    = [value_parsed] # without range modifier, it should contain only one value
    # vars to be used for variable replacement
    iid_v   = iid.split(":")
    print(f"IID_V:{iid_v}, KEY:{key}, VALUE_PARSED:{value_parsed}")
    it_dat  = loadYAML(f"stats/{iid_v[0]}/items/{iid_v[1]}.yaml")
    it_keys = it_dat.keys()

    if ".." in value_parsed:
        vals = value_parsed.split("..") # overwrites with two items if it's range
        print(f"VALS: {vals}")

    # NOTE: below converters only convert `str` | consider converting float > int, int > float if needed
    # PyCharm errors about vals[0] or vals[ix] being str or other type are untrue, ignore
    # -- variable replacement
    for ix, val in enumerate(vals):
        print(f"{ix}, {val} enumerated! IT_KEYS: {it_keys}")
        if val in it_keys:
            vals[ix] = it_dat[val]
    print(f"VALS after IT_DAT: {vals}")
    # -- range
    if len(vals) == 2:
        if key in toInt or key[-1] == "^":              # convert to int
            vals = [random.randint(vals[0], vals[1])]
        elif key in toFloat or key[-1] == "*":          # convert to float
            vals = [random.uniform(vals[0], vals[1])]

    return vals[0]

def addItem(name: str, iid: str, count_data: int | dict | None):
    # recognise whether item is stackable or not, compare to count_data type
    iid_v = iid.split(":")

    log.debug(f"Adding item: {iid} to inventory: {name}, with data: {count_data}.")

    # checking for category of an item
    it_dat = loadYAML(f"stats/{iid_v[0]}/items/{iid_v[1]}.yaml")
    it_cat = 1 if "data" in it_dat.keys() else 0 # stackable = 0, unique = 1

    # proceed to check if item exists (only if stackable), perform action
    inv = loadYAML(f"saves/{name}/buffer/inventory.yaml")
    match it_cat: # modify 'inv'
        case 0:
            if iid in inv["stackables"].keys():
                inv["stackables"][iid] = inv["stackables"][iid] + count_data
            else:
                inv["stackables"][iid] = count_data
        case 1:
            dat_out = it_dat["data"]
            if count_data is not None:
                for dk in count_data.keys():
                    dat_out[dk] = count_data[dk]
            for ix, vl in dat_out.items():
                dat_out[ix] = parseDataScript(iid, ix, vl)
            inv["uniques"].append({iid: dat_out})
        case _: raise KeyError(f"Tried to find category {it_cat} for item {iid} while adding to inventory of {name}, but failed. Additional data: {count_data}.")
    writeYAML(f"saves/{name}/buffer/inventory.yaml", inv) # finish by saving 'inv'

def removeItem(): pass
def changeItem(): pass #!!!
def equipItem(): pass
def deequipItem(): pass
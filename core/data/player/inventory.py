from core.file_system.parsers import loadYAML, writeYAML
from core.data.world.item import getItem
from os.path import exists
import logging as log

def isUnique(iid: str) -> bool:
    """Returns whether item is unique (non-stackable) or stackable; True is unique"""
    iid_v = iid.split(":")
    if "data" in loadYAML(f"stats/{iid_v[0]}/items/{iid_v[1]}.yaml").keys():
        return True
    return False

def addItem(name: str, iid: str, count_data: int | dict):
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
            inv["uniques"].append({iid: it_dat["data"]})
        case _: raise KeyError(f"Tried to find category {it_cat} for item {iid} while adding to inventory of {name}, but failed. Additional data: {count_data}.")
    writeYAML(f"saves/{name}/buffer/inventory.yaml", inv) # finish by saving 'inv'

def removeItem(): pass
def changeItem(): pass #!!!
def equipItem(): pass
def deequipItem(): pass
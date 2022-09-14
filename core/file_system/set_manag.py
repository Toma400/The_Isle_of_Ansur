from core.utils import *

def set_change(key, value=None):
    setval = json_read("settings.json", key)
    if type(setval) is bool:
        json_change("settings.json", key, not setval)
        log.debug(f"Switching settings for: {key} to {not setval}.")
    elif type(setval) is int and type(value) is int:
        json_change_ins("settings.json", key, value)
        log.debug(f"Switching settings for: {key} with appended value of {value}.")
    else:
        json_change("settings.json", key, list_iter(set_lists(key), setval))
        log.debug(f"Switching settings for: {key} to {list_iter(set_lists(key), setval)}.")

def set_lists(key):
    match key:
        case "language": return ["english", "polish"]

def def_set(callout):
    set_dict = {
        "language":         "english",
        "time_system":      "proportional",
        "hunger_thirst":    False,
        "permadeath":       False,
        "legacy_unloading": False
    }
    return set_dict[callout]

# Returns next element from the list
def list_iter(lv: list, element):
    lv = list(dict.fromkeys(lv)) # removes any duplicates
    ind = lv.index(element)
    if ind+1 >= len(lv): ind = -1
    return lv[ind+1]
from core.utils import *

def set_change(key, value=None):
  setval = json_read("settings.json", key)
  if type(setval) is bool:
      json_change("settings.json", key, not setval)
      log.debug(f"Switching settings for: {key} to {not setval}.")
  if type(setval) is int and type(value) is int:
      json_change_ins("settings.json", key, value)
      log.debug(f"Switching settings for: {key} with appended value of {value}.")
  # switch for time system
  #if json_read(path, key) == "proportional":
  #  json_change_ins(path, key, "realistic")
  #elif json_read(path, key) == "realistic":
  #  json_change_ins(path, key, "proportional")
  # switch for boolean elements

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
    if ind > len(lv): ind = 0
    return lv[ind+1]
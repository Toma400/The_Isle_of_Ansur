from core.utils import *

# changes settings depending on passed value type (automation similar to json_change_ins)
def set_change(key, value=None):
    setval = json_read("settings.json", key)
    if type(setval) is bool:
        json_change("settings.json", key, not setval)
        log.debug(f"Switching settings for: {key} to {not setval}.")
    elif type(setval) is int and type(value) is int:
        json_change_ins("settings.json", key, value)
        log.debug(f"Switching settings for: {key} with appended value of {value}. End value: {value+setval}.")
    elif type(setval) is int and "set=" in value:
        fval = value.replace("set=", ""); fval = int(fval)
        json_change("settings.json", key, fval)
        log.debug(f"Switching settings for: {key} to {value}.")
    elif type(setval) is float and type(value) is float:
        json_change_ins("settings.json", key, value)
        log.debug(f"Switching settings for: {key} with appended value of {value}. End value: {value + setval}.")
    else:
        if value is None: json_change("settings.json", key, list_iter(set_lists(key), setval))
        if value == "rev": json_change("settings.json", key, list_iter(set_lists(key), setval, True))
        log.debug(f"Switching settings for: {key} to {list_iter(set_lists(key), setval)}.")

# lists to iterate over by list_iter
def set_lists(key):
    match key:
        case "language": return ["english", "polish"]
        case "listbox_mode": return ["proportional", "sized"]

# returns default value of specific settings
def def_set(callout):
    set_dict = {
        "language":         "english",
        "res_x":            1000,
        "res_y":            700,
        "sound":            40,
        "log_limit":        15,
        "legacy_unloading": False,
        "listbox_mode":     "proportional"
    }
    return set_dict[callout]

# Returns next (or previous) element from the list
def list_iter(lv: list, element, rev=False):
    lv = list(dict.fromkeys(lv)); lv.sort() # removes any duplicates and sorts list vals alphabetically
    ind = lv.index(element)
    if not rev: # return next element (default)
        if ind+1 >= len(lv): ind = -1
        return lv[ind+1]
    else: # return previous element
        if ind-1 < 0: ind = len(lv)
        return lv[ind-1]
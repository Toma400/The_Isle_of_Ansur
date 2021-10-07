def default_settings(callout=None):
  time_system = "proportional"
  hunger_thirst = False
  permadeath = False
  if callout == "time_system":
    return time_system
  elif callout == "hunger_thirst":
    return hunger_thirst
  elif callout == "permadeath":
    return permadeath

def version_call(selector):
  if selector == "game_version":
    return "pre-alpha 1"
  elif selector == "save_system":
    return "1.0"

def settings(callout):
  import system.json_manag
  if callout == "time_system":
    return system.json_manag.json_read("system/system_settings.json", "time_system")
  elif callout == "hunger_thirst":
    return system.json_manag.json_read("system/system_settings.json", "hunger_thirst")
  elif callout == "permadeath":
    return system.json_manag.json_read("system/system_settings.json", "permadeath")

def settings_changer(callout):
  import system.json_manag
  path = "system/system_settings.json"
  if system.json_manag.json_read(path, callout) == "proportional":
    system.json_manag.json_change_ins(path, callout, "realistic")
  elif system.json_manag.json_read(path, callout) == "realistic":
    system.json_manag.json_change_ins(path, callout, "proportional")
  elif system.json_manag.json_read(path, callout) == True:
    system.json_manag.json_change_ins(path, callout, False)
  elif system.json_manag.json_read(path, callout) == False:
    system.json_manag.json_change_ins(path, callout, True)
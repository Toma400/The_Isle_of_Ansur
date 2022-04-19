def default_settings(callout=None):
  time_system = "proportional"
  hunger_thirst = False
  permadeath = False
  autoimport_packs = True
  if callout == "time_system":
    return time_system
  elif callout == "hunger_thirst":
    return hunger_thirst
  elif callout == "permadeath":
    return permadeath
  elif callout == "autoimport_packs":
    return autoimport_packs

#-------------------------------
# VERSION CALL
# Returns version of game/systems
# being current. Versioning can
# be found in docs (glossary.md).
#-------------------------------
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
  elif callout == "autoimport":
    return system.json_manag.json_read("system/system_settings.json", "autoimport_of_packs")

#-----------------------------
# SETTINGS CHANGER
# Switches settings' values
#-----------------------------
def settings_changer(callout):
  import system.json_manag
  import logging as log
  path = "system/system_settings.json"
  # switch for time system
  if system.json_manag.json_read(path, callout) == "proportional":
    system.json_manag.json_change_ins(path, callout, "realistic")
  elif system.json_manag.json_read(path, callout) == "realistic":
    system.json_manag.json_change_ins(path, callout, "proportional")
  # switch for boolean elements
  elif system.json_manag.json_read(path, callout) == True:
    system.json_manag.json_change_ins(path, callout, False)
  elif system.json_manag.json_read(path, callout) == False:
    system.json_manag.json_change_ins(path, callout, True)
  #------
  # LOGS
  #------
  if system.json_manag.json_read(path, callout) == "proportional":
    log.debug("Switching settings for: " + callout + "to realistic.")
  elif system.json_manag.json_read(path, callout) == "realistic":
    log.debug("Switching settings for: " + callout + "to proportional.")
  elif system.json_manag.json_read(path, callout) == True:
    log.debug("Switching settings for: " + callout + "to False.")
  elif system.json_manag.json_read(path, callout) == False:
    log.debug("Switching settings for: " + callout + "to True.")
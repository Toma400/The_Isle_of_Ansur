from system.ref_systems.system_ref import SysRef
from system.json_manag import *
from utils.decorators import *

def default_settings(callout=None):
  language = "english"
  time_system = "proportional"
  hunger_thirst = False
  permadeath = False
  legacy_unloading = False
  if callout == "language":
    return language
  if callout == "time_system":
    return time_system
  elif callout == "hunger_thirst":
    return hunger_thirst
  elif callout == "permadeath":
    return permadeath
  elif callout == "legacy_unloading":
    return legacy_unloading

#-------------------------------
# VERSION CALL
# Returns version of game/systems
# being current. Versioning can
# be found in docs (glossary.md).
#-------------------------------

@Deprecated("core.utils | settings constants")
def settings(callout):
  if callout == "language":
    return json_read("system/system_settings.json", "language")
  elif callout == "time_system":
    return json_read("system/system_settings.json", "time_system")
  elif callout == "hunger_thirst":
    return json_read("system/system_settings.json", "hunger_thirst")
  elif callout == "permadeath":
    return json_read("system/system_settings.json", "permadeath")
  elif callout == "legacy_unpacking":
    return json_read("system/system_settings.json", "legacy_unpacking")

#-----------------------------
# SETTINGS CHANGER
# Switches settings' values
#-----------------------------
def settings_changer(callout):
  import logging as log
  path = "system/system_settings.json"
  # switch for time system
  if json_read(path, callout) == "proportional":
    json_change_ins(path, callout, "realistic")
  elif json_read(path, callout) == "realistic":
    json_change_ins(path, callout, "proportional")
  # switch for boolean elements
  elif json_read(path, callout) is True:
    json_change_ins(path, callout, False)
  elif json_read(path, callout) is False:
    json_change_ins(path, callout, True)
  #------
  # LOGS
  #------
  if json_read(path, callout) == "proportional":
    log.debug(f"Switching settings for: {callout} to realistic.")
  elif json_read(path, callout) == "realistic":
    log.debug(f"Switching settings for: {callout} to proportional.")
  elif json_read(path, callout) is True:
    log.debug(f"Switching settings for: {callout} to False.")
  elif json_read(path, callout) is False:
    log.debug(f"Switching settings for: {callout} to True.")
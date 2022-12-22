from utils.repo_manag import dir_checker as dir_check

#--------------------------------------------------------
# MOD LISTER
# Returns list with mods loaded. Can exclude core mod if
# needed.
#--------------------------------------------------------
def mod_lister (directory, system="full"):
  if directory == "stats":
    #checks whether mod is in stats directory
    path = "stats/"
    mod_loaded = dir_check(path, "dir")
    return lister(mod_loaded, system)
  elif directory == "worlds":
    #checks whether mod is in worlds directory
    path = "worlds/"
    mod_loaded = dir_check(path, "dir")
    return lister(mod_loaded, system)
  elif directory == "all":
    #lists all mods altogether
    path1 = "stats/"
    path2 = "worlds/"
    mod_loaded = dir_check(path1, "dir")
    mod_loaded.append (dir_check(path2, "dir"))
    return lister(mod_loaded, system)
  elif directory == "both":
    #lists only globalpacks
    path1 = "stats/"
    path2 = "worlds/"
    mod_loaded = list(set(dir_check(path1, "dir")) & set(dir_check(path2, "dir")))
    return lister(mod_loaded, system)

#--------------------------------------------------------
# MOD CHECKER
# Checks if mod is loaded
#--------------------------------------------------------
def mod_checker (directory, name):
  if directory == "stats":
    mod_loaded = mod_lister ("stats")
    return checker(name, mod_loaded)

  elif directory == "worlds":
    mod_loaded = mod_lister ("worlds")
    return checker(name, mod_loaded)

  elif directory == "all":
    #checks whether mod is in any of two directories (OR)
    mod_loaded = mod_lister ("all")
    return checker(name, mod_loaded)

  elif directory == "both":
    #checks whether mod is in both directories (AND)
    mod_loaded = mod_lister ("both")
    return checker(name, mod_loaded)

# --------------------------------------------------------
# MOD READER
# Reads specific information from mod info.json file
# --------------------------------------------------------
def mod_reader(name, value):
  from os.path import isfile as search
  from system.json_manag import json_read as read
  path_s = f"stats/{name}/info.json"
  path_w = f"worlds/{name}/info.json"
  if not search(path_s):
    if not search(path_w):
      if value == "name":
        return name_formatter(name)
      elif value == "credits":
        return str(None)
      else:
        return value.title() + " not found"
    else:
      return read(path_w, value)
  else:
    return read(path_s, value)
    # checks if there's file in stats/, if not then goes to
    # worlds/, if not then returns either formatted name,
    # or message of not-found element

#--------------------------------------------------------
# MOD BLACKLISTER
# Used to either blacklist/whitelist specific mod, or
# to return value if specific mod is blacklisted
#--------------------------------------------------------
def mod_blacklister(mod, is_blacklisted=False):
  from system.json_manag import json_read as read
  from system.json_manag import json_write as write
  blacklist = read("system/blackloading.json", "", True)
  if is_blacklisted:
    return mod in blacklist
  else:
    if mod in blacklist:
      blacklist.remove(mod)
    else:
      blacklist.append(mod)
    write("system/blackloading.json", blacklist)

#--------------------------------------------------------
# ID BUILDER
# Small function to unclutter ID building
#--------------------------------------------------------
def id_builder(mod_id, item):
  return mod_id + ":" + item

#--------------------------------------------------------
# LOADERS
# Load full list of races/classes from all packs that are
# inside files. Return list of RIDs/CIDs.
#--------------------------------------------------------
def rid_loader ():
  import system.json_manag
  mods_loaded = mod_lister("stats")
  races_loaded = []
  for i in mods_loaded:
    try:
      path = f"stats/{i}/races.json"
      temp_dir = len(system.json_manag.json_read(path))
      for j in range(temp_dir):
        element = (system.json_manag.json_read(path)[j])
        races_loaded.append(id_builder(i, element))
        overflow_protector(races_loaded, "RID")
    except FileNotFoundError:
      continue
  return races_loaded

def cid_loader ():
  import system.json_manag
  mods_loaded = mod_lister("stats")
  classes_loaded = []
  for i in mods_loaded:
    try:
      path = f"stats/{i}/classes.json"
      temp_dir = len(system.json_manag.json_read(path))
      for j in range(temp_dir):
        element = (system.json_manag.json_read(path)[j])
        classes_loaded.append(id_builder(i, element))  # previously inside append: system.json_manag.json_subread(path, element, "class_id")
        overflow_protector(classes_loaded, "CID")
    except FileNotFoundError:
      continue
  return classes_loaded

#--------------------------------------------------------
# SIMPLIFIERS
# Functions to simplify the code above
#--------------------------------------------------------
def lister (mod_loaded, system):
  if system == "modded":
    mod_loaded.remove("ansur")
    return mod_loaded
  if system == "full":
    return mod_loaded

def checker (name, loaded_value):
  if name in loaded_value:
    return True
  else:
    return False

def name_formatter (name):
  # used for simplified name formatting into readable state
  name = name.replace("_", " ")
  name = name.title()
  return name

#--------------------------------------------------------
# OVERFLOW PROTECTOR
# Function taking care of (probably never reachable)
# overflow of mod elements. If list reaches specific
# limit amount, prints message and backs to menu
#--------------------------------------------------------
def overflow_protector (list_, module):
  from utils.text_manag import colour_formatter as colour
  import time
  import gui.menu
  import sys
  limit = sys.maxsize / 2
  if len(list_) >= limit:
    print (colour("red", f"Limit of loaded elements for module: {module} reached! Terminating the game."))
    time.sleep(10)
    gui.menu.start()
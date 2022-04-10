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
    path1 = "stats/"
    path2 = "worlds/"
    mod_loaded = dir_check(path1, "dir")
    mod_loaded.append (dir_check(path2, "dir"))
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
    path1 = "stats/"
    path2 = "worlds/"   
    mod_loaded1 = dir_check(path1, "dir")
    mod_loaded2 = dir_check(path2, "dir")
    mods_loaded = set(mod_loaded1) & set(mod_loaded2)
    return checker(name, mods_loaded)

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
  import system.mod_manag
  import system.json_manag
  mods_loaded = system.mod_manag.mod_lister("stats")
  races_loaded = []
  for i in mods_loaded:
    try:
      path = "stats/" + i + "/races.json"
      temp_dir = len(system.json_manag.json_read(path, "list", True))
      for j in range(temp_dir):
        element = (system.json_manag.json_read(path, "list", True)[j])
        races_loaded.append(id_builder(i, element))  # previously inside append: system.json_manag.json_subread(path, element, "race_id")
    except FileNotFoundError:
      continue
  return races_loaded

def cid_loader ():
  import system.mod_manag
  import system.json_manag
  mods_loaded = system.mod_manag.mod_lister("stats")
  classes_loaded = []
  for i in mods_loaded:
    try:
      path = "stats/" + i + "/classes.json"
      temp_dir = len(system.json_manag.json_read(path, "list", True))
      for j in range(temp_dir):
        element = (system.json_manag.json_read(path, "list", True)[j])
        classes_loaded.append(id_builder(i, element))  # previously inside append: system.json_manag.json_subread(path, element, "class_id")
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
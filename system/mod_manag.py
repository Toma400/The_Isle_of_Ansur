from utils.repo_manag import dir_checker as dir_check

def mod_lister (directory, system="full"):
  if directory == "stats":
    #checks whether mod is in stats directory
    path = "stats/"
    mod_loaded = dir_check(path, "dir")
    if system == "modded":
      mod_loaded.remove ("ansur")
      return mod_loaded
    if system == "full":
      return mod_loaded
  elif directory == "worlds":
    #checks whether mod is in worlds directory
    path = "worlds/"
    mod_loaded = dir_check(path, "dir")
    if system == "modded":
      mod_loaded.remove ("ansur")
      return mod_loaded
    if system == "full":
      return mod_loaded
  elif directory == "all":
    path1 = "stats/"
    path2 = "worlds/"
    mod_loaded = dir_check(path1, "dir")
    mod_loaded.append (dir_check(path2, "dir"))
    if system == "modded":
      mod_loaded.remove ("ansur")
      return mod_loaded
    if system == "full":
      return mod_loaded

def mod_checker (directory, name):
  if directory == "stats":
    mod_loaded = mod_lister ("stats")
    if name in mod_loaded:
      return True
    else:
      return False
  elif directory == "worlds":
    mod_loaded = mod_lister ("worlds")
    if name in mod_loaded:
      return True
    else:
      return False
  elif directory == "all":
    #checks whether mod is in any of two directories (OR)
    mod_loaded = mod_lister ("all")
    if name in mod_loaded:
      return True
    else:
      return False
  elif directory == "both":
    #checks whether mod is in both directories (AND)
    path1 = "stats/"
    path2 = "worlds/"   
    mod_loaded1 = dir_check(path1, "dir")
    mod_loaded2 = dir_check(path2, "dir")
    mods_loaded = set(mod_loaded1) & set(mod_loaded2)
    if name in mods_loaded:
      return True
    else:
      return False

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
        races_loaded.append(i + ":" + element)  # previously inside append: system.json_manag.json_subread(path, element, "race_id")
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
        classes_loaded.append(i + ":" + element)  # previously inside append: system.json_manag.json_subread(path, element, "class_id")
    except FileNotFoundError:
      continue
  return classes_loaded
import utils.repo_manag

def mod_lister (directory, system="full"):
  if directory == "stats":
    #checks whether mod is in stats directory
    path = "stats/"
    mod_loaded = utils.repo_manag.dir_checker(path, "dir")
    if system == "modded":
      mod_loaded.remove ("ansur")
      return mod_loaded
    if system == "full":
      return mod_loaded
  elif directory == "worlds":
    #checks whether mod is in worlds directory
    path = "worlds/"
    mod_loaded = utils.repo_manag.dir_checker(path, "dir")
    if system == "modded":
      mod_loaded.remove ("ansur")
      return mod_loaded
    if system == "full":
      return mod_loaded
  elif directory == "all":
    path1 = "stats/"
    path2 = "worlds/"
    mod_loaded = utils.repo_manag.dir_checker(path1, "dir")
    mod_loaded.append (utils.repo_manag.dir_checker(path2, "dir"))
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
    mod_loaded1 = utils.repo_manag.dir_checker(path1, "dir")
    mod_loaded2 = utils.repo_manag.dir_checker(path2, "dir")
    mods_loaded = set(mod_loaded1) & set(mod_loaded2)
    if name in mods_loaded:
      return True
    else:
      return False
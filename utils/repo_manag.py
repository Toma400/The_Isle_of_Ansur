def file_deleting (pathage):
  import os
  import shutil
  try:
    shutil.rmtree(pathage)
  except NotADirectoryError:
    os.remove(pathage)
  except FileNotFoundError:
    pass
  del shutil

def dir_checker (path, separator, extension="None"):
  if separator == "Dir":
    from os import listdir
    from os.path import isdir, join
    return [f for f in listdir(path) if isdir(join(path, f))]
  elif separator == "File":
    from os import listdir
    from os.path import isfile, join
    return [f for f in listdir(path) if isfile(join(path, f))]
  elif separator == "File+":
    import glob
    listed = glob.glob(path + "*." + extension)
    listed2 = []
    for i in listed:
      i = i.replace(path, "")
      listed2.append (i.replace("." + extension, ""))
    return listed2
  elif separator == "All":
    import glob
    listed = glob.glob(path + "*")
    listed2 = []
    for i in listed:
      listed2.append (i.replace(path, ""))
    return listed2

def mod_lister (directory, system="Full"):
  import glob
  if directory == "stats":
    #checks whether mod is in stats directory
    path = "stats/"
    mod_loaded = dir_checker(path, "Dir")
    if system == "Modded":
      mod_loaded.remove ("ansur")
      return mod_loaded
    if system == "Full":
      return mod_loaded
  elif directory == "worlds":
    #checks whether mod is in worlds directory
    path = "worlds/"
    mod_loaded = dir_checker(path, "Dir")
    if system == "Modded":
      mod_loaded.remove ("ansur")
      return mod_loaded
    if system == "Full":
      return mod_loaded
  elif directory == "all":
    path1 = "stats/"
    path2 = "worlds/"
    mod_loaded = dir_checker(path1, "Dir")
    mod_loaded.append (dir_checker(path2, "Dir"))
    if system == "Modded":
      mod_loaded.remove ("ansur")
      return mod_loaded
    if system == "Full":
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
    mod_loaded = mod_lister ("All")
    if name in mod_loaded:
      return True
    else:
      return False
  elif directory == "both":
    #checks whether mod is in both directories (AND)
    path1 = "stats/"
    path2 = "worlds/"   
    mod_loaded1 = dir_checker(path1, "Dir")
    mod_loaded2 = dir_checker(path2, "Dir")
    mods_loaded = set(mod_loaded1) & set(mod_loaded2)
    if name in mods_loaded:
      return True
    else:
      return False
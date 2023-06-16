from os.path import join, isdir, isfile
from os import listdir
import os, shutil, logging

gpath = os.path.dirname(os.path.abspath("main.py"))
#================|========================================
# DIR FUNCTIONS  | To orientate between dirs and files
#================|========================================
# A bit different from original, it does return full path
def dir_checker (path, separator, extension=None, no_path=False):
  if separator == "dir":
    from os import listdir
    return [f for f in listdir(path) if isdir(join(path, f))]

  elif separator == "file" and extension is None:
    from os import listdir
    return [f for f in listdir(path) if isfile(join(path, f))]

  elif separator == "file":
    import glob
    listed = glob.glob(path + "*." + extension)
    if no_path: return no_pather(listed, path)
    return listed

  elif separator == "all":
    import glob
    listed = glob.glob(path + "*")
    if no_path: return no_pather(listed, path)
    return listed

# Checks if directory is empty
def empty_checker (path):
  return os.stat(path).st_size == 0

# "Safe" file deleter (flexible towards both folders and files)
def deleter (pathage):
  try: shutil.rmtree(pathage)
  except NotADirectoryError: os.remove(pathage)
  except FileNotFoundError: pass
  except PermissionError:
    print(f"Couldn't remove file {pathage} due to invalid permission.")

# Log deleting function ('num' should be None if manually removed)
def logs_deleting (num: int = None):
  all_logs = file_lister("core/logs\\", "log"); all_logs.sort()
  full_num = len(all_logs)
  if num is not None:
    if full_num > num:
      del_num = full_num - num
      for ui, u in enumerate(all_logs):
        if ui < del_num:
          print(u)
          deleter(f"{gpath}/core/logs/{u}.log")
  else:
    for u in all_logs: deleter(f"{gpath}/core/logs/{u}.log")
    logging.debug("Removed all logs with request of the user.")

#================|========================================
# LISTERS        | Lists things within said directory
#================|========================================
def dir_lister (path):
  return [f for f in listdir(path) if isdir(join(path, f))]

def file_lister (path, ext=None):
  if ext is None:
    return [f for f in listdir(path) if isfile(join(path, f))]
  else:
    import glob; listed = glob.glob(path + "*." + ext); listed2 = []
    for i in listed:
      i = i.replace(path, "")
      listed2.append(i.replace("." + ext, ""))
    return listed2

def deep_file_lister (path, ext=None):
  list1 = file_lister(path, ext)
  while len(dir_lister(path)) > 0: # searches in nested directories
    for i in dir_lister(path):
      path = f"{path}/{i}/"
      ilist = file_lister(path, ext)
      for j in ilist: list1.append(j)
  return list1

#================|========================================
# SYSTEM RELATED | Related to system file operations
#================|========================================
# Creates necessary folders for .gitignore elements
def folder_init():
  folders = [
    f"{gpath}/core/logs", f"{gpath}/saves"
  ]
  for i in folders:
    if not os.path.isdir(i): os.makedirs(i)

#================|========================================
# UNSPAGHETTIERS | Making code a bit cleaner
#================|========================================
def no_pather(given_list, path):
    returned_list = []
    for i in given_list:
        returned_list.append(i.replace(path, ""))
    return returned_list
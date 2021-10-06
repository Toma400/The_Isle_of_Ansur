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
  if separator == "dir":
    from os import listdir
    from os.path import isdir, join
    return [f for f in listdir(path) if isdir(join(path, f))]
  elif separator == "file":
    from os import listdir
    from os.path import isfile, join
    return [f for f in listdir(path) if isfile(join(path, f))]
  elif separator == "file+":
    import glob
    listed = glob.glob(path + "*." + extension)
    listed2 = []
    for i in listed:
      i = i.replace(path, "")
      listed2.append (i.replace("." + extension, ""))
    return listed2
  elif separator == "all":
    import glob
    listed = glob.glob(path + "*")
    listed2 = []
    for i in listed:
      listed2.append (i.replace(path, ""))
    return listed2

def empty_checker (path):
  import os
  if os.stat(path).st_size == 0:
    return True
  else:
    return False
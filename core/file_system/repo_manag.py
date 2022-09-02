from os.path import join, isdir, isfile

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

#================|========================================
# UNSPAGHETTIERS | Making code a bit cleaner
#================|========================================
def no_pather(given_list, path):
    returned_list = []
    for i in given_list:
        returned_list.append(i.replace(path, ""))
    return returned_list
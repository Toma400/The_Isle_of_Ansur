def directory_call():
  import os
  path = os.getcwd()
  print ("The current working directory is %s" % path)
  return path

def folder_creating(name):
  import os
  import utils.text
  path = "saves/" + name
  print (path)
  if os.path.isdir(path) == True:
    print (utils.text.text_align("--- Not able to create player profile, the name is taken. Please use different name instead ---", "centre"))
  else:
    try:
      os.makedirs(path)
    except OSError:
      print ("Creation of the directory %s failed" % path)
    else:
      print ("Successfully created the directory %s" % path)
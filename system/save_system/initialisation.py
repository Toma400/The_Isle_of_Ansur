def directory_call():
  import os
  path = os.getcwd()
  print ("The current working directory is %s" % path)
  return path

def folder_creating(name):
  import os
  import utils.text
  path = "saves/" + name
  if os.path.isdir(path) == True:
    print (utils.text.text_align("※ Not able to create player profile, the name is taken. Please use different name instead ※", "centre"))
    return False
  else:
    try:
      os.makedirs (path)
      profile_creating (path)
      return True
    except OSError:
      print ("Creation of the directory %s failed" % path)
      return False
    else:
      #print ("Successfully created the directory %s" % path)
      pass

def profile_creating(path):
  import os
  deeper_path = path + "/in_use"
  temp_var = "/"
  save_jsons = ["quests.json", "inventory.json", "world.json", "profile.json"]
  #creating subfolder
  try:
    os.makedirs(deeper_path)
  except OSError:
    print ("Creation of the directory %s failed" % path)
  else:
    pass
  #creating jsons for main folder and subfolder
  for i in save_jsons:
    creating = open(path + temp_var + i, "a")
  for j in save_jsons:
    creating2 = open(deeper_path + temp_var + j, "a")
    stats_creating(deeper_path, "profile")
    stats_creating(deeper_path, "inventory")
    stats_creating(deeper_path, "quests")
    stats_creating(deeper_path, "world")

def stats_creating(path, set):
  if set == "profile":
    deeper_path = path + "/profile.json"
    import json
    import stats.default_stats
    default_stats = {}
    default_stats.update (stats.default_stats.profile.not_default_stats)
    default_stats.update (stats.default_stats.profile.general_stats)
    default_stats.update (stats.default_stats.profile.attributes)
    default_stats.update (stats.default_stats.profile.abilities)
    default_stats.update (stats.default_stats.profile.perks)
    default_stats.update (stats.default_stats.profile.settings)
    with open (deeper_path,'w') as file:
      json.dump(default_stats, file, indent = 2)
  elif set == "inventory":
    deeper_path = path + "/inventory.json"
    import json
    import stats.default_stats
    default_stats = {}
    with open (deeper_path,'w') as file:
      json.dump(default_stats, file, indent = 2)
  elif set == "quests":
    deeper_path = path + "/quests.json"
    import json
    import stats.default_stats
    default_stats = {}
    with open (deeper_path,'w') as file:
      json.dump(default_stats, file, indent = 2)
  elif set == "world":
    deeper_path = path + "/world.json"
    import json
    import stats.default_stats
    default_stats = {}
    with open (deeper_path,'w') as file:
      json.dump(default_stats, file, indent = 2)
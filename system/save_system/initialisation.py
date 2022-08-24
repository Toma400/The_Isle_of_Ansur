import logging as log

def directory_call():
  import os
  path = os.getcwd()
  print ("The current working directory is %s" % path)
  return path

def folder_creating(name):
  import os
  import utils.text_manag as util
  path = f"saves/{name}"
  if os.path.isdir(path) == True:
    print (util.colour_formatter("yellow", "※ Not able to create player profile, the name is taken. Please use different name instead ※"))
    log.debug("Name is taken.")
    return False
  else:
    try:
      os.makedirs (path)
      profile_creating (path)
      return True
    except OSError:
      print ("Creation of the directory %s failed" % path)
      log.debug("OSError occured.")
      return False

def profile_creating(path):
  import os
  deeper_path = f"{path}/in_use"
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
    deeper_path = f"{path}/profile.json"
    import json
    import system.ref_systems.default_stats
    default_stats = {}
    default_stats.update (system.ref_systems.default_stats.profile.not_default_stats)
    default_stats.update (system.ref_systems.default_stats.profile.general_stats)
    default_stats.update (system.ref_systems.default_stats.profile.attributes)
    default_stats.update (system.ref_systems.default_stats.profile.skills)
    default_stats.update (system.ref_systems.default_stats.profile.perks)
    default_stats.update (system.ref_systems.default_stats.profile.settings)
    with open (deeper_path,'w') as file:
      json.dump(default_stats, file, indent = 2)

  elif set == "inventory":
    deeper_path = f"{path}/inventory.json"
    import json
    import system.ref_systems.default_stats
    default_stats = {}
    default_stats.update (system.ref_systems.default_stats.inventory.main_slots)
    with open (deeper_path,'w') as file:
      json.dump(default_stats, file, indent = 2)

  elif set == "quests":
    deeper_path = f"{path}/quests.json"
    import json
    import system.ref_systems.default_stats
    default_stats = {}
    with open (deeper_path,'w') as file:
      json.dump(default_stats, file, indent = 2)

  elif set == "world":
    deeper_path = f"{path}/world.json"
    import json
    import system.ref_systems.default_stats
    default_stats = {}
    with open (deeper_path,'w') as file:
      json.dump(default_stats, file, indent = 2)
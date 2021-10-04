import system.json_manag

def full_save (name):
  import json
  temp_list = ["inventory", "profile", "quests", "world"]
  world_list = [] #here we should have full list of worlds and make them appear during generation/load/save
  temp2_list = []
  if not world_list:
    pass
  else:
    #for "modded worlds"
    for i in world_list:
      temp2_list.append("world_" + i)
    temp_list.append(temp2_list)
  for j in temp_list:
    try:
      system.json_manag.save_change(name, j, 0, "game_save", 0, False)
    except json.decoder.JSONDecodeError:
      print ("JSON File: " + j + ".json does not have any arguments. Skipping.")

def full_load (name):
  import json
  temp_list = ["inventory", "profile", "quests", "world"]
  world_list = [] #here we should have full list of worlds and make them appear during generation/load/save
  temp2_list = []
  if not world_list:
    pass
  else:
    #for "modded worlds"
    for i in world_list:
      temp2_list.append("world_" + i)
    temp_list.append(temp2_list)
  for j in temp_list:
    try:
      system.json_manag.save_change(name, j, 0, "game_load", 0)
    except json.decoder.JSONDecodeError:
      print ("JSON File: " + j + ".json does not have any arguments. Skipping.")
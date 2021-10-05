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
    system.json_manag.save_change(name, j, 0, "game_save", 0, False)

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
    system.json_manag.save_change(name, j, 0, "game_load", 0)
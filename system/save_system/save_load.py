import system.json_manag

def full_save (name):
  import system.mod_manag
  temp_list = ["inventory", "profile", "quests", "world"]
  world_list = system.mod_manag.mod_lister("worlds", "modded") #here we should have full list of worlds and make them appear during generation/load/save
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
  import system.mod_manag
  temp_list = ["inventory", "profile", "quests", "world"]
  world_list = system.mod_manag.mod_lister("worlds", "modded") #here we should have full list of worlds and make them appear during generation/load/save
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

def deep_load (name):
  #differs from full_load that it checks settings integrity and returns true if everything worked properly
  import utils.text_manag as util
  try:
    settings_checklist = ["time_system", "hunger_thirst", "permadeath"]
    error_count = 0
    for i in settings_checklist:
      #i - key, json_read - key value
      profile_data = system.json_manag.save_read(name, "profile", i)
      settings_data = system.json_manag.json_read("system/system_settings.json", i)
      if profile_data != settings_data:
        print (util.colour_formatter("yellow", "Found difference between system settings and save settings with: " + i))
        #time system difference
        error_count = error_count + 1
        if i == "time_system" and profile_data == "proportional" or i == "hunger_thirst" and profile_data == False:
          temp_var = input(
            util.align ("Do you want your save file settings be changed? [Y/N]", "centre_colour")).lower()
          if temp_var == "y":
            system.json_manag.save_change_ins(name, "profile", i, settings_data)
            error_count = error_count - 1
            pass
          else:
            deep_load_error()
        elif i == "time_system" and profile_data == "realistic" or i == "hunger_thirst" and profile_data == True:
          deep_load_error(True)
      else:
        pass
    if error_count == 0:
      import gui.interface
      full_load(name)
      gui.interface.main_game (name)
  except FileNotFoundError:
    deep_load_error("name")

def deep_load_error (critical=False):
  import time
  import gui.menu
  from utils.text_manag import colour_formatter as colour
  if critical is True:
    print (colour("yellow", "Unfortunately that setting can't be set back to default. Please change your settings in menu to fit that save file."))
  if critical is "name":
    print (colour("yellow", "No character profile is found with that name. Please make sure you wrote it correctly."))
    print (colour("yellow", "[case sensitivity matters]"))
  print (colour("yellow", "Redirecting to game menu."))
  time.sleep(1)
  gui.menu.start()
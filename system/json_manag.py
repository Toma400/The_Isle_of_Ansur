def json_read(path, element, dict_type=False):
  import json
  data = {}
  with open(path) as json_file:
    data = json.load(json_file)
  if dict_type == False:
    return data[element]
  else:
    return data

def json_change(path, element, change_type, change_value):
  #change type identifies whether you want to do replacement, maths or var addition
  #replacement - it simply makes value X become value Y
  #maths - it adds value X to value Y (3+4=7, str+str=strstr)
  #var addition - compatibility type, adds another variable with specified default value - possibly using within "save_system" type of thing, when element needs to be updated
  import json
  #json_file = open (path, "r")
  #^ function a bit obsolete, but can be used to non-save related things, such as objects with non-changeable directory (default worlds/Ansur elements, for example)
  #for [modded] worlds/X elements though, another loader can be necessary

def save_read(name, category, element, dict_type=False):
  import json
  final_path = "saves/" + name + "/in_use/" + category + ".json"
  data = {}
  with open(final_path) as json_file:
    data = json.load(json_file)
  if dict_type == False:
    return data[element]
  else:
    return data
  #element tells what type of variable is needed to be read

def save_change(name, category, element, change_type, change_value, in_use=True):
  #in_use=True is for all data elements within game, =False for saving game
  import json
  if in_use == True:
    final_path = "saves/" + name + "/in_use/" + category + ".json"
    #simply replacing value with new one (usually for string variables)
    if change_type == "replace":
      temp_dict = save_read(name, category, element, True)
      temp_dict[element] = change_value
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)
    #math is intended to change value with +/- (use negative value to make it smaller)
    elif change_type == "math":
      temp_dict = save_read(name, category, element, True)
      temp_dict[element] = temp_dict[element] + change_value
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)
    #math, but for (*) [rare case]
    elif change_type == "math*":
      temp_dict = save_read(name, category, element)
      temp_dict[element] = temp_dict[element] * change_value
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)
    #math, but for (/) [rare case]
    elif change_type == "math/":
      temp_dict = save_read(name, category, element)
      temp_dict[element] = temp_dict[element] / change_value
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)
    #var_add is intended to be dict; can be useful with version_updater especially
    elif change_type == "var_add":
      temp_dict = save_read(name, category, element, True)
      temp_dict.update (change_value)
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)
    #var_add, but for deleting; change_value can be anything in this case
    elif change_type == "var_del":
      temp_dict = save_read(name, category, element, True)
      temp_dict.remove (element)
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)
    #for loading the game (uses load_read)
    elif change_type == "game_load":
      temp_dict = load_read(name, category, element, True)
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)
  elif in_use == False:
    #for game saving | 'element' and 'change_value' can be anything
    if change_type == "game_save":
      final_path = "saves/" + name + "/" + category + ".json"
      temp_dict = save_read(name, category, element, True)
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)

def load_read(name, category):
  #for loading the game
  import json
  final_path = "saves/" + name + "/" + category + ".json"
  data = {}
  with open(final_path) as json_file:
    data = json.load(json_file)
  return data
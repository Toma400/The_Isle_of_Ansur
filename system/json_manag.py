#inventory is managed by its separate instance (gui/inventory.py)
import json

def json_read(path, element, dict_type=False):
  data = {}
  try:
    with open(path) as json_file:
      data = json.load(json_file)
    if dict_type == False:
      return data[element]
    if dict_type == True and element == "list":
      #returns list with keys instead of dict
      return [*data]
    else:
      return data
  except json.decoder.JSONDecodeError:
    print (f"JSON File: {path} does not have any arguments. Skipping.")

#--------------------------------------
# SUBREAD
# Reads second key of .json file
#--------------------------------------
def json_subread(path, element, subelement):
  #used to call values of objects from ID
  subdata = json_read(path, element)[0]
  return subdata[subelement]

#--------------------------------------
# KEYREAD
# Reads first key of .json file
#--------------------------------------
def json_keyread(path, element):
  #used to call objects from ID
  subdata = json_read(path, element)[0]
  return subdata

def json_write(path, dictionary):
  creating = open(path, "a")
  with open (path, 'w') as json_file:
    json.dump(dictionary, json_file, indent = 2)

#--------------------------------------------------------------
# JSON_CHANGE
# Multitask function to operate on .json files, depending on
# `change_type` string you put there.
# Can perform:
#
# * replacing values with new ones
# * replacing math values with relative ones
# * adding variables to .jsons
# * removing variables from .jsons
#--------------------------------------------------------------
def json_change(path, element, change_type, change_value):
  temp_dict = {}
  #simply replacing value with new one (usually for string variables)
  if change_type == "replace":
    temp_dict = json_read(path, element, True)
    temp_dict[element] = change_value
    with open (path,'w') as file:
      json.dump(temp_dict, file, indent = 2)
  #math is intended to change value with +/- (use negative value to make it smaller)
  elif change_type == "math":
    temp_dict = json_read(path, element, True)
    temp_dict[element] = int(temp_dict[element]) + int(change_value)
    with open (path,'w') as file:
      json.dump(temp_dict, file, indent = 2)
  #math, but for (*) [rare case]
  elif change_type == "math*":
    temp_dict = json_read(path, element, True)
    temp_dict[element] = int(temp_dict[element]) * int(change_value)
    with open (path,'w') as file:
      json.dump(temp_dict, file, indent = 2)
  #math, but for (/) [rare case]
  elif change_type == "math/":
    temp_dict = json_read(path, element, True)
    temp_dict[element] = int(temp_dict[element]) / int(change_value)
    with open (path,'w') as file:
      json.dump(temp_dict, file, indent = 2)
  #var_add is intended to be dict; can be useful with version_updater especially
  elif change_type == "var_add":
    temp_dict = json_read(path, element, True)
    temp_dict.update (change_value)
    with open (path,'w') as file:
      json.dump(temp_dict, file, indent = 2)
  #var_add, but for deleting; change_value can be anything in this case
  elif change_type == "var_del":
    temp_dict = json_read(path, element, True)
    temp_dict.remove (element)
    with open (path,'w') as file:
      json.dump(temp_dict, file, indent = 2)

#--------------------------------------------------------------
# JSON_CHANGE_INS(ENSITIVE)
# Variant of Json_Change function, automatically recognising
# type of value. From obvious reasons, more convenient for
# automating, having less broad use instead.
#--------------------------------------------------------------
def json_change_ins(path, element, change_value, extended_math=False):
  #basically variable type insensitive variant of json_change()
  #detects type and redirects for its type; automation friendly 
  #useful for dicts with various types of variables, which needs to be looped
  if extended_math == False:
    #int/str detector (int can use "math", str not)
    if type(change_value) == int:
      json_change(path, element, "math", change_value)
    elif type(change_value) == str or type(change_value) == bool:
      json_change(path, element, "replace", change_value)
  elif extended_math == "*":
    json_change(path, element, "math*", change_value)
  elif extended_math == "/":
    json_change(path, element, "math/", change_value)

def save_read(name, category, element, dict_type=False):
  final_path = "saves/" + name + "/in_use/" + category + ".json"
  data = {}
  try:
    with open (final_path) as json_file:
      data = json.load(json_file)
    if dict_type == False:
      return data[element]
    else:
      return data
  except json.decoder.JSONDecodeError:
    print (f"JSON File: {final_path} does not have any arguments. Skipping.")
  #element tells what type of variable is needed to be read

def save_change(name, category, element, change_type, change_value, in_use=True):
  #in_use=True is for all data elements within game, =False for saving game
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
      temp_dict[element] = int(temp_dict[element]) + int(change_value)
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)

    #math, but for (*) [rare case]
    elif change_type == "math*":
      temp_dict = save_read(name, category, element)
      temp_dict[element] = int(temp_dict[element]) * int(change_value)
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)

    #math, but for (/) [rare case]
    elif change_type == "math/":
      temp_dict = save_read(name, category, element)
      temp_dict[element] = int(temp_dict[element]) / int(change_value)
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
      temp_dict = load_read(name, category)
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)
    #
    #-------------------- EOT

  elif in_use == False:
    #for game saving | 'element' and 'change_value' can be anything
    final_path = "saves/" + name + "/" + category + ".json"
    if change_type == "game_save":
      temp_dict = save_read(name, category, element, True)
      with open (final_path,'w') as file:
        json.dump(temp_dict, file, indent = 2)

def save_change_ins(name, category, element, change_value, extended_math=False):
  #basically variable type insensitive variant of save_change()
  #detects type and redirects for its type; automation friendly 
  #useful for dicts with various types of variables, which needs to be looped
  if extended_math == False:
    #int/str detector (int can use "math", str not)
    if type(change_value) == int:
      save_change(name, category, element, "math", change_value)
    elif type(change_value) == str or type(change_value) == bool:
      save_change(name, category, element, "replace", change_value)
  elif extended_math == "*":
    save_change(name, category, element, "math*", change_value)
  elif extended_math == "/":
    save_change(name, category, element, "math/", change_value)

def load_read(name, category):
  #for loading the game
  final_path = "saves/" + name + "/" + category + ".json"
  data = {}
  try:
    with open(final_path) as json_file:
      data = json.load(json_file)
    return data
  except json.decoder.JSONDecodeError:
    print (f"JSON File: {final_path} does not have any arguments. Skipping.")
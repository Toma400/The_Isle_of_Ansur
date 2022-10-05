import json, os, logging; gpath = os.path.dirname(os.path.abspath("main.py"))

#=====================|=========================================================================================
# MAIN JSON OPERATORS | Used to operate over .json files
#=====================|=========================================================================================
# Reads file and returns either value, dict or list
def json_read(path, element=None, isdict=True):
  try:
    fpath = f"{gpath}/{path}"
    with open(fpath, encoding="utf-8") as json_file:
      data = json.load(json_file)
    if element is None and isdict is True: return data     #returns dict
    if element is None and isdict is False: return [*data] #returns list
    return data[element] #returns element

  except json.decoder.JSONDecodeError: logging.warning (f"JSON File: {path} does not have any arguments. Skipping.")

# Changes .json file
def json_change(path, key, dest_value):
  temp_dict = json_read(path)
  temp_dict[key] = dest_value
  with open (path, 'w') as file: json.dump(temp_dict, file, indent=2)

# Changes .json file in more specific way
def json_change_adv(path, key, dest_value, change_type, float_round: int = None):
  temp_dict = json_read(path)
  match change_type:

    #math is intended to change int value (use negative value for 'math' to substract)
    case "math":
      if type(dest_value) == int:   temp_dict[key] = int(temp_dict[key]) + int(dest_value)
      if type(dest_value) == float: temp_dict[key] = float(temp_dict[key]) + float(dest_value)

    case "math*":
      if type(dest_value) == int:   temp_dict[key] = int(temp_dict[key]) * int(dest_value)
      if type(dest_value) == float: temp_dict[key] = float(temp_dict[key]) * float(dest_value)

    case "math/":
      if type(dest_value) == int:   temp_dict[key] = int(temp_dict[key]) / int(dest_value)
      if type(dest_value) == float: temp_dict[key] = float(temp_dict[key]) / float(dest_value)

    #var_add is intended to be dict; can be useful with version updaters especially
    case "var_add": temp_dict.update (dest_value)

    #var_add, but for deleting; change_value can be anything in this case
    case "var_del": temp_dict.remove (key)

  if float_round is not None: # used to shorten float
    temp_dict[key] = round(temp_dict[key], float_round)

  with open (path, 'w') as file: json.dump(temp_dict, file, indent=2)

#===============|===============================================================================================
# INS(ENSITIVE) | Ported over from old IoA. Variant of Json_Change function, automatically recognising type of
# OPERATOR      | value. From obvious reasons, more convenient for automating, having less broad use instead.
#---------------|
# According to old docs: useful for dicts with various types of variables, which needs to be looped.
#===============================================================================================================
def json_change_ins(path, key, dest_value, extended_math=False, floatr: int = None):
  if not extended_math:
    if type(dest_value) == int or type(dest_value) == float:
      json_change_adv(path, key, dest_value, "math", float_round=floatr)
    elif type(dest_value) == str or type(dest_value) == bool:
      json_change(path, key, dest_value)
  elif extended_math == "*": json_change_adv(path, key, dest_value, "math*")
  elif extended_math == "/": json_change_adv(path, key, dest_value, "math/")

#============|==================================================================================================
# SUBSYSTEMS | Smaller functions used for special purposes
#============|==================================================================================================
# Reads second key of .json file (used to call values of objects from ID)
def json_subread(path, element, subelement):
  subdata = json_read(path, element)[0]
  return subdata[subelement]
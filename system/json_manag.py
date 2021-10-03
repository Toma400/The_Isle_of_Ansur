def json_read(path, element):
  import json
  json_file = open(path, "r")
  print (json.load(json_file))
  print (type(json_file))

def json_change(path, element, change_type, change_value):
  #change type identifies whether you want to do replacement, maths or var addition
  #replacement - it simply makes value X become value Y
  #maths - it adds value X to value Y (3+4=7, str+str=strstr)
  #var addition - compatibility type, adds another variable with specified default value - possibly using within "save_system" type of thing, when element needs to be updated
  import json
  #json_file = open (path, "r")
  #^ function a bit obsolete, but can be used to non-save related things, such as objects with non-changeable directory (default worlds/Ansur elements, for example)
  #for [modded] worlds/X elements though, another loader can be necessary

def save_read(name, category, element):
  import json
  final_path = "saves/" + name + "/" + category + ".json"
  #element tells what type of variable is needed to be read

def save_change(name, category, element, change_type, change_value):
  #same as json_change, but with save_read principles
  #-> since json_change couldn't read /relative/ path for player, since it has no name argument (therefore you should create final_path manually everytime)
  save_read(name, category, element)
  #operate on save_read
  pass

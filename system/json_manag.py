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
import system.id_manag
import system.json_manag

def main_inv (name):
  path = "saves/" + name + "/in_use/inventory.json"
  items = system.json_manag.json_read(path, "inventory").keys()
  print ("✺---------------------------------------------------------------✺")
  j = 1
  for i in items:
    name = system.id_manag.iid_conv (i, "descript")
    print ("[" + str(j) + "][ " + name + " ]")
    j = j+1
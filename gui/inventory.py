import system.id_manag
import system.json_manag

def add_item (name, iid, modifier=False):
  #adds item, considering its amount and stackability
  if (system.id_manag.iid_conv(iid, "stackable")) == False:
    #item_data stores all "unstackable" properties (data_creator creates them)
    item_data = add_data (name, iid, modifier)
    final_item_data = {iid: item_data}
    system.json_manag.save_change(name, "inventory", "inventory", "var_add", final_item_data)
  else:
    #modifier here serves as amount counter 
    if type(modifier) == int:
      numb = modifier
    else:
      numb = 1
    item_data = inv_key_reader (name, iid, 0, "item_stackable_amount")
    final_item_data = {iid: item_data + numb}
    system.json_manag.save_change(name, "inventory", "inventory", "var_add", final_item_data)

def del_item (name, iid):
  if inv_key_reader (name, iid, 0, "if_item_exists") == True and inv_key_reader (name, iid, 0, "item_amount") > 1:
    pass
  else:
    #dict.remove ()
    pass

def add_data (name, iid, source=False):
  #creator of all properties, depending on skills
  pass

def inv_key_reader (name, iid, element, selector):
  path = "saves/" + name + "/in_use/inventory.json"
  #inventory of selected player
  main_dict = system.json_manag.json_read(path, "inventory")
  #list of items in that inventory
  key_dict = main_dict.keys()

  #SURFACE DATA (inventory manag, items themselves)

  #checker whether item exists or not
  if selector == "if_item_exists":
    found = 0
    for i in key_dict:
      if "^" in i:
        amount_splitter = i.split("^")
        i = amount_splitter[0]
      if i == iid:
        found = found + 1
      else:
        pass
    if found > 0:
      return True
    else:
      return False

  #returns number of items
  elif selector == "item_amount":
    found = []
    for i in key_dict:
      if i == iid or iid + "^" in i:
        found.append(i)
      else:
        pass
    return len(found)

  elif selector == "item_stackable_amount":
    if inv_key_reader (name, iid, 0, "if_item_exists") == True:
      return main_dict[iid]
    else:
      return 0

  #DEEPER DATA (item key-value)

  elif selector == "deep_inv":
    if inv_key_reader(name, iid, 0, "if_item_exists") == True:
      deep_dict = main_dict[iid]
      #dict of keys/values of specific item
      return deep_dict
    else:
      print ("Item called by function does not exist. Checker prevention action failed.")
  
  elif "slot" in selector:
    pass

  elif selector == "if_value_exists":
    temp_dict = inv_key_reader(name, iid, 0, "deep_inv")
    #list of keys (values) for item
    deep_key_dict = temp_dict.keys()
    found = 0
    for i in deep_key_dict:
      if i == iid:
        found = found + 1
      else:
        pass
    if found > 0:
      return True
    else:
      return False

  elif selector == "value":
    temp_dict = inv_key_reader(name, iid, 0, "deep_inv")
    #list of keys (values) for item
    deep_dict = temp_dict[iid]
    deep_key_dict = deep_dict.keys()
    return deep_dict[element]


def inv_key_creator (name, iid, element, selector):
  path = "saves/" + name + "/in_use/inventory.json"
  #inventory of selected player
  main_dict = system.json_manag.json_read(path, "inventory")
  #list of items in that inventory
  key_dict = main_dict.keys()
  #SURFACE/DEEPER DATA CREATOR (only basic data, primitive function)
  #uses "element" being "dict"
  if selector == "item_creator":
    temp_var = {iid: element}
    system.json_manag.save_change(name, "inventory", "inventory", "var_add", temp_var)









  #slot selector
  #key creator
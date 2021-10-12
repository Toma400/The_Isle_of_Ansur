import system.id_manag
import system.json_manag

def add_item (name, iid, modifier=False):
  #adds item, considering its amount and stackability
  if (system.id_manag.iid_conv(iid, "stackable")) == False:
    #item_data stores all "unstackable" properties
    item_data = add_data (name, iid, modifier)
    #item_data has to be dict with all properties (if none, then item data is just empty dict)
    if inv_key_reader (name, iid, 0, "if_item_exists"):
      iid = iid + "^" + str(inv_key_reader (name, iid, 0, "item_amount"))
      inv_key_creator (name, iid, 0, item_data, "item_change")
    else:
      inv_key_creator (name, iid, 0, item_data, "item_change")
  else:
    #modifier here serves as amount counter 
    if type(modifier) == int:
      numb = modifier
    else:
      numb = 1
    item_data = inv_key_reader (name, iid, 0, "item_stackable_amount")
    inv_key_creator (name, iid, 0, item_data + numb, "item_change")

def del_item (name, iid, modifier=False):
  #returns value to check if there's possibility to delete/decrease
  if inv_key_reader (name, iid, 0, "if_item_exists") == True:
    if (system.id_manag.iid_conv(iid, "stackable")) == False:
      if inv_key_reader (name, iid, 0, "item_amount") > 1:
        iid = iid + "^" + str(inv_key_reader (name, iid, 0, "item_amount") - 1)
        inv_key_creator (name, iid, 0, 0, "item_del")
      else:
        inv_key_creator (name, iid, 0, 0, "item_del")
    else:
      if type(modifier) == int:
        numb = modifier
      else:
        numb = 1
      item_data = inv_key_reader (name, iid, 0, "item_stackable_amount")
      if item_data - numb > -1:
        return True
        inv_key_creator (name, iid, 0, item_data - numb, "item_change")
      else:
        return False
  else:
    return False

def add_data (name, iid, source=False):
  #creator of all properties, depending on skills (for now only: quality)
  return {}

def inv_key_reader (name, iid, element, selector):
  path = "saves/" + name + "/in_use/inventory.json"
  #inventory of selected player
  main_dict = system.json_manag.json_read(path, "inventory")
  #list of items in that inventory
  key_dict = main_dict.keys()
  #========================================================
  #SURFACE DATA (inventory manag, items themselves)
  #--------------------------------------------------------
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
  #returns number of items for stackable items
  elif selector == "item_stackable_amount":
    if inv_key_reader (name, iid, 0, "if_item_exists") == True:
      return main_dict[iid]
    else:
      return 0
  #========================================================
  #DEEPER DATA (item key-value)
  #--------------------------------------------------------
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


def inv_key_creator (name, iid, element, value, selector, slot="inventory"):
  path = "saves/" + name + "/in_use/inventory.json"
  #inventory of selected player (all slots)
  main_dict = system.json_manag.json_read(path, 0, True)
  #list of items in that inventory
  #for i in main_dict:
    #globals()['_%s' % i] = main_dict[i]
  #key_dict = main_dict.keys()
  #SURFACE/DEEPER DATA CREATOR (only basic data, primitive function)
  #uses "element" being "dict"
  #if selector == "item_creator":
  #  temp_var = {iid: element}
  if selector == "item_change":
    if value != 0:
      temp_dict = {iid:value}
      main_dict[slot].update (temp_dict)
      system.json_manag.json_write(path, main_dict)
    else:
      inv_key_creator (name, iid, element, value, "item_del", slot)

  if selector == "item_del":
    temp_dict = main_dict[slot]
    del temp_dict[iid]
    main_dict[slot] = temp_dict
    system.json_manag.json_write(path, main_dict)

  if selector == "value_change":
    #can be used to change value, but also add new one
    change_point = main_dict[slot]
    change_set = {element:value}
    change_point[iid].update(change_set)
    main_dict[slot] = change_point
    system.json_manag.json_write(path, main_dict)








  #slot selector
  #key creator
  #del item
  #add data
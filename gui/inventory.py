import system.id_manag
import system.json_manag
from utils.text import text_align as align

#-----------------------------------------------------------------------------
# MAIN_INV
# Interface showing inventory items
#-----------------------------------------------------------------------------
def main_inv (name):
  path = "saves/" + name + "/in_use/inventory.json"
  items = system.json_manag.json_read(path, "inventory").keys()
  print("✺---------------------------------------------------------------✺")
  j = 1
  for i in items:
    item_name = system.id_manag.iid_conv (i, "descript")
    print ("[" + str(j) + "][ " + item_name + " ]")
    j = j+1
  print("✺---------------------------------------------------------------✺")
  # Here there will be actions which you will need to choose
  print("[U] [Use the item]\n[E] [Equip the item]\n[T] [Throw item away]\n[Q] [Go back]")
  print("✺---------------------------------------------------------------✺")
  print(align("{ use single letter to choose the action }", "centre"))
  print(align("{ use letter, dot and number to choose both action and item }", "centre"))
  print("✺---------------------------------------------------------------✺")
  choice = input ("").lower()
  if len(choice) > 1:
    # checks if user wrote input correctly
    if "." not in choice:
      print("Incorrect ID")
      main_inv(name)
    else:
      choice_list = choice.split(".") # splits by dot and sort into the list
      # then, checks if values are correct, and if so, redirects to function
      if choice_checker(name, choice_list[0], choice_list[1]) == True:
        action_selector_full(name, choice_list[0], choice_list[1])
  else:
    if choice_checker(name, choice) == True: # checks if value is correct
      action_selector_empty(name, choice)

#------------------------------------------------------------------------------
# ACTION SELECTORS
# These are inputs from player on which action they wish to do.
# If they type only action button, they will be redirected to panel with item
# selecting - if they type both action and slot, they will be redirected
# directly to action on that item.
#------------------------------------------------------------------------------
def action_selector_empty(name, action):
  print("✺---------------------------------------------------------------✺")
  print(align("{ select item by putting number of it }", "centre"))
  print("✺---------------------------------------------------------------✺")
  choice = input("")

def action_selector_full(name, action, slot):
  slot = int(slot)
  pass

#------------------------------------------------------------------------------
# TECHNICAL
#------------------------------------------------------------------------------
def choice_checker(name, action, slot=0):
  # checks if values are written correctly
  if action == "u" or action == "e" or action == "t" or action == "q":
    if int(slot):
      return True
    else:
      print(align("{ values are incorrect! }", "centre"))
      main_inv(name)
      return False
  else:
    print(align("{ values are incorrect! }", "centre"))
    main_inv(name)
    return False
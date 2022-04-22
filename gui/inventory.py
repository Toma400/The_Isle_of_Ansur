import gui.interface
import system.id_manag
import system.json_manag
import logging as log
from utils.text_manag import align

#-----------------------------------------------------------------------------
# MAIN_INV
# Interface showing inventory items
#-----------------------------------------------------------------------------
def main_inv (name):
  log.info("Opening inventory menu...")
  choice = "x"
  while choice != "q": # call stack killer: root
    path = f"saves/{name}/in_use/inventory.json"
    items = system.json_manag.json_read(path, "inventory").keys()
    print("✺---------------------------------------------------------------✺")
    inventory_items(items) # shows items from inventory being iterated here
    print("✺---------------------------------------------------------------✺")
    # here there will be actions which you will need to choose
    print("[U] [Use the item]\n[E] [Equip the item]\n[T] [Throw item away]\n[Q] [Go back]")
    print("✺---------------------------------------------------------------✺")
    print(align("{ use single letter to choose the action }"))
    print(align("{ use letter, dot and number to choose both action and item }"))
    print("✺---------------------------------------------------------------✺")
    choice = input ("").lower()
    if len(choice) > 1:
      # checks if user wrote input correctly
      if "." not in choice:
        print(align("{ incorrect selector used! }"))
        continue
      else:
        choice_list = choice.split(".")  # splits by dot and sort into the list
        # then, checks if values are correct, and if so, redirects to function
        if choice_checker(name, choice_list[0], choice_list[1]) == True:
          action_selector_full(name, choice_list[0], choice_list[1])
        else:
          print(align("{ values are incorrect! }"))
          continue
    else:
      if choice_checker(name, choice) == True:  # checks if value is correct
        action_selector_empty(name, choice)
      else:
        print(align("{ values are incorrect! }"))
        continue

#------------------------------------------------------------------------------
# ACTION SELECTORS
# These are inputs from player on which action they wish to do.
# If they type only action button, they will be redirected to panel with item
# selecting - if they type both action and slot, they will be redirected
# directly to action on that item.
#------------------------------------------------------------------------------
def action_selector_empty(name, action):
  while True: # call stack killer: root/inventory
    print("✺---------------------------------------------------------------✺")
    print(align("{ select item by putting number of it }"))
    print("✺---------------------------------------------------------------✺")
    try:
      item_choice = input("")
      if item_choice.lower() != "q":  # checks if user does not want to quit
        int(item_choice)
      else:
        break  # quits if user used 'q' key
    except ValueError:  # if item_choice is non-convertible-string
      print(align("{ values are incorrect! }"))
      continue

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
      return False
  else:
    return False

def inventory_items(items):
  j = 1
  for i in items:
    item_name = system.id_manag.iid_conv(i, "descript")
    print("[" + str(j) + "][ " + item_name + " ]")
    j = j + 1
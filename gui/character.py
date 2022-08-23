#-------------------------------------------------------------------------------------------------------------------
# CHARACTER.PY
# Character module is run only with new game initialisation, and it is generally character builder. It runs several
# functions which then save player profile, function-by-function appending new elements. It is the only one moment
# in game which doesn't care about call stack, implementing functions carelessly without closing the ones already
# running.
# All next game iterations are run from [load] initialisation, which skips that module.
#
# * breaks after functions are part of call stack killing, though they may be changed, since they - realistically -
#   never gonna happen (left for legacy reasons)
# * 'name' is the only continuously used variable throughout whole game, recognising the save profile and allowing
#   game to constantly communicate with saved profile
#-------------------------------------------------------------------------------------------------------------------
from system.ref_systems.stats_langkey import get_lkey as alstr
from system.ref_systems.default_stats import profile as defaults
from utils.text_manag import align
from utils.text_manag import colour_formatter as format
from utils.text_manag import quit_checker as quit
from utils.text_manag import langstring as lstr
from utils.text_manag import langjstring as jlstr
from system.id_manag import *

import system.json_manag as json_manag
import logging as log
import system.mod_manag

def name():
  log.info("Initialising character setup. Opening name selection...")
  import system.save_system.initialisation as init
  print (format("blue+", "--------------------"))
  print ("\n")
  print (align(lstr("game__init_charname")))
  print (align("---"))
  print (align(lstr("game__init_charname_rv")))
  print ("\n")
  while True:
    player_name = input ("")
    if quit(player_name, True, "0"):
      log.debug("Cancelling character setup. Coming back to menu.")
      return "0"  # return will be False
    else:
      if init.folder_creating(player_name) == False:
        log.debug("Failed to create player directory. Printing the reason:")
        # creates profile, if fails then loops back to start (usually because of already existing name of character)
        continue
      else:
        json_manag.save_change(player_name, "profile", "name", "replace", player_name)
        log.debug("Successfully created player directory. Moving to new character section.")
        break  # return will be player_name
  return player_name

def gender(name):
  log.info("Opening gender selection...")
  print (format("blue+", "--------------------"))
  print ("\n")
  print (align(lstr("game__init_gender1")))
  print (align(lstr("game__init_gender2")))
  print (align(lstr("game__init_gender3")))
  print (align(lstr("game__init_gender4")))
  print (align("---"))
  print ("\n")
  while True:
    gender = input ("")
    if quit(gender):
      log.debug("Cancelling character setup. Coming back to menu.")
      return False
    elif gender == "1" or gender == "2" or gender == "3":
      gender_name = ""
      if gender == "1":
        gender_name = "Male"
      elif gender == "2":
        gender_name = "Female"
      elif gender == "3":
        gender_name = "Non-binary"
      json_manag.save_change(name, "profile", "gender", "replace", gender_name)
      return True
    else:
      continue

def race(name):
  log.info("Opening race selection...")
  races_loaded = system.mod_manag.rid_loader()
  races_count = len(races_loaded)
  print (format("blue+", "--------------------"))
  print ("\n")
  print (align(lstr("game__init_race")))
  print ("\n")
  listing_races(races_loaded)  # prints out available races
  print ("\n")
  while True:
    choose_race = int_check(input(""))
    if not choose_race:
      continue
    if quit(choose_race):
      log.debug("Cancelling character setup. Coming back to menu.")
      return False
    elif 0 < choose_race <= races_count:
      chosen_race = races_loaded[choose_race-1]
      system.json_manag.save_change(name, "profile", "race", "replace", chosen_race)
      for i in rid_conv(chosen_race, 0, True):
        k = rid_conv(chosen_race, i)
        try:
          if i == "race_id" or i == "descript":
            pass
          else:
            system.json_manag.save_change_ins(name, "profile", i, k)
        except KeyError:
          #detector of values that can't be added
          print (f"Unknown value: {i}. Skipped.") #<- fStrings be difficult, let that be English here (GUI should make it disappear)
      return True
    else:
      continue

def profession(name):
  log.info("Opening class selection...")
  classes_loaded = system.mod_manag.cid_loader()
  classes_count = len(classes_loaded)
  print (format("blue+", "--------------------"))
  print ("\n")
  print (align(lstr("game__init_class")))
  print ("\n")
  listing_classes(classes_loaded)  # prints out available classes
  print ("\n")
  while True:
    choose_class = int_check(input(""))
    if not choose_class:
      continue
    if quit(choose_class):
      log.debug("Cancelling character setup. Coming back to menu.")
      return False
    elif 0 < choose_class <= classes_count:
      chosen_class = classes_loaded[choose_class-1]
      try:
        #checks
        if system.json_manag.save_read(name, "profile", "race") == cid_conv(chosen_class, "race_exclusive"):
          pass
        else:
          print (format("yellow", lstr("game__init_class_excl"))) #??????????????? this is reported to the police (GitHub tracker), such a dumb idea
          print ("\n")
          continue
      except KeyError:
        pass
      #runs if not interrupted by race_exclusivity
      system.json_manag.save_change(name, "profile", "class", "replace", chosen_class)
      for i in cid_conv(chosen_class, 0, True):
        k = cid_conv(chosen_class, i)
        try:
          if i == "class_id" or i == "descript" or i == "race_exclusive":
            pass
          else:
            system.json_manag.save_change_ins(name, "profile", i, k)
        except KeyError:
          #detector of values that can't be added
          print (f"Unknown value: {i}. Skipped.") #will leave it as it is, GUI will make it go
      return True
    else:
      continue

def manual_attribute(name):
  log.info("Opening manual attribute selection...")
  attribute_list = []
  for i in defaults.attributes:
    attribute_list.append (i)
  print (format("blue+", "--------------------"))
  print ("\n")
  print (align(lstr("game__init_attr")))
  print ("\n")
  listing_attributes(attribute_list)  # prints out attributes
  print ("\n")
  while True:
    try:
      choose_atr = int(input (""))
    except ValueError:
      continue
    if quit(choose_atr):
      log.debug("Cancelling character setup. Coming back to menu.")
      return False
    elif 0 < choose_atr <= len(attribute_list):
      choose_atr = attribute_list[choose_atr-1]
      choose_atr = str(choose_atr)
    else:
      continue
    system.json_manag.save_change(name, "profile", choose_atr, "math", 1)
    return True

def manual_ability(name):
  log.info("Opening manual ability selection...")
  import system.id_manag
  abilities = defaults.abilities
  ability_list = []
  for i in abilities:
    ability_list.append (i)
  print (format("blue+", "--------------------"))
  print ("\n")
  print (align(lstr("game__init_abil")))
  print ("\n")
  j = 1
  listing_abilities(ability_list)  # prints out abilities
  print ("\n")
  while True:
    try:
      choose_abil = int(input (""))
    except ValueError:
      continue
    if quit(choose_abil):
      log.debug("Cancelling character setup. Coming back to menu.")
      return False
    elif 0 < choose_abil <= len(ability_list):
      choose_abil = ability_list[choose_abil-1]
      choose_abil = str(choose_abil)
    else:
      continue  # previously it was calling of manual attribute, but this doesn't make sense here # <- WTF I meant here?
    system.json_manag.save_change(name, "profile", choose_abil, "math", 1)
    return True

#-------------------------------------------------------
# LIST PRINTING FUNCTIONS
# Put as separate functions just for improved code
# readibility above
#-------------------------------------------------------
def listing_races(races_loaded):
  j = 1
  for k in races_loaded:
    race_name = jlstr(rid_conv(k, "descript"), "stats", id_splitter(k, 0))
    print("[" + str(j) + "][" + race_name + "]")
    j = j + 1

def listing_classes(classes_loaded):
  j = 1
  for k in classes_loaded:
    class_name = jlstr(cid_conv(k, "descript"), "stats", id_splitter(k, 0))
    print("[" + str(j) + "][" + class_name + "]")
    j = j + 1

def listing_attributes(attribute_list):
  j = 1
  for i in attribute_list:
    atr_i = lstr(alstr(i))
    print ("[" + str(j) + "][" + atr_i + "]")
    j = j+1

def listing_abilities(skills_list):
  j = 1
  for i in skills_list:
    skl_i = lstr(alstr(i))
    print("[" + str(j) + "][" + skl_i + "]")
    j = j + 1

# checks if value is convertable into integer
def int_check (insert):
  try:
    return int(insert)
  except ValueError:
    return False
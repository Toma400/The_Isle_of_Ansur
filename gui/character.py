import system.json_manag
#player_name is the only continuously used variable throughout whole game, recognising the save profile
import utils.text.text_align as align
import utils.colours.bcolors as colour

def name():
  import system.save_system.initialisation
  print (align(colour.OKBLUE + "--------------------" + colour.ENDC, "centre_colour"))
  print ("\n")
  print (align("Type your character name", "centre"))
  print (align("---", "centre"))
  print (align("Type -0- to cancel", "centre"))
  print ("\n")
  while True:
    player_name = input ("")
    if player_name != "0":
      if system.save_system.initialisation.folder_creating(player_name) == False:
        #function creating profile, if it fails then loops back to start (usually because of already existing name of character)
        name()
        break
      else:
        system.json_manag.save_change(player_name, "profile", "name", "replace", player_name)
        gender (player_name)
        break
    else:
      break

def gender(name):
  print (align(colour.OKBLUE + "--------------------" + colour.ENDC, "centre_colour"))
  print ("\n")
  print (align("Choose your gender", "centre"))
  print (align("[1] Male", "centre"))
  print (align("[2] Female", "centre"))
  print (align("---", "centre"))
  print ("\n")
  while True:
    gender = input ("")
    if gender == "1" or gender == "2":
      gender_name = ""
      if gender == "1":
        gender_name = "Male"
      elif gender == "2":
        gender_name = "Female"
      system.json_manag.save_change(name, "profile", "gender", "replace", gender_name)
      race(name)
      break
    else:
      gender(name)

def race(name):
  import system.mod_manag
  import system.id_manag.rid_conv as rid_conv #garbage.py rule avoided
  import json
  races_loaded = system.mod_manag.rid_loader()
  races_count = len(races_loaded)
  print (align(colour.OKBLUE + "--------------------" + colour.ENDC, "centre_colour"))
  print ("\n")
  print (align("Choose your race", "centre"))
  print ("\n")
  j = 1
  for k in races_loaded:
    print ("[" + str(j) + "][" + rid_conv (k, "descript") + "]")
    j = j+1
  print ("\n")
  while True:
    choose_race = int(input (""))
    if choose_race > 0 and choose_race <= races_count:
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
          print ("Unknown value:" + i + ". Skipped.")
      classes(name)
      break
    else:
      race(name)

def classes(name):
  import system.mod_manag
  import system.id_manag.cid_conv as cid_conv #garbage.py rule avoided
  import json
  classes_loaded = system.mod_manag.cid_loader()
  classes_count = len(classes_loaded)
  print (align(colour.OKBLUE + "--------------------" + colour.ENDC, "centre_colour"))
  print ("\n")
  print (align("Choose your class", "centre"))
  print ("\n")
  j = 1
  for k in classes_loaded:
    print ("[" + str(j) + "][" + cid_conv (k, "descript") + "]")
    j = j+1
  print ("\n")
  while True:
    choose_class = int(input (""))
    if choose_class > 0 and choose_class <= classes_count:
      chosen_class = classes_loaded[choose_class-1]
      try:
        #checks
        if system.json_manag.save_read(name, "profile", "race") == cid_conv(chosen_class, "race_exclusive"):
          pass
        else:
          print ((align(colour.CYELLOW2 + "Class is exclusive for race you don't represent!" + colour.ENDC, "centre_colour")))
          print ("\n")
          classes(name)
          break
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
          print ("Unknown value:" + i + ". Skipped.")
      manual_attribute(name)
      break
    else:
      classes(name)

def manual_attribute(name):
  import system.mod_manag
  import system.id_manag
  import json
  import stats.default_stats
  attribute_list = []
  for i in stats.default_stats.profile.attributes:
    i = i.replace("atr_", "")
    i = i.title()
    attribute_list.append (i)
  print (align(colour.OKBLUE + "--------------------" + colour.ENDC, "centre_colour"))
  print ("\n")
  print (align("Choose attribute you want to enhance", "centre"))
  print ("\n")
  j = 1
  for i in attribute_list:
    print ("[" + str(j) + "][" + i + "]")
    j = j+1
  print ("\n")
  while True:
    choose_atr = int(input (""))
    if choose_atr > 0 and choose_atr <= len(attribute_list):
      choose_atr = attribute_list[choose_atr-1].lower()
      choose_atr = choose_atr.replace(" ", "_")
      choose_atr = ("atr_" + choose_atr)
      pass
    else:
      manual_attribute(name)
      break
    system.json_manag.save_change(name, "profile", choose_atr, "math", 1)
    manual_ability(name)
    break

def manual_ability(name):
  import system.mod_manag
  import system.id_manag
  import gui.interface
  import stats.default_stats.profile.abilities as abilities
  import json
  ability_list = []
  for i in abilities:
    i = i.replace("abil_", "")
    i = i.replace("_", " ")
    i = i.title()
    ability_list.append (i)
  print (align(colour.OKBLUE + "--------------------" + colour.ENDC, "centre_colour"))
  print ("\n")
  print (align("Choose ability you want to enhance", "centre"))
  print ("\n")
  j = 1
  for i in ability_list:
    print ("[" + str(j) + "][" + i + "]")
    j = j+1
  print ("\n")
  while True:
    choose_abil = int(input (""))
    if choose_abil > 0 and choose_abil <= len(ability_list):
      choose_abil = ability_list[choose_abil-1].lower()
      choose_abil = choose_abil.replace(" ", "_")
      choose_abil = ("abil_" + choose_abil)
      pass
    else:
      manual_attribute(name)
      break
    system.json_manag.save_change(name, "profile", choose_abil, "math", 1)
    gui.interface.main_game (name)
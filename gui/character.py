import system.json_manag
#player_name is the only continuously used variable throughout whole game, recognising the save profile

def name():
  import utils.text
  import utils.colours
  import system.save_system.initialisation
  print (utils.text.text_align(utils.colours.bcolors.OKBLUE + "--------------------" + utils.colours.bcolors.ENDC, "centre_colour"))
  print ("\n")
  print (utils.text.text_align("Type your character name", "centre"))
  print (utils.text.text_align("---", "centre"))
  print (utils.text.text_align("Type -0- to cancel", "centre"))
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
  import utils.text
  import utils.colours
  print (utils.text.text_align(utils.colours.bcolors.OKBLUE + "--------------------" + utils.colours.bcolors.ENDC, "centre_colour"))
  print ("\n")
  print (utils.text.text_align("Choose your gender", "centre"))
  print (utils.text.text_align("[1] Male", "centre"))
  print (utils.text.text_align("[2] Female", "centre"))
  print (utils.text.text_align("---", "centre"))
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
  import utils.text
  import utils.colours
  import system.mod_manag
  import system.id_manag
  import json
  races_loaded = system.mod_manag.rid_loader()
  races_count = len(races_loaded)
  print (utils.text.text_align(utils.colours.bcolors.OKBLUE + "--------------------" + utils.colours.bcolors.ENDC, "centre_colour"))
  print ("\n")
  print (utils.text.text_align("Choose your race", "centre"))
  print ("\n")
  j = 1
  for k in races_loaded:
    print ("[" + str(j) + "][" + system.id_manag.rid_conv (k, "descript") + "]")
    j = j+1
  while True:
    choose_race = int(input (""))
    if choose_race > 0 and choose_race <= races_count:
      chosen_race = races_loaded[choose_race-1]
      system.json_manag.save_change(name, "profile", "race", "replace", chosen_race)
      classes(name)
      break
    else:
      race(name)

def classes(name):
  pass
from utils.colours import bcolors as colour
from utils.colours import text_align as align
from utils.colours import colour_formatter as format
from system.settings import version_call as version_call

import gui.character
import system.mod_manag as sys

def start():
  version_call("game_version")
  while True:
    print ('''\n\n|__) _|_    _ _ _   (_ |_  _  _| _     _   _  _  _|  |  . _ |_ |_ 
|__)(-|_\)/(-(-| )  __)| )(_|(_|(_)\)/_)  (_|| )(_|  |__|(_)| )|_ 
                                                         _/  
''')
    print ("𝚃𝚑𝚎 𝙸𝚜𝚕𝚎 𝚘𝚏 𝙰𝚗𝚜𝚞𝚛\n")
    print (align(version_call("game_version") + "\n\n", "right"))
    is_core_pack_loaded()
    print (align("--------------------", "centre"))
    print (align("[1] START THE GAME", "centre"))
    print (align("[2] LOAD THE GAME", "centre"))
    print (align("[3] SETTINGS", "centre"))
    print (align("[4] PACKS", "centre"))
    print (align("[5] EXIT THE GAME", "centre"))
    print ("\n\n")
    menu_choice = input ("")
    if menu_choice == "1":
      if is_core_pack_loaded():
        gui.character.name()
    elif menu_choice == "2":
      if is_core_pack_loaded():
        game_load()
    elif menu_choice == "3":
      settings()
    elif menu_choice == "4":
      if is_core_pack_loaded():
        packs()
    elif menu_choice == "5" or "q":
      break

def game_load():
  import utils.repo_manag as repo_manag
  import system.json_manag as json_manag
  import system.id_manag as id_manag
  loaded_profiles = repo_manag.dir_checker ("saves/", "dir")
  for i in loaded_profiles:
    openability = json_manag.save_read(i, "profile", "openable")
    if openability == False:
      loaded_profiles.remove(i)
  loaded_profiles.sort()
  profile_set = {}
  j = 1
  print ("\n")
  print (align("--------------------", "centre"))
  print (align("Choose your save", "centre"))
  print (align("[use numbers or precise name]", "centre"))
  print ("\n")
  for i in loaded_profiles:
    if repo_manag.empty_checker("saves/" + i + "/in_use/profile.json") == False:
      race = id_manag.rid_conv(json_manag.save_read(i, "profile", "race"), "descript")
      classe = id_manag.cid_conv(json_manag.save_read(i, "profile", "class"), "descript")
      locate = json_manag.save_read(i, "profile", "location")
      print (align("[ " + colour.OKCYAN + i + colour.ENDC + " ][" + race + " - " + classe + "][ " + colour.OKCYAN + locate + colour.ENDC + " ]", "centre_colour"))
      profile_set[str(j)] = i
      j = j + 1
    else:
      pass
  print ("\n")
  print (align("--------------------", "centre"))
  print (align("[use any non-assigned button to go back to menu]", "centre"))
  print (align("[use slash '/' before name to delete profile]", "centre"))
  print ("\n")
  temp_var = input ("")
  if "/" in temp_var: #deleting save
    import time
    path = ("saves/" + temp_var.replace("/", ""))
    try:
      temp_var2 = repo_manag.dir_checker (path, "dir")
      repo_manag.file_deleting (path)
      print (align("--------------------", "centre"))
      print (align("Profile successfully deleted!", "centre"))
      print (align("--------------------", "centre"))
      time.sleep(2)
      game_load()
    except FileNotFoundError:
      import system.save_system.save_load
      system.save_system.save_load.deep_load_error("name")
  else:
    #finds out whether player inputted number or name
    try:
      just_testing = int(temp_var)
      name = profile_set[temp_var]
    except ValueError:
      name = temp_var
    #checks if: game is in permadeath and if: game was saved before
    if json_manag.save_read(name, "profile", "openable"):
      import system.save_system.save_load
      if name in repo_manag.dir_checker ("saves/", "dir"):
        if repo_manag.empty_checker("saves/" + name + "/profile.json") == False:
          system.save_system.save_load.deep_load (name)
        else:
          special_load(name)
      else:
        system.save_system.save_load.deep_load_error("name")
    else:
      print ("\n")
      print (align("--------------------", "centre"))
      print (align("You died in that save while having Permanent Death enabled", "centre"))
      print (align("--------------------", "centre"))
      print ("\n")
      game_load()

def special_load(name):
  import system.save_system.save_load
  #special load for game that wasn't saved before exiting the game, but loaded
  #it simply saves "temp" files and tries to load them to avoid error from empty .jsons
  print (align("--------------------", "centre"))
  print (align("Save file wasn't saved before. Saving from in-game data.", "centre"))
  print (align("--------------------", "centre"))
  system.save_system.save_load.full_save (name)
  system.save_system.save_load.deep_load (name)

def settings():
  import system.settings
  import system.json_manag
  while True:
    print ("\n")
    print (align("--------------------", "centre"))
    print (align("Select setting to switch.", "centre"))
    print (align("--------------------", "centre"))
    setting_options = ["Time System", "Hunger/Thirst", "Permanent Death"]
    setting_set = {}
    j = 1
    for i in setting_options:
      i2 = i.replace("nent D", "d") #permadeath
      i2 = i2.lower().replace(" ", "_")
      i2 = i2.replace("/", "_")
      y = system.json_manag.json_read("system/system_settings.json", i2)
      print (align("[" + str(j) + "][" + i + "][ " + colour.OKCYAN + str(y).capitalize() + colour.ENDC + " ]", "centre_colour"))
      setting_set[str(j)] = i2
      j = j + 1
    print ("\n")
    print (align("--------------------", "centre"))
    print (align("[use any non-numerical button to go back to menu]", "centre"))
    print ("\n")
    temp_var = input ("")
    try:
      system.settings.settings_changer(setting_set[temp_var])
      continue
    except KeyError:
      break

#---------------------------------------------------------
# PACKS
# List all packs available, sorted by their type
#---------------------------------------------------------
def packs():
  print("\n")
  while True:
    packs_loaded = []
    print(align("-----------------------------------------------------------", "centre"))
    print(align(" PACKS LOADED ", "centre"))
    print(align("⊱⋅-----------------------------------------⋅⊰", "centre"))
    for pack_type in pack_type_helper():
      packgroup_opened = pack_loader(pack_type)
      if packgroup_opened:  # checks if specific packgroup list is not empty
        for pack_name in packgroup_opened:
          packs_loaded.append(pack_name)
          print(align("[ " + pack_colour(pack_type) + " ] [ " + pack_name + " ]", "centre_colour"))
          ## ^ add here some info about pack being disabled or enabled soon
    print(align("-----------------------------------------------------------", "centre"))
    print(align(" Enter name of pack to open its settings ", "centre"))
    print(align(" Press -q- to leave the menu ", "centre"))
    print(align("-----------------------------------------------------------", "centre"))
    keybind = input("").lower()
    if keybind == "q":
      break
    else:
      pack_settings_checker(keybind, packs_loaded)

def pack_settings(pack_name):
  from system.mod_manag import mod_reader as p_read
  print("\n")
  while True:
    print(align("-----------------------------------------------------------", "centre"))
    print(format("violet", p_read(pack_name, "name")))  # mod name
    print(align("Pack ID: " + pack_name, "centre"))
    print(align("⊱⋅---------------------------------⋅⊰", "centre"))
    ## HERE PUT PACK TYPE, INFO ABOUT BEING ENABLED OR DISABLED
    print(format("blue", p_read(pack_name, "description"), "left"))  # mod description
    print(align("-----------------------------------------------------------", "centre"))
    print(format("cyan", "URL: " + p_read(pack_name, "link")))  # link assigned
    print(format("green", "Credits: " + p_read(pack_name, "credits")))  # mod credits
    print(align("-----------------------------------------------------------", "centre"))
    break

#---------------------------------------------------------
# SYSTEM FUNCTIONS
# Functions used for some system-related behaviours
#---------------------------------------------------------
def is_core_pack_loaded():
  # checks whether ansur globalpack is loaded
  core_checker = sys.mod_checker("both", "ansur")
  if not core_checker:
    print(align(colour.CRED + "Core files are not loaded! Restricted menu options." + colour.ENDC, "centre_colour"))
    return False
  else:
    return True

def pack_loader(request):
  # returns list of all correctly sorted modded packs depending on requested type
  globalpacks_loaded = sys.mod_lister("both", "modded")
  if request == "globalpack":
    return sys.mod_lister("both", "modded")
  if request == "statpack":
    return [x for x in sys.mod_lister("stats", "modded") if x not in globalpacks_loaded]  # loads statpacks-only packs
  if request == "worldpack":
    return [x for x in sys.mod_lister("worlds", "modded") if x not in globalpacks_loaded]  # loads worldpacks-only packs

def pack_settings_checker(pack_name, pack_list):
  # checks if pack name entered is listed inside available packs
  while True:
    if pack_name in pack_list:
      pack_settings(pack_name)
      break
    else:
      print(format("red", "Pack with this name does not exist!"))
      break

#---------------------------------------------------------
# UNSPAGHETTIERS
# Used for making code a bit cleaner
#---------------------------------------------------------
def pack_type_helper(number=None):
  pack_types = [
    "globalpack",
    "worldpack",
    "statpack"
  ]
  if number == None:
    return pack_types
  else:
    return pack_types[number]

def pack_colour(type):
  if type == "globalpack":
    return colour.OKBLUE + pack_type_helper()[0] + colour.ENDC
  elif type == "worldpack":
    return colour.CVIOLET2 + pack_type_helper()[1] + colour.ENDC
  elif type == "statpack":
    return colour.CGREEN + pack_type_helper()[2] + colour.ENDC
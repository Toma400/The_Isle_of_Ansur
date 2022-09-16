from utils.text_manag import bcolors as colour
from utils.text_manag import align
from utils.text_manag import colour_formatter as format
from utils.text_manag import encoded as enc
from utils.text_manag import langstring as lstr
from system.settings import settings as settings_check
from system.log_manag import run_text as logtxt
from core.system_ref import SysRef

import gui.character
import gui.interface
import system.mod_manag as sys
import logging as log
import shutil
import os
gpath = os.path.dirname(os.path.abspath("main.py"))

def start():
  log.info(logtxt())
  log.info("Initialising start menu...")
  if not settings_check("legacy_unpacking"):
    log.info("Autoupdating of packs enabled. Importing...")
    pack_remover()
    pack_unloader()
  while True:
    log.info("Menu successfully loaded. Printing elements.")
    first_game = False
    print ('''\n\n|__) _|_    _ _ _   (_ |_  _  _| _     _   _  _  _|  |  . _ |_ |_ 
|__)(-|_\)/(-(-| )  __)| )(_|(_|(_)\)/_)  (_|| )(_|  |__|(_)| )|_ 
                                                         _/  
''')
    print (enc(f"{SysRef.name}\n"))
    print (align(f"{SysRef.status} {SysRef.version}" + "\n\n", "right"))
    is_core_pack_loaded()
    print (align("--------------------", "centre"))
    print (align(lstr("menu__button_start"), "centre"))
    print (align(lstr("menu__button_load"), "centre"))
    print (align(lstr("menu__button_settings"), "centre"))
    print (align(lstr("menu__button_packs"), "centre"))
    print (align(lstr("menu__button_exit"), "centre"))
    print ("\n\n")
    menu_choice = input ("")
    if menu_choice == "1":
      if is_core_pack_loaded():
        name = gui.character.name()
        if name != "0":
          if gui.character.gender(name):
            if gui.character.race(name):
              if gui.character.profession(name):
                if gui.character.manual_attribute(name):
                  if gui.character.manual_skill(name):
                    first_game = True
        if first_game:
          print ("Yay! Game would start if this wasn't unfinished version!") # run the game
        # else:
          # [here there was import of utils.repo_manag.file_deleting]
          # delete("saves/" + name) <- it doesn't work, because for some reason file
          # is created *after* closing the game, not during function running
          # continue  # <- possibly unnecessary code, loop will rerun anyway
          # + folder creation time aside, it needs to use name of the player, so just
          # remember that (ik its foolish to remind that obviousness)
    elif menu_choice == "2":
      if is_core_pack_loaded():
        game_load()
    elif menu_choice == "3":
      settings()
    elif menu_choice == "4":
      if is_core_pack_loaded():
        packs()
    elif menu_choice == "5" or menu_choice == "q":
      break
    if first_game:  # run only if menu_choice is run and all character creation steps are done
      gui.interface.main_game(name)  # dw about warning, it is strictly conditioned to happen

def game_load():
  import utils.repo_manag as repo_manag
  import system.json_manag as json_manag
  import system.id_manag as id_manag
  import utils.text_manag as text_manag
  import system.save_system.save_load
  log.debug("Game loading menu opened. Loading profiles.")

  while True:
    loaded_profiles = repo_manag.dir_checker ("saves/", "dir")
    for i in loaded_profiles:
      openability = json_manag.save_read(i, "profile", "openable")
      if openability == False:
        loaded_profiles.remove(i)
    loaded_profiles.sort()
    profile_set = {}
    j = 1
    print ("\n")
    print (align("--------------------"))
    print (align(lstr("menu__load_choose")))
    print (align(lstr("menu__load_choose_hint")))
    print ("\n")
    for i in loaded_profiles:
      if repo_manag.empty_checker(f"saves/{i}/in_use/profile.json") == False:
        race = id_manag.rid_conv(json_manag.save_read(i, "profile", "race"), "descript")
        classe = id_manag.cid_conv(json_manag.save_read(i, "profile", "class"), "descript")
        locate = json_manag.save_read(i, "profile", "location")
        print (align(f"[ {colour.OKCYAN}{i}{colour.ENDC} ][{race} - {classe}][ {colour.OKCYAN}{locate}{colour.ENDC} ]", "centre_colour")) #should be translated, ewh
        profile_set[str(j)] = i
        j = j + 1
      else:
        pass
    print ("\n")
    print (align("--------------------"))
    print (align(lstr("menu__load_action1")))
    print (align(lstr("menu__load_action2")))
    print ("\n")
    temp_var = input ("")
    if "/" in temp_var:  # deleting save
      log.debug("Deleting initialised. Proceeding.")
      import time
      path = ("saves/" + temp_var.replace("/", ""))
      try:
        temp_var2 = repo_manag.dir_checker (path, "dir")
        repo_manag.file_deleting (path)
        print (align("--------------------"))
        print (align(lstr("menu__load_save_deleted")))
        print (align("--------------------"))
        time.sleep(2)
        log.info("Deleting successful!")
        continue
      except FileNotFoundError:
        system.save_system.save_load.deep_load_error("name")  # recursiveness, call stack killer needed + redirects to main menu weirdly
        log.debug("File not found. Deleting of save cancelled.")
    elif text_manag.quit_checker(temp_var):
      break
    else:
      log.debug("Loading of save initialised. Proceeding.")
      #finds out whether player inputted number or name
      try:
        just_testing = int(temp_var)
        name = profile_set[temp_var]
      except ValueError:
        name = temp_var
      #checks if: game is in permadeath and if: game was saved before
      if json_manag.save_read(name, "profile", "openable"):  # totally unefficient and done wrongly, dir_checker should be first to work as descript says
        if name in repo_manag.dir_checker ("saves/", "dir"):  # because hierarchy here will either say about permadeath or raise error if you write blabber
          if repo_manag.empty_checker("saves/" + name + "/profile.json") == False:
            system.save_system.save_load.deep_load (name)
            log.debug("Loading save data and opening the save...")
          else:
            special_load(name)
        else:
          system.save_system.save_load.deep_load_error("name")
      else:
        log.info("Loaded save with permadeath settings enabled. Unfortunately you died and can't go back :<")
        print ("\n")
        print (align("--------------------"))
        print (align("You died in that save while having Permanent Death enabled"))
        print (align("--------------------"))
        print ("\n")

def special_load(name):
  import system.save_system.save_load
  #special load for game that wasn't saved before exiting the game, but loaded
  #it simply saves "temp" files and tries to load them to avoid error from empty .jsons
  log.debug("Loaded save was quitted before manual save. Thankfully we got you covered! Reading automatical saves and writing them to main save...")
  print (align("--------------------"))
  print (align(lstr("menu__load_save_unsaved")))
  print (align("--------------------"))
  system.save_system.save_load.full_save (name)
  system.save_system.save_load.deep_load (name)
  log.debug("Loading save data and opening the save...")

#---------------------------------------------------------------------------------------------
# SETTINGS
# Function allowing user to switch their settings to desired ones. Takes values from
# `settings_options` list, formats them into .json keys and check their values
#---------------------------------------------------------------------------------------------
def settings():
  import system.settings
  import system.json_manag
  log.debug("Opening game settings!")
  while True:
    print ("\n")
    print (align("--------------------"))
    print (align(lstr("menu__settings_choose")))
    print (align("--------------------"))
    setting_options = ["Time System", "Hunger/Thirst", "Permanent Death", "Legacy Unpacking"] #should be translated, ewh
    setting_set = {}
    j = 1
    for i in setting_options:
      i2 = i.replace("nent D", "d") #permadeath
      i2 = i2.lower().replace(" ", "_")
      i2 = i2.replace("/", "_")
      y = system.json_manag.json_read("settings.json", i2)
      print (align("[" + str(j) + "][" + i + "][ " + colour.OKCYAN + str(y).capitalize() + colour.ENDC + " ]", "centre_colour"))
      setting_set[str(j)] = i2
      j = j + 1
    print ("\n")
    print (align("--------------------"))
    print (align(lstr("menu__settings_action")))
    print ("\n")
    temp_var = input ("")
    try:
      system.settings.settings_changer(setting_set[temp_var])
      continue
    except KeyError:
      break

#---------------------------------------------------------------------------------------------
# PACKS
# List all packs available, sorted by their type, also
# operations possible on them (blacklisting, unzipping)
#---------------------------------------------------------------------------------------------
def packs():
  log.debug("Opening packloader! Printing the contents...")
  from system.mod_manag import mod_blacklister as blacklisted
  print("\n")
  while True:
    packs_loaded = []
    print(align("-----------------------------------------------------------"))
    print(align(lstr("pack__general_info")))
    print(enc(align("*-----------------------------------------*")))
    for pack_type in pack_type_helper():
      packgroup_opened = pack_loader(pack_type)
      if packgroup_opened:  # checks if specific packgroup list is not empty
        for pack_name in packgroup_opened:
          packs_loaded.append(pack_name)
          log.debug("Successfully loaded pack: " + pack_name)
          if blacklisted(pack_name, True):
            print(align(f"[ {pack_colour(pack_type)} ] [ {colour.CRED}{pack_name}{colour.ENDC} ] ", "centre_colour+")) #check later if needs to be translated
          else:
            print(align(f"[ {pack_colour(pack_type)} ] [ {pack_name} ]", "centre_colour"))
    print(align("-----------------------------------------------------------"))
    print(align(lstr("pack__actions_opt1")))
    print(align(lstr("pack__actions_opt2")))
    print(align(lstr("pack__actions_opt3")))
    print(align("-----------------------------------------------------------"))
    keybind = input("").lower()
    if keybind == "q" or keybind == "quit" or keybind == "":
      break
    if keybind == "unzip":
      pack_unloader()
      continue
    else:
      pack_settings_checker(keybind, packs_loaded)

#----------------------------------------------------
# PACK SETTINGS
# Shows info.json and makes a way to disable the pack
#----------------------------------------------------
def pack_settings(pack_name):
  from system.mod_manag import mod_reader as p_read
  from system.mod_manag import mod_blacklister as blacklisted
  import webbrowser
  lister_vals = [
    lstr("pack__lister_id"),
    lstr("pack__lister_type"),
    lstr("pack__lister_credits")
  ]
  mod_name = p_read(pack_name, "name")
  print("\n")
  while True:
    print(align("-----------------------------------------------------------"))
    print(format("violet", mod_name))  # mod name
    print(align(f"{lister_vals[0]}: {pack_name}"))
    print(align("⊱⋅---------------------------------⋅⊰"))
    if blacklisted(pack_name, True):  # shows up only if blacklisted
      print(format("red", lstr("pack__lister_disabled")))
    print(align(f"{lister_vals[1]}: {pack_type_recogniser(pack_name)}"))
    print(enc(align("*---------------------------------*")))
    print(format("blue", p_read(pack_name, "description"), "left"))  # mod description
    print(align("-----------------------------------------------------------"))
    print(format("cyan", f"URL: {mod_name}", "link"))  # link assigned
    print(format("green", f"{lister_vals[2]}: {mod_name}", "credits"))  # mod credits
    print(align("-----------------------------------------------------------"))
    print(lstr("pack__lister_action1"))
    print(lstr("pack__lister_action2"))
    print(lstr("pack__lister_action3"))
    print(align("-----------------------------------------------------------"))
    keyword = input("").lower()
    if keyword == "link":  # opens website in browser
      webbrowser.open(p_read(pack_name, "link"))
    if keyword == "switch":  # switches mod from being enabled to disabled and reversely
      from system.mod_manag import mod_blacklister as blacklister
      blacklister(pack_name)
      continue
    if keyword == "q" or keyword == "quit" or keyword == "":
      break
    else:
      continue

#----------------------------------------------------
# PACK UNLOADER
# Allows unzipping mods from /pack/ dir and updating
#----------------------------------------------------
def pack_remover():
  non_removable_keys = SysRef.vanilla_modules
  stats_rv = os.listdir(f"{gpath}/stats/"); worlds_rv = os.listdir(f"{gpath}/worlds/")
  scripts_rv = os.listdir(f"{gpath}/scripts/")
  def rv(t, tc):
    if os.path.isdir(t) and tc not in non_removable_keys:
      shutil.rmtree(t)

  for i in stats_rv:
    rv(f"{gpath}/stats/{i}", i)
  for i in worlds_rv:
    rv(f"{gpath}/worlds/{i}", i)
  for i in scripts_rv:
    rv(f"{gpath}/scripts/{i}", i)

def pack_unloader():
  log.info("Pack unloading requested.")
  import os, zipfile
  packs_in_dir = os.listdir("packs/")
  for pack in packs_in_dir:
    if ".zip" in pack:  # make sure file has correct extension
      with zipfile.ZipFile("packs/" + pack, "r") as file:
        pack_unloader_checker(file, pack)
        file.close()

def pack_unloader_checker(file, pack):
  for i in file.namelist():
    if "stats/" in i:
      file.extract(i, "")
      log.debug("Unpacking of statpack: " + pack)
    if "worlds/" in i:
      file.extract(i, "")
      log.debug("Unpacking of worldpack: " + pack)

#---------------------------------------------------------------------------------------------
# SYSTEM FUNCTIONS
# Functions used for some system-related behaviours
#---------------------------------------------------------------------------------------------
def is_core_pack_loaded():
  # checks whether ansur globalpack is loaded
  core_checker = sys.mod_checker("both", "ansur")
  if not core_checker:
    print(format("red", lstr("menu__warn_core_missing")))
    log.warning("Core files are not loaded! Restricting menu options.")
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
      print(format("red", lstr("pack__error_not_exist")))
      break

#---------------------------------------------------------------------------------------------
# UNSPAGHETTIERS
# Used for making code a bit cleaner
#---------------------------------------------------------------------------------------------
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

def pack_type_recogniser(pack_name):
  if pack_name in pack_loader("globalpack"):
    return pack_colour("globalpack")
  elif pack_name in pack_loader("statpack"):
    return pack_colour("statpack")
  elif pack_name in pack_loader("worldpack"):
    return pack_colour("worldpack")
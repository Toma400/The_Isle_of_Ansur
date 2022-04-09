from utils import colours as colour
from utils.text import text_align as align
import gui.character
from system.settings import version_call as version_call

def start():
  version_call("game_version")
  while True:
    print ('''\n\n|__) _|_    _ _ _   (_ |_  _  _| _     _   _  _  _|  |  . _ |_ |_ 
|__)(-|_\)/(-(-| )  __)| )(_|(_|(_)\)/_)  (_|| )(_|  |__|(_)| )|_ 
                                                         _/  
''')
    print ("𝚃𝚑𝚎 𝙸𝚜𝚕𝚎 𝚘𝚏 𝙰𝚗𝚜𝚞𝚛\n")
    print (align(version_call("game_version") + "\n\n", "right"))
    print (align("--------------------", "centre"))
    print (align("[1] START THE GAME", "centre"))
    print (align("[2] LOAD THE GAME", "centre"))
    print (align("[3] ENCYCLOPAEDIA", "centre"))
    print (align("[4] GAME SETTINGS", "centre"))
    print (align("[5] EXIT THE GAME", "centre"))
    print ("\n\n")
    menu_choice = input ("")
    if menu_choice == "1":
      gui.character.name()
    elif menu_choice == "2":
      game_load()
    elif menu_choice == "3":
      continue #encyclopaedia removed, should go into "save managment" to remove saves w/o entering folders
    elif menu_choice == "4":
      settings()
    elif menu_choice == "5" or "q":
      break
    else:
      continue

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
    settings()
  except KeyError:
    start()
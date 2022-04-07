from utils import colours as colour
from utils.text import text_align as align

def start():
  import gui.character
  import system.settings.version_call as version_call
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
      break
    elif menu_choice == "3":
      encyclopaedia()
      break
    elif menu_choice == "4":
      settings()
      break
    elif menu_choice == "5":
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

def encyclopaedia():
  elements = ["CHARACTER CREATION", "ELSE"]
  print ("\n")
  print (align("--------------------", "centre"))
  #straight style, url: https://patorjk.com/software/taag/
  print ('''                 __                             
                |_  _  _   _| _  _  _  _ _|. _  
                |__| )(_\/(_|(_)|_)(_|(-(_||(_| 
                        /       |               ''')
  print (align("THE KEEPER OF KNOWLEDGE", "centre"))
  print ("\n")
  for i in range (len(elements)):
    #assigning available spaces
    if i == 1:
      assigned_var = align(colour.CRED + "[" + str(i+1) + "] " + elements[i] + colour.ENDC, "centre_colour")
    else:
      assigned_var = align("[" + str(i+1) + "] " + elements[i], "centre")
    print (assigned_var)
  print ("\n\n")
  gate = input ("")
  encyclopaedia_pages (gate)

def encyclopaedia_pages (paged):
  if paged == "1":
    elements = {"RACES":'''Races are main factor of your character once you create it - in longer run they are not as deciding (but it differs, sometimes they can), but on initial part of the game, abilities, perks and characteristics of race can guide you into totally different playstyles. It can also help you to focus on specific direction, so you don't need to grind through all needed things to become what you want to.\nThere are a lot of races and subraces in Baedoor world, each of them living in their specific area. In The Isle of Ansur you will have possibility to see some of them, at least for alpha stage of the game. In the future more can be added. Races in The Isle of Ansur are:\n[1] Human - being quite regular race with subtle bonuses to various attributes. Good if you prefer balanced gameplay. Baedoorian is more technical-oriented, while Westernwaldian is more magic-oriented.\n[2] Tri - elven-like creatures, being probably oldest civilisations of Baedoor universe. Have several subraces, such as voitri - the dark ones, and saphtri - desert tris. They all prefer to use swords and magic, but while voitri uses rather demonic powers, saphtri exchange them for mechanical bows and weird technical systems.\n[3] Ormath - inhabitants of Great Desert of Arennan. They are pacifistic living beings, wandering with their nomadic villages built on-the-fly. Usually they know the spirit of winds and sand more than anyone in whole universe could ever know. It's a bit extreme race, but it is also the only one bound so much to connection power.\n[4] Ett - dwarven-like race, one of the ancient races involved in times when noone even wrote any historical chronicles. They are said as a keepers of oldest technologies and are probably the most talented on these - despite baedoorians being more advanced in modern technology.\n[5] Ghlodds - another old civilisation of weirdly mutated beings. Their civilisation is heavily bound to both mystical and technological side of universe, therefore making them great unbalanced choice for anyone who wants merge these both sides. Usually a bit aggressive, which was the reason of their past glory in older eras.''',"CLASSES":'''Classes are secondary factors, making the character shape on skill side. Their names are usually self explanatory, so I won't get you through them all, but it's needed to point out that these are not as important as race itself. They can still help you with progressing further with your playstyle, especially if combined with race and your custom points assigned to skills.'''}
    print ("\n")
    print (align("--------------------", "centre"))
    for k, v in elements.items():
      print ("\n")
      print (align("[" + k + "]", "centre"))
      print (v)
      print ("\n\n")
      temp_input = input (align("»", "centre"))
    encyclopaedia()
  else:
    start()
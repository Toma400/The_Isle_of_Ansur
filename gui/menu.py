import utils.colours
import utils.text

def start():
  import gui.character
  import system.settings
  system.settings.version_call("game_version")
  while True:
    print ('''\n\n|__) _|_    _ _ _   (_ |_  _  _| _     _   _  _  _|  |  . _ |_ |_ 
|__)(-|_\)/(-(-| )  __)| )(_|(_|(_)\)/_)  (_|| )(_|  |__|(_)| )|_ 
                                                         _/  
''')
    print ("𝚃𝚑𝚎 𝙸𝚜𝚕𝚎 𝚘𝚏 𝙰𝚗𝚜𝚞𝚛\n")
    print (utils.text.text_align(system.settings.version_call("game_version") + "\n\n", "right"))
    print (utils.text.text_align("--------------------", "centre"))
    print (utils.text.text_align("[1] START THE GAME", "centre"))
    print (utils.text.text_align("[2] LOAD THE GAME", "centre"))
    print (utils.text.text_align("[3] ENCYCLOPAEDIA", "centre"))
    print (utils.text.text_align("[4] GAME SETTINGS", "centre"))
    print (utils.text.text_align("[5] EXIT THE GAME", "centre"))
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
  import utils.repo_manag
  import system.json_manag
  import system.id_manag
  import system.save_system.save_load
  loaded_profiles = utils.repo_manag.dir_checker ("saves/", "dir")
  loaded_profiles.sort()
  profile_set = {}
  j = 1
  print ("\n")
  print (utils.text.text_align("--------------------", "centre"))
  print (utils.text.text_align("Choose your save", "centre"))
  print (utils.text.text_align("[use numbers or precise name]", "centre"))
  print ("\n")
  for i in loaded_profiles:
    if utils.repo_manag.empty_checker("saves/" + i + "/in_use/profile.json") == False:
      race = system.id_manag.rid_conv(system.json_manag.save_read(i, "profile", "race"), "descript")
      classe = system.id_manag.cid_conv(system.json_manag.save_read(i, "profile", "class"), "descript")
      locate = system.json_manag.save_read(i, "profile", "location")
      print (utils.text.text_align("[ " + utils.colours.bcolors.OKCYAN + i + utils.colours.bcolors.ENDC + " ][" + race + " - " + classe + "][ " + utils.colours.bcolors.OKCYAN + locate + utils.colours.bcolors.ENDC + " ]", "centre_colour"))
      profile_set[str(j)] = i
      j = j + 1
    else:
      pass
  print ("\n")
  print (utils.text.text_align("--------------------", "centre"))
  print (utils.text.text_align("[use any non-assigned button to go back to menu]", "centre"))
  print (utils.text.text_align("[use slash '/' before name to delete profile]", "centre"))
  print ("\n")
  temp_var = input ("")
  if "/" in temp_var: #deleting save
    import utils.repo_manag
    import time
    path = ("saves/" + temp_var.replace("/", ""))
    try:
      temp_var2 = utils.repo_manag.dir_checker (path, "dir")
      utils.repo_manag.file_deleting (path)
      print (utils.text.text_align("--------------------", "centre"))
      print (utils.text.text_align("Profile successfully deleted!", "centre"))
      print (utils.text.text_align("--------------------", "centre"))
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
    #checks if game was saved before
    if name in utils.repo_manag.dir_checker ("saves/", "dir"):
      if utils.repo_manag.empty_checker("saves/" + name + "/profile.json") == False:
        system.save_system.save_load.deep_load (name)
      else:
        special_load(name)
    else:
      system.save_system.save_load.deep_load_error("name")
      

def special_load(name):
  import system.save_system.save_load
  #special load for game that wasn't saved before exiting the game, but loaded
  #it simply saves "temp" files and tries to load them to avoid error from empty .jsons
  print (utils.text.text_align("--------------------", "centre"))
  print (utils.text.text_align("Save file wasn't saved before. Saving from in-game data.", "centre"))
  print (utils.text.text_align("--------------------", "centre"))
  system.save_system.save_load.full_save (name)
  system.save_system.save_load.deep_load (name)

def settings():
  import system.settings
  import system.json_manag
  print ("\n")
  print (utils.text.text_align("--------------------", "centre"))
  print (utils.text.text_align("Select setting to switch.", "centre"))
  print (utils.text.text_align("--------------------", "centre"))
  setting_options = ["Time System", "Hunger/Thirst", "Permanent Death"]
  setting_set = {}
  j = 1
  for i in setting_options:
    i2 = i.replace("nent D", "d") #permadeath
    i2 = i2.lower().replace(" ", "_")
    i2 = i2.replace("/", "_")
    y = system.json_manag.json_read("system/system_settings.json", i2)
    print (utils.text.text_align("[" + str(j) + "][" + i + "][ " + utils.colours.bcolors.OKCYAN + str(y).capitalize() + utils.colours.bcolors.ENDC + " ]", "centre_colour"))
    setting_set[str(j)] = i2
    j = j + 1
  print ("\n")
  print (utils.text.text_align("--------------------", "centre"))
  print (utils.text.text_align("[use any non-numerical button to go back to menu]", "centre"))
  print ("\n")
  temp_var = input ("")
  try:
    system.settings.settings_changer(setting_set[temp_var])
    settings()
  except KeyError:
    start()

def encyclopaedia():
  import utils.colours
  elements = ["CHARACTER CREATION", "ELSE"]
  print ("\n")
  print (utils.text.text_align("--------------------", "centre"))
  #straight style, url: https://patorjk.com/software/taag/
  print ('''                 __                             
                |_  _  _   _| _  _  _  _ _|. _  
                |__| )(_\/(_|(_)|_)(_|(-(_||(_| 
                        /       |               ''')
  print (utils.text.text_align("THE KEEPER OF KNOWLEDGE", "centre"))
  print ("\n")
  for i in range (len(elements)):
    #assigning available spaces
    if i == 1:
      assigned_var = utils.text.text_align(utils.colours.bcolors.CRED + "[" + str(i+1) + "] " + elements[i] + utils.colours.bcolors.ENDC, "centre_colour")
    else:
      assigned_var = utils.text.text_align("[" + str(i+1) + "] " + elements[i], "centre")
    print (assigned_var)
  print ("\n\n")
  gate = input ("")
  encyclopaedia_pages (gate)

def encyclopaedia_pages (paged):
  import utils.text
  if paged == "1":
    import utils.colours
    elements = {"RACES":'''Races are main factor of your character once you create it - in longer run they are not as deciding (but it differs, sometimes they can), but on initial part of the game, abilities, perks and characteristics of race can guide you into totally different playstyles. It can also help you to focus on specific direction, so you don't need to grind through all needed things to become what you want to.\nThere are a lot of races and subraces in Baedoor world, each of them living in their specific area. In The Isle of Ansur you will have possibility to see some of them, at least for alpha stage of the game. In the future more can be added. Races in The Isle of Ansur are:\n[1] Human - being quite regular race with subtle bonuses to various attributes. Good if you prefer balanced gameplay. Baedoorian is more technical-oriented, while Westernwaldian is more magic-oriented.\n[2] Tri - elven-like creatures, being probably oldest civilisations of Baedoor universe. Have several subraces, such as voitri - the dark ones, and saphtri - desert tris. They all prefer to use swords and magic, but while voitri uses rather demonic powers, saphtri exchange them for mechanical bows and weird technical systems.\n[3] Ormath - inhabitants of Great Desert of Arennan. They are pacifistic living beings, wandering with their nomadic villages built on-the-fly. Usually they know the spirit of winds and sand more than anyone in whole universe could ever know. It's a bit extreme race, but it is also the only one bound so much to connection power.\n[4] Ett - dwarven-like race, one of the ancient races involved in times when noone even wrote any historical chronicles. They are said as a keepers of oldest technologies and are probably the most talented on these - despite baedoorians being more advanced in modern technology.\n[5] Ghlodds - another old civilisation of weirdly mutated beings. Their civilisation is heavily bound to both mystical and technological side of universe, therefore making them great unbalanced choice for anyone who wants merge these both sides. Usually a bit aggressive, which was the reason of their past glory in older eras.''',"CLASSES":'''Classes are secondary factors, making the character shape on skill side. Their names are usually self explanatory, so I won't get you through them all, but it's needed to point out that these are not as important as race itself. They can still help you with progressing further with your playstyle, especially if combined with race and your custom points assigned to skills.'''}
    print ("\n")
    print (utils.text.text_align("--------------------", "centre"))
    for k, v in elements.items():
      print ("\n")
      print (utils.text.text_align("[" + k + "]", "centre"))
      print (v)
      print ("\n\n")
      temp_input = input (utils.text.text_align("»", "centre"))
    encyclopaedia()
  else:
    start()
import utils.colours
import utils.text

def start():
  import gui.character
  while True:
    print ('''\n\n|__) _|_    _ _ _   (_ |_  _  _| _     _   _  _  _|  |  . _ |_ |_ 
|__)(-|_\)/(-(-| )  __)| )(_|(_|(_)\)/_)  (_|| )(_|  |__|(_)| )|_ 
                                                         _/  
''')
    print ("𝚃𝚑𝚎 𝙸𝚜𝚕𝚎 𝚘𝚏 𝙰𝚗𝚜𝚞𝚛\n")
    print (utils.text.text_align("alpha 0.0.1b\n\n", "right"))
    print (utils.text.text_align("--------------------", "centre"))
    print (utils.text.text_align("[1] START THE GAME", "centre"))
    print (utils.text.text_align(utils.colours.bcolors.CRED + "[2] LOAD THE GAME" + utils.colours.bcolors.ENDC, "centre_colour"))
    print (utils.text.text_align("[3] ENCYCLOPAEDIA", "centre"))
    print (utils.text.text_align(utils.colours.bcolors.CRED + "[4] GAME SETTINGS" + utils.colours.bcolors.ENDC, "centre_colour"))
    print (utils.text.text_align("[5] EXIT THE GAME", "centre"))
    print ("\n\n")
    menu_choice = input ("")
    if menu_choice == "1":
      gui.character.name()
    elif menu_choice == "2":
      print ("Option unavailable")
      break
    elif menu_choice == "3":
      encyclopaedia()
      break
    elif menu_choice == "4":
      print ("Option unavailable")
      break
    elif menu_choice == "5":
      break
    else:
      continue

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
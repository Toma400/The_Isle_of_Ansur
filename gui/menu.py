import utils.colours
import utils.text

def start():
  while True:
    print ('''\n\n|__) _|_    _ _ _   (_ |_  _  _| _     _   _  _  _|  |  . _ |_ |_ 
|__)(-|_\)/(-(-| )  __)| )(_|(_|(_)\)/_)  (_|| )(_|  |__|(_)| )|_ 
                                                         _/  
''')
    print ("𝚃𝚑𝚎 𝙸𝚜𝚕𝚎 𝚘𝚏 𝙰𝚗𝚜𝚞𝚛\n")
    print (utils.text.text_align("alpha 0.0.1\n\n", "right"))
    #align all bottom part to center
    print (utils.text.text_align("--------------------", "centre"))
    print (utils.text.text_align("[1] START THE GAME", "centre"))
    print (utils.text.text_align("[2] LOAD THE GAME", "centre"))
    print (utils.text.text_align("[3] ENCYCLOPAEDIA", "centre"))
    print (utils.text.text_align("[4] EXIT THE GAME", "centre"))
    print ("\n\n")
    menu_choice = input ("")
    if menu_choice == "1":
      print ("Option unavailable")
      break
    elif menu_choice == "2":
      print ("Option unavailable")
      break
    elif menu_choice == "3":
      encyclopaedia()
      break
    elif menu_choice == "4":
      break
    else:
      continue

def encyclopaedia():
  elements = ["CHARACTER CREATION", "OFF", "OFF"]
  print ("\n")
  print (utils.text.text_align("--------------------", "centre"))
  print (utils.text.text_align("THE KEEPER OF KNOWLEDGE", "centre"))
  print ("\n")
  for i in range (len(elements)):
    print (utils.text.text_align("[" + str(i+1) + "] " + elements[i], "centre"))
  gate_1 = input ("")
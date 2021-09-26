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
    print ("--------------------")
    print ("[1] START THE GAME")
    print ("[2] LOAD THE GAME")
    print ("[3] ENCYCLOPAEDIA")
    print ("[4] EXIT THE GAME\n\n")
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
  print ("THE KEEPER OF KNOWLEDGE")
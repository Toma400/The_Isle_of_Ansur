def name():
  import utils.text
  import utils.colours
  import system.save_system
  print (utils.text.text_align(utils.colours.bcolors.OKBLUE + "--------------------" + utils.colours.bcolors.ENDC, "centre_colour"))
  print ("\n")
  print (utils.text.text_align("Type your character name", "centre"))
  while True:
    player_name = input ("")
    if system.save_system.folder_creating(player_name) == False:
      pass
    else:
      break
      #theoretically, it should be another step in character creation here
      #but "break" can be useful just in case loop will continue
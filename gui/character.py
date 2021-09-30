def name():
  import utils.text
  import utils.colours
  import system.save_system
  print (utils.text.text_align(utils.colours.bcolors.OKBLUE + "--------------------" + utils.colours.bcolors.ENDC, "centre_colour"))
  print ("\n")
  print (utils.text.text_align("Type your character name", "centre"))
  print (utils.text.text_align("---", "centre"))
  print (utils.text.text_align("Type -0- to cancel", "centre"))
  print ("\n")
  while True:
    player_name = input ("")
    if system.save_system.folder_creating(player_name) == False:
      name()
      break
    else:
      #actually that part should already export 'player_name' to 'in_use' profile.json
      #and gender should have no arguments, since no need is necessary
      gender (player_name)
      break

def gender(name):
  print (name)
def name():
  import utils.text
  import utils.colours
  import system.save_system.initialisation
  print (utils.text.text_align(utils.colours.bcolors.OKBLUE + "--------------------" + utils.colours.bcolors.ENDC, "centre_colour"))
  print ("\n")
  print (utils.text.text_align("Type your character name", "centre"))
  print (utils.text.text_align("---", "centre"))
  print (utils.text.text_align("Type -0- to cancel", "centre"))
  print ("\n")
  while True:
    player_name = input ("")
    if system.save_system.initialisation.folder_creating(player_name) == False:
      name()
      break
    else:
      save (name, player_name)
      gender (player_name)
      #pushing player_name further is used for folder recognition
      break

def gender(name):
  print (name)

def save(data_type, value):
  #temporary function to mark out where data should be saved
  #data_type is for variable name
  #each save should have thread to be marked as "todo"
  #also, save will obviously need "player_name" to mark out the destined folder, as already seen in json_manag.py file (/system)
  print (value)
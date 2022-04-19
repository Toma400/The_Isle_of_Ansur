import playsound
import os
import random
import logging

#------------------------------------------------------------
# SOUND MANAGMENT
# Module used to control sounds being played during the game
#
# Splits the sounds by being core or pack-related. Core ones
# are related to general elements, like menu sounds.
# Pack-related (non-core) sounds are related to locations.
#------------------------------------------------------------

def play_specific(name, path):
    # used to play specific sound
    pass

def play_loc(location, pack_id):
    # used to play randomly selected location sound
    path = "worlds/" + pack_id + "/locations/" + location + "/sounds/"
    soundlist = os.listdir(path)
    # <- here we will have appending element for location settings
    if soundlist:
        r = random.randint(0, len(soundlist) - 1)
        playsound(path + soundlist[r])
    else:
        logging.warning("Not found any files in: <" + path + ">. Skipping.")

def play_core(core_element):
    # used to play randomly selected core sound
    path = "utils/sounds/" + core_element + "/"
    soundlist = os.listdir(path)
    if soundlist:
        r = random.randint(0, len(soundlist) - 1)
        playsound(path + soundlist[r])
    else:
        logging.warning("Not found any files in: <" + path + ">. Skipping.")

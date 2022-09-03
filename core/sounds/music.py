from core.sounds.sd_system import bg_music
from core.utils import sndv
from pygame.mixer import *

def music_handler(music_playing, guitype):

    if not get_busy(): # checks if music ended

        match guitype:

            case "menu":
                music_playing = Sound(bg_music()); music_playing.set_volume(sndv/100)
                music_playing.play(fade_ms=2000)

    else: # for situations when sound should be interrupted
        pass

    return music_playing
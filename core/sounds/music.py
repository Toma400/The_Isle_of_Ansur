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
        pass # this point here should cut off music, not set new one -> because if music is cut off, it can easily
    # redirect program to ^ if not get_busy() and select new one there - avoiding some issues of infinite looping and so on, if we would
    # like to play new music in `else` (losing biggest trigger being 'is music playing')
    # here we just can use events which can interrupt the music constantly playing, such as 'battle starts', 'battle ends', 'location music incompat'

    return music_playing
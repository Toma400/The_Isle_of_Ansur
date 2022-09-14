from core.sounds.sd_system import bg_music
from pygame.mixer import *
from core.utils import *

def music_handler(music_playing, guitype, fg_events):

    if not get_busy(): # checks if music ended

        match guitype[0]:

            case "menu":
                music_playing = Sound(bg_music()); music_playing.set_volume(scx("sndv")/100)
                music_playing.play(fade_ms=2000)
                return music_playing

    else: # for situations when sound should be interrupted
        if "SNDV_CHG" in fg_events: # controls updates of sound volume
            music_playing.set_volume(scx("sndv")/100); fg_events.remove("SNDV_CHG")

    # this point here should cut off music, not set new one -> because if music is cut off, it can easily
    # redirect program to ^ if not get_busy() and select new one there - avoiding some issues of infinite looping and so on, if we would
    # like to play new music in `else` (losing biggest trigger being 'is music playing')
    # here we just can use events which can interrupt the music constantly playing, such as 'battle starts', 'battle ends', 'location music incompat'
    return music_playing
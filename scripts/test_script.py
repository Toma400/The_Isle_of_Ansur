from core.scripts import ioaScript
from core.graphics.text_manag import put_rectext
#=======================================
# Script has to import ioaScript class ^
# and use it for parenting V
#=======================================
class TestScript(ioaScript):

    event = "MENU" # name of the event when script should be run

    #====================================================================
    # run() function is where IoA will search for code when event is run
    #-----------------------------
    # Arguments for run() can be:
    #-----------------------------
    # *args - put it always if you do not use all of elements below:
    #---
    # screen - if you want to interfere with screen
    # pg_events - if you want to use PyGame events
    #====================================================================
    def run(self, screen, *args, **kwargs):
        stringed = '''
        I want to test something, if text can fit the screen correctly! Let's say, I have ambitions to write really long paragraph here!@* Like really, why should I care about space?
        '''
        put_rectext(screen, stringed, "menu", 5, 70, 25, 95, req_size=20)
        #put_rectext(screen, stringed, "menu", 55, 70, 95, 95)

    #====================================================================
    # You need to create __init__() function and make it return super()
    def __init__(self):
        super().__init__()
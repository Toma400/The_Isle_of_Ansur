from core.scripts import ioaScript
#=======================================
# Script has to import ioaScript class ^
# and use it for parenting V
#=======================================
class ExampleScript(ioaScript):

    event = "EVENT_NAME" # name of the event when script should be run

    #====================================================================
    # run() function is where IoA will search for code when event is run
    #-----------------------------
    # Arguments for run() can be:
    #-----------------------------
    # *args - put it always if you do not use all of elements below:
    #---
    # screen    - if you want to interfere with screen
    # pg_events - if you want to use PyGame events
    #====================================================================
    def run(self, *args, **kwargs):
        pass # here you write your code

    #====================================================================
    # You need to create __init__() function and make it return super()
    def __init__(self):
        super().__init__()
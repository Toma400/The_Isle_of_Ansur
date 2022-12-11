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
    # *args - put it always, even if arguments below are used:
    #---
    # screen    - if you want to interfere with screen
    # pg_events - if you want to use PyGame events
    # fg_events - if you want to access IoA events
    # fg_core   - if you want to access IoA running Screen object
    #====================================================================
    def run(self, *args, **kwargs):
        pass # here you write your code

    #====================================================================
    # You need to create __init__() function and make it return super()
    def __init__(self):
        super().__init__()
from core.graphics.lb_manag import ListBox, ListBoxPattern
from core.graphics.gh_manag import Image, NestedImage

class GUI_Helper:
    """ [ GUI HELPER ]
    Class dedicated to store all text and graphical objects of the game, to be initialised during start of the game (as dyn_screen).
    You can access those by running 'dyn_screen.gui(-string-)', where -string- should be stored as variable in here.

    You can still initialise those objects in the loop (via direct input in scripts), but outsourcing is recommended format,
    being way less resource-heavy (as objects do not reinitialise every second).
    This may not be important for simple, single elements (images, text), but can be "be or not to be" for more advanced features
    (such as listboxes or multilined text).

    Naming conventions:
    gh | graphics, image
    tx | text
    """

    def __init__(self):
        # MENU
        self.menu__gh_logo       = Image(path="core/assets/visuals/", file="logo.png",            pos=(10, 3, 90, 19))
        self.menu__gh_background = Image(path="core/assets/visuals/", file="menu_background.jpg", pos=(0, 0))

        self.menu__gh_testpt     = ListBoxPattern(NestedImage("core/assets/visuals/", "skill_1.jpg", (0, 0, 100, 100)))
        self.menu__gh_test       = ListBox((10, 10, 30, 50), pattern=self.menu__gh_testpt)

    def get_element(self, element: str):
        return self.__getattribute__(element)

    def restart(self):
        self.__init__()
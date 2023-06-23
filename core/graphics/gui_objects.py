from core.file_system.theme_manag import bg_handler
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

    def __init__(self, panorama):
        # MENU
        self.menu__gh_logo       = Image(path=bg_handler("logo", True)[0], file=bg_handler("logo", True)[1], pos=(10, 1, 90, 22))
        self.menu__gh_background = Image(path=bg_handler("menu", True)[0], file=bg_handler("menu", True)[1], pos=(0, 0))
        self.menu__gh_panorama   = Image(path=panorama[0],                 file=panorama[1],                 pos=(0, 0)).full()

        # self.alvb                = NestedImage("core/assets/visuals/", "dunaj.jpg", (0, 0, 100, 100)) # probably temporary, as everything below (listbox testing)
        # self.alvn                = NestedImage("core/assets/visuals/", "denaj.png", (0, 0, 100, 100))
        # self.menu__gh_testpt     = ListBoxPattern(NestedImage("core/assets/visuals/", "skill_1.jpg", (0, 0, 100, 100)))
        # self.menu__gh_test       = ListBox((10, 10, 30, 50), pattern=self.menu__gh_testpt).decor(bgdeco=self.alvb,
        #                                                                                          sgdeco=self.alvn)

    def get_element(self, element: str):
        return self.__getattribute__(element)

    def restart(self, panorama):
        self.__init__(panorama)
from core.graphics.gh_manag import Image

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

    # MENU
    menu__gh_logo       = Image(path="core/assets/visuals/", file="logo.png",            pos=(10, 3, 90, 19))
    menu__gh_background = Image(path="core/assets/visuals/", file="menu_background.jpg", pos=(0, 0))

    @classmethod
    def get_element(cls, element: str):
        return cls.__getattribute__(cls, element)
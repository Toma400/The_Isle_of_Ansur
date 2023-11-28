from core.file_system.theme_manag import bg_handler
from core.graphics.gh_manag import Image, ratioCell
from core.gui.elements.ttooltip import TTooltip
from core.gui.manag.langstr import langstring
from core.gui.manag.pc import toPxX, toPxY

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
        self.menu__gh_logo       = Image(path=bg_handler("logo", True)[0],     file=bg_handler("logo", True)[1],     pos=(10, 1, 90, 22))
        self.menu__gh_background = Image(path=bg_handler("menu", True)[0],     file=bg_handler("menu", True)[1],     pos=(0, 0))
        self.menu__gh_panorama   = Image(path=panorama[0],                     file=panorama[1],                     pos=(0, 0)).full()
        # ---
        self.loc__gh_background  = Image(path=bg_handler("location", True)[0], file=bg_handler("location", True)[1], pos=(0, 0)).full()
        # Tooltips (Settings):
        self.menu__tp_sett_res   = TTooltip(langstring("menu__sett_tooltip_res"),     text_size=20, pos=(toPxX(80), toPxY(16)))
        self.menu__tp_sett_lang  = TTooltip(langstring("menu__sett_tooltip_lang"),    text_size=20, pos=(toPxX(80), toPxY(24)))
        self.menu__tp_sett_music = TTooltip(langstring("menu__sett_tooltip_music"),   text_size=20, pos=(toPxX(80), toPxY(32)))
        self.menu__tp_sett_legu  = TTooltip(langstring("menu__sett_tooltip_legacy"),  text_size=20, pos=(toPxX(80), toPxY(16)))
        self.menu__tp_sett_loglm = TTooltip(langstring("menu__sett_tooltip_log_lm"),  text_size=20, pos=(toPxX(80), toPxY(24)))
        self.menu__tp_sett_logrv = TTooltip(langstring("menu__sett_tooltip_log_rv"),  text_size=20, pos=(toPxX(80), toPxY(32)))
        self.menu__tp_sett_lbox  = TTooltip(langstring("menu__sett_tooltip_listbox"), text_size=20, pos=(toPxX(80), toPxY(40)))
        self.menu__tp_sett_lb_am = TTooltip(langstring("menu__sett_tooltip_lb_am"),   text_size=20, pos=(toPxX(80), toPxY(48)))
        self.menu__tp_sett_lb_sz = TTooltip(langstring("menu__sett_tooltip_lb_size"), text_size=20, pos=(toPxX(80), toPxY(56)))
        self.menu__tp_sett_tx_sz = TTooltip(langstring("menu__sett_tooltip_tx_size"), text_size=20, pos=(toPxX(80), toPxY(64)))
        self.menu__tp_sett_vernf = TTooltip(langstring("menu__sett_tooltip_ver_nf"),  text_size=20, pos=(toPxX(80), toPxY(72)))
        self.menu__tp_sett_tltp  = TTooltip(langstring("menu__sett_tooltip_tooltip"), text_size=20, pos=(toPxX(80), toPxY(80)))
        # Tooltips (MMM):
        self.menu__tp_load_load  = TTooltip(langstring("load__error"),          text_size=20, pos=(toPxX(91), toPxY(14)))
        self.menu__tp_pack_db    = TTooltip(langstring("pack__tooltip_switch"), text_size=20, pos=(toPxX(90), toPxY(14)))
        self.menu__tp_pack_mvu   = TTooltip(langstring("pack__tooltip_mvu"),    text_size=20, pos=(toPxX(90), toPxY(19)))
        self.menu__tp_pack_mvd   = TTooltip(langstring("pack__tooltip_mvd"),    text_size=20, pos=(toPxX(90), toPxY(25)))
        # Tooltips (Character creation):
        self.ccrt__tp_name       = TTooltip(langstring("ccrt__tooltip_name"),        text_size=20, pos=(toPxX(84), toPxY(16)))
        self.ccrt__tp_av_lib     = TTooltip(langstring("ccrt__tooltip_av_lib"),      text_size=20, pos=(toPxX(84), toPxY(49)))
        self.ccrt__tp_av_url     = TTooltip(langstring("ccrt__tooltip_av_url"),      text_size=20, pos=(toPxX(84), toPxY(59)))
        self.ccrt__tp_av_dir     = TTooltip(langstring("ccrt__tooltip_av_dir"),      text_size=20, pos=(toPxX(84), toPxY(69)))
        self.ccrt__tp_pdeath     = TTooltip(langstring("ccrt__sett_hardcore_descr"), text_size=20, pos=(toPxX(30), toPxY(14)))
        self.ccrt__tp_save       = TTooltip(langstring("ccrt__end_save_warn"),       text_size=20, pos=(toPxX(58), toPxY(69)))

    def get_element(self, element: str):
        """Returns specific field/attribute given its string"""
        return self.__getattribute__(element)

    def get_elements(self) -> [str]:
        """Returns list of fields/attributes of the class"""
        return self.__dict__.keys()

    def draw(self, element: str, screen, pos: (int, int) = None):
        """Performs drawing on supporting elements (TTooltip at the time of writing this)"""
        match self.get_element(element).__module__:
            case TTooltip.__module__: self.get_element(element).draw(screen, pos)

    def restart(self, panorama):
        """Restarts whole initialisation process of the class"""
        self.__init__(panorama)
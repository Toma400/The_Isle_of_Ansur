from core.graphics.gh_manag import returnCell
from pygame.freetype import Font as FFont
from pygame.font import Font
from core.utils import *

def put_text (screen, text, font_cat, size, pos_x, pos_y, colour=None, bg_colour=None):
    if colour is None: colour = (0, 0, 0) # default text colour is black
    pos_x = returnCell(pos_x, "x")
    pos_y = returnCell(pos_y, "y")
    font = font_handler(category=font_cat)
    # 'size' is not cell-related because this would restrict precision
    #======================================
    fontobj = Font(f"{gpath}/core/assets/fonts/{font}", size)
    txtobj = fontobj.render(text, True, colour, bg_colour)
    screen.blit(txtobj, (pos_x, pos_y))

# FREETYPE TWEAKING
def put_ftext (screen, text, font_cat, size, pos_x, pos_y, colour=None, bg_colour=None):
    if colour is None: colour = (0, 0, 0) # default text colour is black
    pos_x = returnCell(pos_x, "x")
    pos_y = returnCell(pos_y, "y")
    font = font_handler(category=font_cat)
    # 'size' is not cell-related because this would restrict precision
    #======================================
    fontobj = FFont(f"{gpath}/core/assets/fonts/{font}", size, ucs4=True)
    txtobj = fontobj.render(text, True, colour, bg_colour)
    screen.blit(txtobj, (pos_x, pos_y))

def put_loretext(lang):
    pass # placeholder function for lore text, which will not be translateable through langkeys, but
    # refer to specific Baedoor fonts, such as ghloddish (or, later, trish and so on); font will
    # be automatically used based on language

#==========|========================================================
# FONT     | Decides on font used depending on category and language
# HANDLER  | You can pass font manually (use category=None then)
#==========|========================================================
def font_handler (category: str, font=None):
    match category:
        case "menu":
            if lang == "polish": font = "credit_valley.ttf"
            else:                font = "ferrum.otf"
    return font

#==========|========================================================
# LANGKEYS | Main part of langkey
#==========|========================================================
# Used to align text to specific part of the console
# Takes a bit different values if used with colours
#===================================================================
def langstring (key: str):
    import toml; t = toml.load(f"{gpath}/core/lang/{lang}.toml")
    return t[key]

def langjstring (key: str, modtype: str, modid: str = "ansur"):
    try:
        read = json_read(f"{modtype}/{modid}/lang.json", lang)
    except KeyError:
        try:
            read = json_read(f"{modtype}/{modid}/lang.json", "english")
        except KeyError:
            log.warning(f"Module {modid} does not have properly set language value for {key}. Please contact the developer of this module for help.")
            return langstring("system__text_load_fail")
    return read[key]
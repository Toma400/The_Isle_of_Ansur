from core.graphics.gh_manag import returnCell
from pygame.font import Font
from core.utils import *
#==========|========================================================
# TEXT     | Allows to blit text on the screen
# PUTTERS  |
#==========|========================================================
# Text renderer using scaling and alignment
def put_text (screen, text, font_cat, size, pos_x=0, pos_y=0, align_x=None, align_y=None, colour=None, bg_colour=None, endpos_x=None, endpos_y=None):
    if colour is None: colour = (0, 0, 0) # default text colour is black
    font = font_handler(category=font_cat)
    #======================================
    fontobj = Font(f"{gpath}/core/assets/fonts/{font}", size)
    fontobjs = fontobj.size(text) # tuple of rendered text size
    pos_x, pos_y = text_replacer(
        fontobjs,
        align_x=align_x,    # <- tells type of alignment of X axis
        align_y=align_y,    # <- tells type of alignment of Y axis
        x_pos=pos_x,        # <- tells cell alignment of X axis | if 'align_x' is not "center", should be filled
        y_pos=pos_y,        # <- tells cell alignment of Y axis | if 'align_y' is not "center", should be filled
        #------------------------------------------------------------------------------------------------------------------
        x_endpos=endpos_x,  # <- fill ONLY if you want precise placement (x, y, ex, ey), else use only values above
        y_endpos=endpos_y   #    this serves as alternative for alignment and determine ending points of a text surface
    )
    txtobj = fontobj.render(text, True, colour, bg_colour)
    screen.blit(txtobj, (pos_x, pos_y))
    return pos_x, pos_y, pos_x+fontobjs[0], pos_y+fontobjs[1] # returns starting and ending position in (x, y, x2, y2) manner

# Simple text renderer, without scaling, using absolute cell positions instead
def put_abstext (screen, text, font_cat, size, pos_x, pos_y, colour=None, bg_colour=None):
    if colour is None: colour = (0, 0, 0) # default text colour is black
    pos_x = returnCell(pos_x, "x")
    pos_y = returnCell(pos_y, "y")
    font = font_handler(category=font_cat)
    # 'size' is not cell-related because this would restrict precision
    #======================================
    fontobj = Font(f"{gpath}/core/assets/fonts/{font}", size)
    txtobj = fontobj.render(text, True, colour, bg_colour)
    screen.blit(txtobj, (pos_x, pos_y))

def put_lore(lang):
    pass # placeholder function for lore text, which will not be translateable through langkeys, but
    # refer to specific Baedoor fonts, such as ghloddish (or, later, trish and so on); font will
    # be automatically used based on language

#==========|========================================================
# FONT     | Decides on font used depending on category and language
# HANDLER  | You can pass font manually (use category=None then)
#==========|========================================================
# Fonts change because not all fonts support specific alphabets
def font_handler (category: str, font=None):
    match category:
        case "menu":
            if lang == "polish": font = "ferrum.otf" #TO FIX
            else:                font = "ferrum.otf"
    return font

# Sets position of text depending on its render size and cell position/alignment set
def text_replacer (text_size, align_x=None, align_y=None, x_pos=0, y_pos=0, x_endpos=None, y_endpos=None):
    match align_x:
        case "center": pos_x = returnCell(100, "x")/2 - text_size[0]/2
        case "right":  pos_x = returnCell(100, "x") - text_size[0] - returnCell(x_pos, "x")
        case other:    pos_x = returnCell(x_pos, "x")
    match align_y:
        case "center": pos_y = returnCell(100, "y")/2 - text_size[1]/2
        case "down":   pos_y = returnCell(100, "y") - text_size[1] - returnCell(y_pos, "y")
        case other:    pos_y = returnCell(y_pos, "y")
    if x_endpos is not None and y_endpos is not None:
        pass
    return pos_x, pos_y

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
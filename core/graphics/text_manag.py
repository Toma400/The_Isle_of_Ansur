import pygame.rect

from core.graphics.gh_manag import returnCell, revCell, iterateCells, iterateRevCells
from core.decorators import Callable, HelperMethod
from pygame.font import Font
from core.utils import *
#==========|========================================================
# TEXT     | Allows to blit text on the screen
# PUTTERS  |
#==========|========================================================
# Text renderer using scaling and alignment
def put_text (screen, text, font_cat, size, pos_x=0, pos_y=0, align_x=None, align_y=None, colour=None, bg_colour=None, endpos_x=None, endpos_y=None, no_blit=False, raw=False):
    if colour is None: colour = (0, 0, 0) # default text colour is black
    font = font_handler(category=font_cat)
    #======================================
    fontobj = Font(f"{gpath}/core/assets/fonts/{font}", txt_size(size))
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
    if not no_blit: screen.blit(txtobj, (pos_x, pos_y))
    if raw: return txtobj, (pos_x, pos_y) # for rendPut use, returns everything simple blit needs
    return pos_x, pos_y, pos_x+fontobjs[0], pos_y+fontobjs[1] # returns starting and ending position in (x, y, x2, y2) manner [px, not cell%], for adv. functions

# Simple text renderer, without scaling, using absolute cell positions instead
def put_abstext (screen, text, font_cat, size, pos_x, pos_y, colour=None, bg_colour=None):
    if colour is None: colour = (0, 0, 0) # default text colour is black
    pos_x = returnCell(pos_x, "x")
    pos_y = returnCell(pos_y, "y")
    font = font_handler(category=font_cat)
    # 'size' is not cell-related because this would restrict precision
    #======================================
    fontobj = Font(f"{gpath}/core/assets/fonts/{font}", txt_size(size))
    txtobj = fontobj.render(text, True, colour, bg_colour)
    screen.blit(txtobj, (pos_x, pos_y))

# Text renderer for long strings, allows for line breaks and dynamic resizing | text_spacing_y uses pixels for bigger precision, the rest operates on cell%
def put_rectext (screen, text, font_cat, rect_x, rect_y, endrect_x, endrect_y, rect_spacing: tuple = (0, 0), req_size=50, colour=None, bg_colour=None, text_spacing=0.2, no_blit=False):
    givlist = txt_split(text, [screen, font_cat, rect_x, rect_y, endrect_x, endrect_y, rect_spacing,
                               txt_size(req_size), colour, bg_colour, text_spacing]) # list of lines for text
    height_given = endrect_y - rect_y
    retlist = [] # for no_blit

    while True:
        line_height = revCell(text_spacing, "y") + revCell(txt_rect_size(text, font_cat, txt_size(req_size), screen)[1], "y") # checks height of line (font height + spacing)
        if height_given < len(givlist) * line_height: # checks if all lines will fit given space (if not, reduces font size)
            req_size -= 1
            givlist = txt_split(text, [screen, font_cat, rect_x, rect_y, endrect_x, endrect_y, rect_spacing,
                                       txt_size(req_size), colour, bg_colour, text_spacing]) # list of lines for text
            continue
        break

    for i in givlist:
        pos_x, pos_y = rect_x + rect_spacing[0], rect_y + rect_spacing[1]  # starting position for text (with user-given gap, default 0 / 0)
        if no_blit: # used for listboxes or when you need to delay blitting text
            retlist.append(put_text(screen, i, font_cat, txt_size(req_size), pos_x, pos_y, colour=colour, bg_colour=bg_colour, no_blit=True, raw=True))
        else: # normal use
            put_text(screen, i, font_cat, txt_size(req_size), pos_x, pos_y, colour=colour, bg_colour=bg_colour)
        rect_y += revCell(text_spacing, "y") + revCell(txt_rect_size(text, font_cat, txt_size(req_size), screen)[1], "y") - rect_spacing[1] # minus to make only first line use rect_spacing

    if no_blit: return retlist

def put_lore(lang):
    pass # placeholder function for lore text, which will not be translateable through langkeys, but
    # refer to specific Baedoor fonts, such as ghloddish (or, later, trish and so on); font will
    # be automatically used based on language
    return ""

#==========|========================================================
# FONT     | Decides on font used depending on category and language
# HANDLER  | You can pass font manually (use category=None then)
#==========|========================================================
# Fonts change because not all fonts support specific alphabets
def font_handler (category: str, font=None):
    match category:
        case "menu":
            if scx("lang") == "polish": font = "ferrum.otf"
            else:                       font = "ferrum.otf"
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
    lang = scx("lang")
    import toml; t = toml.load(f"{gpath}/core/lang/{lang}.toml")
    return t[key]

def langjstring (key: str, modtype: str, modid: str = "ansur"):
    try:
        read = json_read(f"{modtype}/{modid}/lang.json", scx("lang"))
    except KeyError:
        try:
            read = json_read(f"{modtype}/{modid}/lang.json", "english")
        except KeyError:
            log.warning(f"Module {modid} does not have properly set language value for {key}. Please contact the developer of this module for help.")
            return langstring("system__text_load_fail")
    return read[key]

#==========|========================================================
# TEXT     | Splits text into list of lines, checking if size fits
# SPLITTER | rectangle given
#          | It splits at sentences and linebreak characters ("@*")
#==========|========================================================
def txt_split (text_given: str, tdata: list):
    out_lines = []  # final outcome of function, list of separate lines to print

    while text_given != "":
        text_given = text_given.split()  # list of words from text
        line_break = False               # after string is detected to not fit into line, this disables checking of later words to not "jump across"
        text_going = ""                  # string which will be rendered in current line
        text_leaving = ""                # string which will be splitted in next line
        sep = ""                         # separator initially is "", to make sentence not have space before first word

        out_lines_add = out_lines.append # for fastening up looped code

        for i in text_given:
            temp_going = text_going + sep + i # string which checks if text can extend with next word
            if txt_rect_manag(tdata[0], temp_going, tdata[1], tdata[2], tdata[3], tdata[4], tdata[5], tdata[6], tdata[7], tdata[8], tdata[9], tdata[10], do_blit=False) and line_break is False:
                if "@*" in i:
                    text_going += sep + i.replace("@*", "")
                    line_break = True # forces end of the line
                else: text_going += sep + i
            else: # if string is too long
                text_leaving += sep + i
                line_break = True # makes loop not be able to overwrite previous string after reaching limit (w/o it, shorter word could get into original string, outside of order)
            sep = " " # separator changes to space after first loop run
        out_lines_add(text_going)
        text_given = text_leaving # left string is given to next iteration

    return out_lines

# Returns size of text rectangle (<->)
def txt_rect_size (text, font_cat, size, screen):
    put_x, put_y, put_x2, put_y2 = put_text(screen, text, font_cat, size, 0, 0, no_blit=True)
    req_x, req_y = put_x2 - put_x, put_y2 - put_y  # rectangle of text
    return req_x, req_y

#==========|========================================================
# ????     | ------
# ???????? | ------
#          | ------
#==========|========================================================
def txt_rect_manag (screen, text, font_cat, rect_x, rect_y, endrect_x, endrect_y, rect_spacing: tuple = (0, 0), req_size=50, colour=None, bg_colour=None, text_spacing=0.2, do_blit=True):
    # variables required for further work
    available_x = returnCell(endrect_x, "x") - returnCell(rect_x, "x") - returnCell(rect_spacing[0], "x") * 2  # rectangle of available size (x axis)
    available_y = returnCell(endrect_y, "y") - returnCell(rect_y, "y") - returnCell(rect_spacing[1], "y") * 2  # rectangle of available size (y axis)
    pos_x, pos_y = rect_x + rect_spacing[0], rect_y + rect_spacing[1] # starting position for text (with user-given gap, default 0 / 0)
    req_x, req_y = txt_rect_size(text, font_cat, req_size, screen)    # gets size of text rectangle, to compare below
    #----------------------------------------------------------
    # Checker if required <-> is enough to fit available length
    if req_x <= available_x and req_y+text_spacing <= available_y:
        if do_blit:
            put_text(screen, text, font_cat, req_size, pos_x, pos_y, colour=colour, bg_colour=bg_colour) # default: blits the text in respective position
        else: return True # used by put_rectext (returns info that this line can be printed)
    else:
        return False

# adjusts size to modifier in settings
def txt_size (size):
    return int(size*scx("txts"))

#==========|========================================================
# TEXT     | Used for objectify text features in cleaner way
# OBJECT   |
#          |
#==========|========================================================
class Text:

    txt_colour = (0, 0, 0)
    bg_colour  = None

    def __init__(self, text: str, pos: tuple, fonts: str, size: int):
        """
        text  | Raw text or language key
        pos   | Tuple of starting x/y and (optional) end x/y values. Work on cell% system.
              | Use either two or four values inside the tuple.
              | Can specify alignment - use "c" to signify center, negative values for
              | down/right and positive for default handling (up/left). Values cannot
              | exceed 100.
        fonts | Specified font category. Use "lore:" prefix to use lore fonts.
        size  | Initial size of the text. Will be adjusted to text size settings.

        @Callable functions return themselves, so can be written in one line, after the dot.
        """
        self.lang:  str = scx("lang")
        self.text       = text
        self.key        = text
        # font / sizes
        self.size       = size
        self.txt_font   = self.font(fonts).txt_font
        self.fontobj    = Font(f"{gpath}/core/assets/fonts/{self.txt_font}", txt_size(size))
        self.txt_size   = self.fontobj.size(self.text) # size of currently rendered text
        # positions
        self.pos        = self.pos_unpacker(pos)           # px value (based on cell%/align given)
        self.cellpos    = self.iterate_rev_cells(self.pos) # cell%    (based on previous calculations)
        # square objects
        self.is_rect    = len(pos) == 4 # checks if position given is simple (len=2) or rectangular (len=4)
        self.rect       = pygame.rect.Rect(self.pos) if self.is_rect else self.field()

        # shorteners for functions
        self.lstr       = self.langstring
        self.ljstr      = self.langjstring

    @Callable
    def colour(self, tcol=(0, 0, 0), bcol=None):
        """Changes default colour of the text"""
        self.txt_colour = tcol
        self.bg_colour  = bcol

    @Callable
    def font(self, font_cat):
        """Chooses font depending on category ('lore:' prefix allows for use of lore fonts)"""
        if "lore:" not in font_cat: self.txt_font = font_handler(category=font_cat)
        else:                       self.txt_font = put_lore(font_cat.replace("lore:", ""))

    @Callable
    def put(self, screen):
        txtobj = self.fontobj.render(self.text, True,
                                     self.txt_colour, self.bg_colour)
        screen.blit(txtobj, (self.pos[0], self.pos[1]))

    @Callable
    def move(self, dest: tuple):
        """Changes initial position of the text. Needs reusing of `put()` if done after blitting text."""
        self.pos        = self.pos_unpacker(dest)          # px value (based on cell%/align given)
        self.cellpos    = self.iterate_rev_cells(self.pos) # cell%    (based on previous calculations)
        self.rect       = pygame.rect.Rect(self.pos) if self.is_rect else self.field()

    @Callable
    def resize(self, dest: int):
        pass # update fontobj, txt_size and size ig

    @Callable
    def langstring(self):
        """Converts -text- passed to the value of respective key in main language file"""
        import toml; t = toml.load(f"{gpath}/core/lang/{self.lang}.toml")
        self.text = t[self.key]

    @Callable
    def langjstring(self, modtype: str, modid: str = "ansur"):
        """Converts -text- passed to the value of respective key in language file of pack with specified type & ID"""
        try:
            read = json_read(f"{modtype}/{modid}/lang.json", self.lang)
        except KeyError:
            try:
                read = json_read(f"{modtype}/{modid}/lang.json", "english")
            except KeyError:
                log.warning(
                    f"Module {modid} does not have properly set language value for {self.key}. Please contact the developer of this module for help.")
                return langstring("system__text_load_fail")
        self.text = read[self.key]

    def collider(self):
        """Returns if mouse was colliding with the text"""
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def pressed(self, mb: int = 0):
        """Returns if mouse was colliding with the text when specific mouse button was pressed"""
        return self.collider() and pygame.mouse.get_pressed()[mb]

    @HelperMethod
    def pos_unpacker(self, dest_tp: tuple):
        if len(dest_tp) > 4: raise ValueError (f"Text object -pos- argument cannot take more than four arguments. Arguments given: {len(dest_tp)}.")

        def iterate_varied_cells(values: tuple):
            no = 0; values = list(values)
            for i in values:
                if type(i) == int and 100 >= i >= 0:
                    if not no+2 % 2: values[no] = returnCell(i, "x")
                    else:            values[no] = returnCell(i, "y")
                if type(i) == int and -100 <= i < 0:
                    ic = i*-1
                    if not no+2 % 2: values[no] = returnCell(100, "x") - self.txt_size[0] - returnCell(ic, "x")
                    else:            values[no] = returnCell(100, "y") - self.txt_size[1] - returnCell(ic, "y")
                if type(i) == str and i == "c" and no < 2:
                    if not no+2 % 2: values[no] = returnCell(100, "x") / 2 - self.txt_size[0] / 2
                    else:            values[no] = returnCell(100, "y") / 2 - self.txt_size[1] / 2
                    if self.is_rect: values[no+2] = "c"
                if type(i) == str and i == "c" and no >= 2:
                    values[no] = values[no-2]
                else:
                    log.error(f"Text cell values: {values} are not proper (are not integer, proper string, or exceed 100). Crash is to be expected.")
                no += 1
            return tuple(values)
        return iterate_varied_cells(dest_tp)

    @HelperMethod
    def iterate_rev_cells(self, values: tuple):
        no = 0; values = list(values)
        for i in values:
            if not no+2 % 2: values[no] = revCell(i, "x")
            else:            values[no] = revCell(i, "y")
            no += 1
        return tuple(values)

    @HelperMethod
    def field(self):
        """Used to determine rectangle of the text if not given (for len(pos)=2)"""
        return pygame.rect.Rect(self.pos[0],
                                self.pos[1],
                                self.txt_size[0],
                                self.txt_size[1])
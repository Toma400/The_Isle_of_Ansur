from core.graphics.gh_manag import returnCell, returnCells, revCell, nestCell, nestCells, rendPut, imgPutRes, Image
from core.decorators import Callable, HelperMethod
from core.graphics.text_manag import put_text
from core.utils import scx
from enum import Enum, auto
import pygame, logging

#========|===========================================================
# LISTBX | Values to state:
#--------|---------------
#        | x/y/end_x/end_y = % of screen
#========|===========================================================
class PatternType(Enum):
    IMAGE = auto()
    TEXT  = auto()

#def pattern_builder(ptype: PatternType.name, *args, **kwargs):
#    match ptype:
#        case PatternType.IMAGE: return Image(*args, **kwargs)
#        case PatternType.TEXT:  return None

#example_pattern = [
#    pattern_builder(PatternType.IMAGE, path="core/assets/visuals/", file="skill_1.jpg", pos=(0, 0, 10, 10))
#]

class ListBox:

    element_cap   = scx("lbam")
    pattern: list = None

    def __init__(self, main_rect: tuple):
        """
        main_rect | Tuple of cell% values to draw main rectangle
        """
        # Raw values (cell%, as passed, just after some checks to validate their values)
        self.raw_mnrect  = self.tuple_test(main_rect, "-main_rect-") #| Main rectangle (containing list elements)
        self.raw_elrect  = self.elrect_builder(self.raw_mnrect)      #| Element rectangle (containing patterns)

        self.mnrect      = returnCells(self.raw_mnrect[0], self.raw_mnrect[1]), returnCells(self.raw_mnrect[2], self.raw_mnrect[3])
        self.elrect      = returnCells(self.raw_elrect[0], self.raw_elrect[1])

    #@Callable
    #def build_pattern(self, ptype: PatternType, pos: tuple, *args, **kwargs):
    #    if len(pos) != 4: raise ValueError(f"Pattern -pos- argument has to contain 4 values.")
    #    repos = nestCells(pos[0], pos[1], self.elrect[0], self.elrect[1]), nestCells(pos[2], pos[3], self.elrect[2], self.elrect[3])
    #    print(repos)
        #match ptype:
        #    case PatternType.IMAGE: self.pattern.append(Image(pos=repos, *args, **kwargs))
        #    case PatternType.TEXT:  self.pattern.append(None)

    @Callable
    def put(self, screen):
        for i in self.pattern:
            i.put(screen)

    @HelperMethod
    def tuple_test(self, checked: tuple, checktype: str = ""):
        if len(checked) != 4:                                      raise ValueError(f"Passed {checktype} argument with {len(checked)} values instead of 4.")
        if checked[2]-checked[0] < 0 or checked[3]-checked[1] < 0: raise ValueError(f"Passed {checktype} argument with values of negative rectangle.")
        return checked

    @HelperMethod
    def elrect_builder(self, base: tuple):
        return base[2]-base[0], (base[3]-base[1]) // self.element_cap

    def inspect(self):
        insp = (f"""
        Inspector >>> printing values of requested ListBox:
        =============================================================
        RawMainRect:    {self.raw_mnrect}
           NonRaw:      {self.mnrect}
        RawElementRect: {self.raw_elrect}
           NonRaw:      {self.elrect}
        """)
        print(insp); logging.info(insp); return insp

class OldListBoxPattern:

    def __init__(self, *args, **kwargs):
        self.rects = {}
        for i in kwargs:
            self.rects["rect{0}".format(i)] = [kwargs[i], ]

        # return will look like it:
        # {
        #   rect0: [RectObj, type_of_filler]
        #   rect1: [RectObj, type_of_filler]
        # }

        # issue: RectObj must be nested, meanwhile its creation is outside of scope (it does not know ListBoxRect to refer)

class OldListBox:

    @staticmethod
    def range_counter(page: int): # for listbox ranges visualised on screen, based on settings value
        page = max(page, 1) # assures you never have negative/0 value for pages
        match page:
            case 1:     return (0,                      scx("lbam") - 1)        # page_1: 0-4 for '5' value
            case 2:     return (scx("lbam"),            page * scx("lbam") - 1) # page_2: 5-9 for '5' value
            case other: return ((page-1) * scx("lbam"), page * scx("lbam") - 1) # page_3+: 10-14, 15-19, ... for '5' value

    def __init__(self, x, y, end_x, end_y, reflist: list, pattern: OldListBoxPattern):
        self.rect = pygame.Rect(returnCell(x, "x"),
                                returnCell(y, "y"),
                                returnCell(end_x, "x"),
                                returnCell(end_y, "y"))
        self.list_entries = self.range_counter(1) # listbox range (initially: 0 <> (settings-1))
        self.active: pygame.Rect = None # active subRect which got highlighted (initially: None)

        # for each element in list = make subRects!

#========|===========================================================
# LISTBX | Module aimed on managing listboxes and their presets
# MANAG  |
#========|===========================================================
# size = (height, width)
# mode = settings (proportional/sized)
# preset = each element of the list
# forced_amount = ignores `mode`
# forced_subsize = ignores `mode` and `forced_amount`

# listbox background (texture/image/colour (?))

def put_listbox (screen, pos_x, pos_y, size: tuple, preset, forced_amount=None, forced_subsize: tuple = None):
    # SUBDATA
    endpos_x, endpos_y = returnCell(pos_x, "x") + returnCell(size[0], "x"), returnCell(pos_y, "y") + returnCell(size[1], "y")
    fullwidth, fullheight = endpos_x - pos_x, endpos_y - pos_y
    eq = 0 # equaliser

    elheight = 100 / scx("lbam") # getting height of one element (in ncell%)

    print ("SUBDATA")
    print (pos_x, pos_y, endpos_x, endpos_y, fullwidth, fullheight)
    print (elheight)

    print ("BLITTING")

    # BLITTING
    for item in preset:
        print (nestCell(0, fullwidth), nestCell(eq, fullheight), nestCell(elheight, fullwidth), nestCell(eq+elheight, fullheight))
        rendPut(screen, imgPutRes(screen, "core/assets/visuals/", preset[item]["image"],
                                  revCell(nestCell(pos_x, fullwidth), "x"), revCell(nestCell(pos_y+eq, fullheight), "y"),
                                  revCell(nestCell(pos_x+elheight, fullheight), "x"), revCell(nestCell(pos_y+eq+elheight, fullheight), "y"), #fullwidth / "x" for second?
                                  alpha=False, no_blit=True))
        put_text(screen, preset[item]["main_text"], "menu", 25, revCell(nestCell(pos_x+elheight, fullwidth), "x"), revCell(nestCell(pos_y+eq, fullheight), "y"))
        eq += elheight

def preset_actions():
    end_y = 20; end_x = 100

preset_list = {
    "tavern": {
        "image":     "skill_1.jpg",
        "main_text": "Visit the tavern",
        "action":    {"type":        "teleport",
                      "destination": "ansur:evros_tavern"}
    },
    "tavern_2": {
        "image":     "skill_2.jpg",
        "main_text": "Visit another tavern",
        "action":    {"type":        "teleport",
                      "destination": "ansur:evros_2tavern"}
    },
    "tavern_3": {
        "image":     "skill_3.jpg",
        "main_text": "Visit yet another tavern",
        "action":    {"type":        "teleport",
                      "destination": "ansur:evros_2tavern"}
    }
}
from core.decorators import HelperMethod, Callable, Deprecated
from PIL import Image as PILImage
from operator import sub
from core.utils import *
import logging as log
import pygame

#========|===========================================================
# IMAGE  | General functions to work with images, such as loading
# MANAG  | them and resizing.
#========|===========================================================
# Basic:
def imgLoad(path, name="", alpha=False): # name is optional, if you want to separate folder path from file for some reason
    """Function-aimed alternative to Image.reload()"""
    try:
        surface = pygame.image.load(f"{gpath}/{path}{name}")
        if alpha is False: return surface.convert()
        return surface.convert_alpha()  # for transparent textures (alpha=True)
    except pygame.error: log.error(f"Error occured during loading texture from path [{gpath}/{path}{name}].")
    except FileNotFoundError: log.error(f"Texture from path [{gpath}/{path}{name}] not found.")

@Deprecated("core.graphics.gh_manag.Image")
def imgRes(path, name, dest_x, dest_y, variation=""): # path should be folder path, written like so: [stats/]
    # "variation" let you make two or three versions of the same img by naming it differently (for example: icon_name.png)
    dir_cleaner(path)
    image = PILImage.open(f"{gpath}/{path}{name}")
    image = image.resize((dest_x, dest_y)); image.save(f"{gpath}/_temp/img/{path}{variation}{name}")

# Blits:
@Deprecated("core.graphics.gh_manag.Image")
def imgIter(screen, image):
    for x in range(scx("svx") // image.get_width() + 1):
        for y in range(scx("svy") // image.get_height() + 1):
            screen.blit(image, (x*image.get_width(), y*image.get_height()))

@Deprecated("core.graphics.gh_manag.Image")
def imgFull(screen, folderpath, imgname, alpha=False): # folderpath should be written like so: [stats/]
    imgRes(folderpath, imgname, scx("svx"), scx("svy"))
    screen.blit(imgLoad(f"_temp/img/{folderpath}{imgname}", alpha=alpha), (0, 0))

@Deprecated("core.graphics.gh_manag.Image")
def imgPut(screen, folderpath, imgname, size_x, size_y, pos_x, pos_y, alpha=False, no_blit=False): # size-pos should be cell%
    # folderpath should be written like so: [stats/]
    fs_x, fs_y = returnCells(size_x, size_y)
    fpos_x, fpos_y = returnCells(pos_x, pos_y)
    imgRes(folderpath, imgname, int(fs_x), int(fs_y))
    if no_blit: return imgLoad(f"_temp/img/{folderpath}{imgname}", alpha=alpha), (fpos_x, fpos_y) # for listboxes use
    else: screen.blit(imgLoad(f"_temp/img/{folderpath}{imgname}", alpha=alpha), (fpos_x, fpos_y)) # for normal use

@Deprecated("core.graphics.gh_manag.Image")
def imgPutRes(screen, folderpath, imgname, pos_x, pos_y, endpos_x, endpos_y, alpha=False, no_blit=False, variation=""): # variation where size is based on start-end ratio
    # folderpath should be written like so: [stats/]
    spos_x, spos_y = returnCells(pos_x, pos_y)
    epos_x, epos_y = returnCells(endpos_x, endpos_y)
    vx, vy = epos_x - spos_x, epos_y - spos_y # resolution is based on rectangle corners
    imgRes(folderpath, imgname, int(vx), int(vy), variation)
    if no_blit: return imgLoad(f"_temp/img/{folderpath}{variation}{imgname}", alpha=alpha), (spos_x, spos_y) # for listboxes use
    else: screen.blit(imgLoad(f"_temp/img/{folderpath}{variation}{imgname}", alpha=alpha), (spos_x, spos_y)) # for normal use

# Blit manager (requires pyGame tuple of (image data, position tuple))
def rendPut(screen, data: tuple):
    screen.blit(data[0], data[1])

#===========|========================================================
# CELLS     | Cell system is made to place precisely elements on the
#-----------┘ screen and adjust their size depending on resolution
# settings. It does that by separating window to 100 "cells" and
# using multiplier to percentage given, it will return proper pixel
# length for current resolution.
#===========|========================================================
# Single element:
def returnCell(pos, axis):
    """Returns pixels of specific % of screen passed"""
    if axis == "x": svc = scx("svx") / 100
    else:           svc = scx("svy") / 100
    return int(pos * svc)

# Double element:
def returnCells(pos_x, pos_y):
    """Returns pixels of specific % of screen passed"""
    return returnCell(pos_x, "x"), returnCell(pos_y, "y")

# Any paired element
def iterateCells(values: tuple):
    axis = 2; values = list(values)
    for no, i in enumerate(values):
        if not axis % 2: values[no] = returnCell(i, "x")
        else:            values[no] = returnCell(i, "y")
        axis += 1
    return tuple(values)

# Pixels to cell%:
def revCell(pos, axis):
    if axis == "x": svc = scx("svx") / 100
    else:           svc = scx("svy") / 100
    return int(pos / svc)

def iterateRevCells(values: tuple):
    axis = 2; values = list(values)
    for no, i in enumerate(values):
        if not axis % 2: values[no] = revCell(i, "x")
        else:            values[no] = revCell(i, "y")
        axis += 1
    return tuple(values)

# Constructs cell% for user-given length (can be used for nested cells):
def nestCell(pos, comparation, spacing=0, axis="x"):
    """
    pos         | int: cell% | Relative coordinate
    comparation | int: px    | Outer rectangle (usually size, not position)
    spacing     | int: cell% | Used for moving the result value
    axis        | str: x / y | Determine axis on which cell% value is based

    Returns cell% value, converted from raw pos/comparation calculations
    """
    svc = comparation / 100
    return int(revCell(pos * svc, axis) + spacing)

# Small function to return ratio-related aspects
def ratioCell(value: int = None, rev_mode=False):
    retval = None
    match rev_mode:
        case False: to_px = returnCell(value, "y"); retval = revCell(to_px, "x") # returns % for x-axis based on the same % of y-axis (useful for square based on y-axis)
        case True:  to_px = returnCell(value, "x"); retval = revCell(to_px, "y") # reverse to above, returns % for y-axis; much rarer use, I suppose
    return retval

#========|===========================================================
# COLLIS | Checks whether element collides with another
#========|===========================================================
# Simple mouse collider using cells:
@Deprecated("pygame::collidepoint")
def mouseColliderCell(st_x, st_y, end_x, end_y):
    pos0 = tuple(returnCells(st_x, st_y))[0] <= pygame.mouse.get_pos()[0] <= tuple(returnCells(end_x, end_y))[0]
    pos1 = tuple(returnCells(st_x, st_y))[1] <= pygame.mouse.get_pos()[1] <= tuple(returnCells(end_x, end_y))[1]
    return pos0 and pos1

# Alternative mouse collider using pixels
@Deprecated("pygame::collidepoint")
def mouseColliderPx(st_x, st_y, end_x, end_y):
    pos0 = (st_x, st_y)[0] <= pygame.mouse.get_pos()[0] <= (end_x, end_y)[0]
    pos1 = (st_x, st_y)[1] <= pygame.mouse.get_pos()[1] <= (end_x, end_y)[1]
    return pos0 and pos1

# Returns whether specific mouse button is pressed (by default = left)
@Deprecated("pygame.mouse.get_pressed()")
def mouseRec(pg_events, mouse_button=1):
    for event in pg_events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == mouse_button:
            return True
    return False


#========|===========================================================
# HELPER | Some helping functions to keep code cleaner
#========|===========================================================
# Used to switch screen. Put this return in respective guitype[pos]
@Deprecated("Temporarily deprecated in favour of 'switch_gscr'. To be restored when PyGameGUI support is dropped.")
def switch_scr(screen, gui_aimed):
    screen.fill("#000000"); log.debug(f"Switching screen to guitype value: [{gui_aimed}]")
    return gui_aimed

def switch_gscr(dscreen, screen, gui_aimed):
    """Requires dynamic_screen instead of its [0] value - important to switch argument during transition"""
    dscreen.clear_pgui()
    screen.fill("#000000"); log.debug(f"Switching screen to guitype value: [{gui_aimed}]")
    return gui_aimed

# Checks if temp directory exists, and if not, then creates one
def dir_cleaner(path):
    if not os.path.isdir(f"{gpath}/_temp/img/{path}"):
        os.makedirs(f"{gpath}/_temp/img/{path}")

#==========|========================================================
# IMAGE    | Used for objectify image features
# OBJECT   |
#          |
#==========|========================================================
class Image:

    alpha = True # transparency

    def __init__(self, path: str, file: str, pos: tuple):
        """
        path | Folder path to the image (should end with "/")
        file | File name with extension
        pos  | Coordinates of the image (tuple of two or four values). If tuple has four values, it will draw rectangle and resize image to fit within it.
             | You can use -ratioCell- to match positions to squared form:
             |    (0, 0, ratioCell(10), 10) <--- will return square of height of 10% of screen and exact width (of 10%*ratio)
        """
        self.path    = path
        self.imgname = file
        self.load    = self.reload()
        self.rawpos  = pos
        self.fpos    = len(pos) == 4           # tells if position given is rectangular (will disable optional size argument + resizing)
        self.pos     = self.pos_unpacker(pos)

        # shorteners for functions
        self.res     = self.resize
        self.col     = self.collider
        self.is_res  = False                   # check for resizing

    @Callable
    def swap_alpha(self):
        """Swaps alpha of the image"""
        self.alpha = not self.alpha
        self.load  = self.reload()

    @Callable
    def resize(self, size: tuple, variation: str = ""):
        """Resizes the image, creating a copy in _temp folder. Uses px values, so returnCells() method in arguments is required to get cell% values"""
        image = PILImage.open(f"{self.path}{self.imgname}")

        if self.is_res is False:                            # debugging feature to avoid looped relocation of path (bug #75)
            dir_cleaner(self.path)                          # prepare _temp directory
            self.path    = f"_temp/img/{self.path}"         # changing path to _temp
            self.imgname = f"{variation}{self.imgname}"     # changing img name to include variation
            self.is_res  = True

        image        = image.resize(size); image.save(f"{self.path}{self.imgname}")
        self.load    = self.reload()

    @Callable
    def size(self, dest: tuple):
        """Allows for setting up size of the image. Only works if object's -pos- had two values passed. Uses cell% as values"""
        if self.fpos: raise ValueError(f"""Tried using -size- method on Image having rectangular position. Method should be used only for objects using two values for -pos- argument""")
        else:
            override = (self.rawpos[0], self.rawpos[1], self.rawpos[0]+dest[0], self.rawpos[1]+dest[1])
            self.rawpos = override
            self.fpos   = True
            self.pos    = self.pos_unpacker(override)

    @Callable
    def full(self):
        """Resizes the image to cover whole screen. Used mostly for panorama and backgrounds. Common variation name: -full-"""
        override = (0, 0, 100, 100)
        self.rawpos = override
        self.fpos   = True
        self.pos    = self.pos_unpacker(override)

    @Callable
    def put(self, screen, variation: str = ""):
        """Blits the image on given position, or on given rectangle (resizing the image).
        variation | Allows for setting name for resized image (recommended when using -full- method)"""
        if not self.fpos: screen.blit(self.load, self.pos)
        else:
            self.resize(tuple(map(sub, self.pos[1], self.pos[0])), variation) # resizes the image to match the rectangle given
            screen.blit(self.load, self.pos[0])

    @Callable
    def iterblit(self, screen):
        """Blits the image in tileable fashion across given rectangle (in contrary of -put- method). You can still resize image itself earlier to manipulate size of image"""
        if not self.fpos: raise ValueError("Tried using -iter- method on Image having two values for -pos- argument, while said method require four values.")
        else:
            aimed = self.pos[1]
            for x in range(aimed[0] // self.load.get_width() + 1):
                for y in range(aimed[1] // self.load.get_height() + 1):
                    screen.blit(self.load, (x * self.load.get_width(), y * self.load.get_height()))

    def collider(self):
        """Returns whether mouse is colliding with the image"""
        rect_py = pygame.rect.Rect(self.pos[0], self.pos[1], self.load.get_width(), self.load.get_height())
        return rect_py.collidepoint(pygame.mouse.get_pos())

    def pressed(self, mb: int = 0):
        """Returns if mouse was colliding with the text when specific mouse button was pressed"""
        return self.collider() and pygame.mouse.get_pressed()[mb]

    @HelperMethod
    def reload(self):
        """Main updating method after working on image file, reloads image"""
        try:
            surface = pygame.image.load(f"{gpath}/{self.path}{self.imgname}")
            if self.alpha is False: return surface.convert()
            else:                   return surface.convert_alpha()
        except pygame.error:      log.error(f"Error occured during loading texture from path [{gpath}/{self.path}{self.imgname}].")
        except FileNotFoundError: log.error(f"Texture from path [{gpath}/{self.path}{self.imgname}] not found.")

    @HelperMethod
    def pos_unpacker(self, dest_tp: tuple):
        if len(dest_tp)   == 4: return returnCells(dest_tp[0], dest_tp[1]), returnCells(dest_tp[2], dest_tp[3])
        elif len(dest_tp) == 2: return returnCells(dest_tp[0], dest_tp[1])
        else:                   raise ValueError(f"Invalid value amount for -pos- argument of Image object (should be 2 or 4). Values given: {len(dest_tp)}.")

    def inspect(self):
        insp = (f"""
        Inspector >>> printing values of requested Image:
        =============================================================
        Filepath:    {self.path}{self.imgname}
        RawPosition: {self.rawpos}
           NonRaw:   {self.pos}
        IsAlpha:     {self.alpha}
        """)
        print(insp); logging.info(insp); return insp

class NestedImage(Image):

    def __init__(self, path: str, file: str, pos: tuple):
        """
        Takes temporary arguments, same as Image class. With difference:
        pos | in NestedImage it takes relative coordinates, which will
            | be adjusted to rectangle when -nest- method is used
        Do not use inherited methods before running -sup- method
        """
        self.temppath = path
        self.tempfile = file
        self.temppos  = pos

    @Callable
    def nest(self, nestpos: tuple):
        """Adjusts given -pos- to rectangle in which Image is nested. Needs four values inside tuple, creating outer rectangle (in %)."""

        if len(nestpos) != 4: raise ValueError(f"Passed argument to -nest- method with {len(nestpos)} values instead of required 4.")

        temppos_math = [] #| temp list to operate in the loop
        nestpos_size = {"x": returnCell(nestpos[2], "x") - returnCell(nestpos[0], "x"), #| size of the nestpos
                        "y": returnCell(nestpos[3], "y") - returnCell(nestpos[1], "y")}
        movement     = {"x": nestpos[0],                                                #| first two values which are needed to adjust positions
                        "y": nestpos[1]}

        # used in_range() below to get correct index (-> multiple occurences in list, index yields first occurence)
        for i in range(len(self.temppos)):
            if i % 2 == 0: axis = "x" #| choosing axis
            else:          axis = "y"

            nestval = nestCell(self.temppos[i],    #| relative position being compared to:
                               nestpos_size[axis], #|   └-> outer rectangle size
                               movement[axis],     #| pushing the value further if requested
                               axis)
            temppos_math.append(nestval)

        self.temppos        = tuple(ing for ing in temppos_math)

    @Callable
    def sup(self):
        """Should be called only once, after using -nest- method"""
        super().__init__(self.temppath, self.tempfile, self.temppos)
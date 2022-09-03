from core.graphics.gh_manag import returnCell
from pygame.font import Font
from core.utils import *

def put_text (screen, text, font, size, pos_x, pos_y, colour=None, bg_colour=None):
    if colour is None: colour = (0, 0, 0) # default text colour is black
    pos_x = returnCell(pos_x, "x")
    pos_y = returnCell(pos_y, "y")
    # 'size' is not cell-related because this would restrict precision
    #======================================
    fontobj = Font(f"{gpath}/core/assets/fonts/{font}", size)
    txtobj = fontobj.render(text, True, colour, bg_colour)
    screen.blit(txtobj, (pos_x, pos_y))
from core.file_system.theme_manag import get_theme_file, getTheme, fontHandler
from core.graphics.text_manag import txt_size
from core.decorators import RequiresImprovement, HelperMethod
from PIL import Image as PILImage
from core.utils import scx, gpath
from pygame.image import load as imgLoad
from pygame.font import Font
from core.utils import scx
from os.path import exists
from pathlib import Path
import logging as log
import os

# TTooltip, as in 'Temporary Tooltip', because text handling will be taken manually here, samely with box drawing
# Proper Tooltip will use Image and Text, most likely
class TTooltip:

    @RequiresImprovement # make it multiline and dependent on Image/Text in core.gui.elements
    def __init__(self, text: str, text_size: int, pos: (int, int) = (0, 0)):
        """
        text      : str        | Text visible on tooltip (if translated, use langstr() in call)
        text_size : int        | Size of text - affects drawing
        """
        self._theme_general = get_theme_file()["tooltip"]["general"]
        self._theme_colour  = get_theme_file()["tooltip"]["colours"]
        self._theme_font    = fontHandler("tooltip")
        self._fontobj       = Font(f"{gpath}/themes/{getTheme()}/fonts/{self._theme_font}", txt_size(text_size, "tooltip"))
        self._text          = text
        self._text_size     = self._fontobj.size(self._text)
        # bg_img maths
        tooltip_bg          = f"themes/{getTheme()}/assets/{get_theme_file()['backgrounds']['tooltip']}"
        if not exists(f"{gpath}/{tooltip_bg}"):
            log.error(f"Couldn't find theme image of path: {tooltip_bg}. Loading default one...")
            tooltip_bg = "core/assets/visuals/test_img_0.png"
        tooltip_bg_res      = self._resize(tooltip_bg, (self._text_size[0] + self._theme_general["padding_side"]*2,  # width/height is text size + padding
                                                        self._text_size[1] + self._theme_general["padding_tops"]*2))
        self._bg_img        = imgLoad(tooltip_bg_res)
        self._bg            = self._bg_img.convert_alpha()
        self._pos           = pos
        # draw method supplementary
        self._ev_pos        = None                           # final position of bg_img (adjusts to drawing position/text)
        self._check_pos     = (-9999, -9999)                 # checking variable if bg_img position was checked against current rel_pos

    def draw(self, screen, rel_pos: (int, int) = None):
        """
        rel_pos   : (int, int) | Point from where draw should appear - tooltip will adjust from it
        """
        if scx("tltp"):
            if rel_pos is None: rel_pos = self._pos
            # check is done once to minimise overload (see __init__ supplementary comments for context)
            if self._ev_pos is None or self._check_pos != rel_pos:
                self._check_pos = rel_pos
                if rel_pos[0] + self._bg.get_width() < scx("svx"):
                    if rel_pos[1] + self._bg.get_height() < scx("svy"):
                        self._ev_pos = rel_pos
                    else:
                        if rel_pos[1] - self._bg.get_height() > 0:
                            self._ev_pos = (rel_pos[0], rel_pos[1] - self._bg.get_height())
                else:
                    if rel_pos[1] + self._bg.get_height() < scx("svy"):
                        self._ev_pos = (rel_pos[0] - self._bg.get_width(), rel_pos[1])
                    else:
                        if rel_pos[1] - self._bg.get_height() > 0:
                            self._ev_pos = (rel_pos[0] - self._bg.get_width(),
                                            rel_pos[1] - self._bg.get_height())

            if self._ev_pos is not None: # equivalent to 'is ev_pos still None?'
                # rect blit
                screen.blit(self._bg, dest=self._ev_pos)
                # text blit
                render = self._fontobj.render(self._text, True,
                                              self._theme_colour["text"],
                                              self._theme_colour["background"])
                screen.blit(render, (self._ev_pos[0] + self._theme_general["padding_side"],
                                     self._ev_pos[1] + self._theme_general["padding_tops"]))
            else:
                log.error(f'''
                Couldn't draw tooltip due to either too long text, too big size or unfortunate placement. Tooltip info:
                Pos   : {rel_pos[0]}, {rel_pos[1]}
                Size  : {self._bg.get_width()}, {self._bg.get_height()}
                Text  :
                {self._text}
                TSize : {self._text_size}
                ''')

    @staticmethod
    @HelperMethod
    def _resize(path: str, dest: (int, int)) -> str:
        dir_path  = f"{gpath}/_temp/img/"
        full_path = list(Path(path).parts)
        full_path.pop()
        for p in full_path:
            dir_path += f"{p}/"
        if not exists(dir_path):
            os.makedirs(dir_path)

        buf_img = PILImage.open(path)
        buf_img = buf_img.resize(dest)
        buf_img.save(f"{gpath}/_temp/img/{path}")
        return f"{gpath}/_temp/img/{path}"
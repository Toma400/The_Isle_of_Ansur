from core.file_system.theme_manag import fontHandler
from core.graphics.text_manag import txt_size
from core.graphics.gh_manag import returnCell
from core.utils import gpath
from pygame.font import Font
import pygame

class InputBox:

    def __init__(self, x, y, end_x, end_y, text_colour="#403F3B", background=None, font=None):
        # Rect setup -------------------------------------------------
        self.rect = pygame.Rect(returnCell(x, "x"),     returnCell(y, "y"),
                                returnCell(end_x, "x"), returnCell(end_y, "y"))

        # Background setup -------------------------------------------
        if "src=" in background: # for image (path)
            self.bgrnd_type = "source"
            self.background = background.replace("src=", "")

        if "cl=" in background: # for pure colour background (hexcode)
            self.background = background.replace("cl=", "")

        else: self.background = "#E6E3D3" # default dark cream background
        # Font setup -------------------------------------------------
        if font is not None: self.font = Font(f"{gpath}/core/assets/fonts/{font}", txt_size(size, font_cat))
        else:                self.font = fontHandler(category="menu")

        # Other variables --------------------------------------------
        self.text        = ''          # text inside the input box
        self.active      = False       # indicates whether it got clicked on
        self.txt_colour  = text_colour # colour of the text
        self.txt_surface = self.font.render(self.text, True, self.txt_colour)

    #===============================================================================================
    def handle_event(self, pg_events):
        event = pg_events

        # Activates the input box when clicked on rect
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

        # Appends new characters to the text
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                self.txt_surface = self.font.render(self.text, True, self.txt_colour) # Re-render the text after change

    #===============================================================================================
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    #===============================================================================================
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
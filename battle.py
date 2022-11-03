import pygame; pygame.init(); pygame.mixer.init()
from elements.objects import Screen, Image

screen = Screen()

def re(*funcs): # does all functions in sequential order (non-return ones)
    for i in funcs:
        i

def res(img, dest, pos, screend):
    re(img.resize(dest),
       screend.put_image(img, pos))

while True:
    screen.set().fill("#000000")
    img1 = screen.put_image(img=Image(path="", name="ioa.png"), pos=(0, 0))

    res(img1, (900, 900), (0, 0), screend=screen)
    # ^ is equivalent to v | solves object looping issue + spaghetti code
    #--------------------------------------------------------------------
    #img1.resize((900, 900))
    #screen.put_image(img=img1, pos=(0, 0))

    pygame.display.flip()
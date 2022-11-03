import pygame; pygame.init(); pygame.mixer.init()
from elements.objects import Screen, Image

screen = Screen()

while True:
    screen.set().fill("#000000")
    img = Image("ioa.png")
    screen.put_image(img=img, pos=(0, 0))

    pygame.display.flip()
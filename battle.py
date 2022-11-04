import pygame; pygame.init(); pygame.mixer.init()
from elements.objects import Screen, Image, Menu, Button

tev = []

def re(*funcs): # does all functions in sequential order (non-return ones)
    for i in funcs:
        i

def res(img, dest, pos, screend):
    re(img.resize(dest),
       screend.put_image(img, pos))

def main_loop():
    menu_handler = Menu(Screen())
    screen       = menu_handler.screen

    while not tev:
        screen.set().fill("#000000")
        button1 = Button((15, 15), (15, 15), Image("", "ioa.png"), screen)

        if button1.is_pressed():
            res(Image("assets/weapons/", "golden_scimitar.png"), (300, 300), (0, 0), screen)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                tev.append("end")

        pygame.display.flip()
        print(screen.tick)
        screen.ticking()

main_loop()
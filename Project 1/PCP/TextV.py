import sys, pygame, os
import pygame.freetype
pygame.init()


screen = pygame.display.set_mode((500,500))

def write_line(text, _Coordinate, _font = pygame.freetype.font("NotoSans-Black", 12)):
    print(pygame.freetype.SysFont("NotoSans-Black", 12))
    text_img = _font.render(text, (0,0,0))
    screen.blit(text_img[0], _Coordinate)


def write_lines(text):
    for index, el in enumerate(text.split("\n")):
        write_line(el, (0,1+(64*index)))
        
with open("samp.txt") as s:
    screen_string = "".join(s.readlines())
    
#screen_string = "dd"
pygame.key.set_repeat(400,50)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.WINDOWFOCUSLOST:
            sys.exit()
        
        if event.type == pygame.KEYDOWN: #and event.key == pygame.K_a:
            if event.key == pygame.K_BACKSPACE:
                screen_string = screen_string[0:-1]
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                pass
            elif event.key == pygame.K_RETURN:
                screen_string += "\n"
            else:
                    print((event.key))
                    screen_string += event.unicode
        
        
    screen.fill((255,255,255))
    
    write_lines(screen_string+"|")
    pygame.display.flip()
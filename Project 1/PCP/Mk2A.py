import sys, pygame
import pygame.freetype
pygame.init()


screen = pygame.display.set_mode((500,500))

def write_line(text, _Coordinate, _font = pygame.freetype.SysFont('Sans', 50)):
    text_img = _font.render(text, (0,0,0))
    _font.render_to
    #screen.blit(text_img, _Coordinate)

def write_lines(text):
    for index, el in enumerate(text.split("\n")):
        write_line(el, (0,0+(16*index)))
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((255,255,255))
    #write_line("lmao", (0,0))
    
    write_lines("ur mother \n and your father")
    pygame.display.flip()
    #pygame.display.update()
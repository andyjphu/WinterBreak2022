import sys, pygame
import pygame.freetype
pygame.init()


screen = pygame.display.set_mode((500,500))

def write_line(text, _Coordinate, _font = pygame.freetype.SysFont('Sans', 50)):
    text_img = _font.render(text, (0,0,0))
    #_font.render_to(screen, _Coordinate, text)
    #print(text_img[1][0],text_img[1][1],text_img[1][2],text_img[1][3])
    #screen.blit(text_img[0], text_img[1])
    #screen.blit(text_img[0], pygame.rect.Rect(0,0,100,100))
    screen.blit(text_img[0], _Coordinate)


def write_lines(text):
    for index, el in enumerate(text.split("\n")):
        write_line(el, (12,12+(64*index)))
        
screen_string = "ur mother \nand your father" 
pygame.key.set_repeat(400,50)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.KEYDOWN: #and event.key == pygame.K_a:
            if event.key == pygame.K_BACKSPACE:
                screen_string = screen_string[0:-1]
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                pass
            elif event.key == pygame.K_RETURN:
                screen_string += "\n"
            #elif event.type == pygame
            #print(pygame.key.get_pressed())
            else:
                if event.mod & pygame.KMOD_SHIFT:
                    print("shifting")

                    screen_string += str.capitalize(chr(event.key))
                else:
                    print((event.key))
                    screen_string += chr(event.key)
    screen.fill((255,255,255))
    #write_line("lmao", (0,0))
    
    write_lines(screen_string+"|")
    pygame.display.flip()
    #pygame.display.update()
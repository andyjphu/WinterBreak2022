import pygame, sys

pygame.init()

screen = pygame.display.set_mode((500,500))

surf = pygame.surface.Surface((10,10))
r = pygame.Rect(100,100,100, 100)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    #pygame.draw(, )
    #screen.fill ((255,0,0))
    r.move_ip(5,0)
    pygame.draw.rect(screen,(255,0,0),r,10)
    
    pygame.display.flip()
    pygame.time.wait(500)
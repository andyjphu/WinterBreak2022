import pygame, sys

pygame.init()

screen = pygame.display.set_mode((500,500))

surf = pygame.surface.Surface((10,10))

class alpha_body(pygame.Rect):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    
r = pygame.Rect(100,100,100, 100)
vy = 0
ay = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    
    screen.fill ((255,255,255))
    pygame.draw.rect(screen,(255,0,0),r,10)
    
    vy += ay
    r.move_ip(0,vy)
    
    if r.bottom >= 500:
        r.top = 0
    
    pygame.display.flip()
    pygame.time.wait(100)
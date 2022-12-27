import pygame, sys

pygame.init()

screen = pygame.display.set_mode((500,500))

surf = pygame.surface.Surface((10,10))

    
r = pygame.Rect(100,100,100, 100)
f = pygame.font.Font(None,50)
vy = 0
ay = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        

    screen.fill ((255,255,255))
    pygame.draw.rect(screen,(255,0,0),r,10)
    f_img = f.render("XX_XX_XXXX",True,(0,0,0))    
    
    vy += ay
    r.move_ip(0,vy)
    
    if r.bottom >= 500:
        r.top = 0
    
    
    screen.blit(f_img,(250,250))
    pygame.display.flip()
    pygame.display.update()
    pygame.time.wait(100)
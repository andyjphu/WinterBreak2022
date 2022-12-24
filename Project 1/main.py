import sys, pygame
pygame.init()

size = width, height = 500, 500
speed = [2, 2]
black = 100, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

#surf = pygame.surface.Surface((500,500))
magnet_surface = pygame.surface.Surface((10,10)) # you move the surface, not the drawings inside the surface?

magnet_rect = pygame.draw.rect(magnet_surface,(255,0,255),(0,0,10,10),1,1)#pygame.draw.circle(world_screen_surface, (255,0,255),(501,500), 10,10)





magnet_vy = 1
magnet_vx = 1
magnet_ay = -1
magnet_ax = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    magnet_vx += magnet_ax
    magnet_vy += magnet_vy
        
    magnet_rect = magnet_rect.move(magnet_vx,magnet_vx)
    screen.blit(magnet_surface,magnet_rect)
    #magnet.centerx += 10
    pygame.display.flip()

    pygame.time.wait(250)

#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]

#     screen.fill(black)
    
#     #magnet_rect = 
#     magnet_rect = magnet_rect.move(1,-1)
#     screen.blit(ball, ballrect)
#     screen.blit(magnet_surface,magnet_rect)
#     #magnet.centerx += 10
#     pygame.display.flip()
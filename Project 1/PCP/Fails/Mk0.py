import sys, pygame
pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)



alpha_body_surface = pygame.surface.Surface((500,500))
alpha_body_poly = pygame.draw.polygon(alpha_body_surface,(0,255,255),[(0,0),(1,1),(1,2)],1)


#gamma_body_surface = pygame.surface.Surface((500,500))
gamma_body_poly = pygame.draw.polygon(alpha_body_surface,(0,255,255),[(0,0),(1,1),(1,2)],1)


beta_vy = 0.0
beta_vx = -0.0
beta_ay = -0.0
beta_ax = 0.0
alpha_points = [[0,0],[0,0],[0,0]]
gamma_points = [[0,500],[0,500],[0,500]]


beta_surface = pygame.surface.Surface((10,10)) # you move the surface, not the drawings inside the surface? you move the rect inside the surface, a screen percentage of the surface
beta_rect = pygame.draw.rect(beta_surface,(255,0,0),(250,250,250+10,250+10),1,1)#pygame.draw.circle(world_screen_surface, (255,0,255),(501,500), 10,10)


while True:
    beta_vy = 5.0
    beta_vx = -5.0
    beta_ay = -1
    beta_ax = 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill((255,0,0))
    
    beta_vx += beta_ax
    beta_vy += beta_ay
    
  
    beta_rect = beta_rect.move(beta_vx,beta_vy)
    alpha_points += [(beta_rect.x, beta_rect.y)]
    gamma_points += [(beta_rect.x, beta_rect.y)]
    
    alpha_body_poly = pygame.draw.polygon(alpha_body_surface,(0,255,255),alpha_points)
    gamma_body_poly = pygame.draw.polygon(alpha_body_surface,(0,0,255),gamma_points)

    screen.blit(alpha_body_surface,alpha_body_poly)
    screen.blit(alpha_body_surface,gamma_body_poly)
    
    screen.blit(beta_surface,beta_rect)
    pygame.display.flip()


    pygame.time.wait(100)
    print(f"{beta_rect.x},{beta_rect.y}")
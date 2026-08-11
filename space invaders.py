import pygame,os
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("space invaders")
r = (255,0,0)
white = (255,255,255)
black = (0,0,0)
y = (255,255,0)
fps = 60
vel = 5#velocity means how fast something goes and this is for the velocity for the spaceships
bulvel = 7# this is the velocity for the bullets
max_bull = 3
yellowhit = pygame.USEREVENT+1
redhit = pygame.USEREVENT+2
space_ship_width = 55
space_ship_height = 40
path1 = os.path.join("images","spaceship_red.png")
path2 = os.path.join("images","spaceship_yellow.png")
path3 = os.path.join("images","copy_of_space.png")
image1 = pygame.image.load(path1)
i1 = pygame.transform.scale(image1,(space_ship_width,space_ship_height))
image2 = pygame.image.load(path2)
i2 = pygame.transform.scale(image2,(space_ship_width,space_ship_height))
image3 = pygame.image.load(path3)
i3 = pygame.transform.scale(image3,(800,800))
yellow_spaceship = pygame.transform.rotate(i1,90)
red_spaceship = pygame.transform.rotate(i2,270)
border = pygame.Rect(395,0,10,800)
def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    screen.blit(i3,(0,0))
    pygame.draw.rect(screen,(0,0,0),border)
    font = pygame.font.SysFont("Times New Roman",10)
    health1 = font.render("health"+str(yellow_health),True,(0,0,255))
    screen.blit(health1,(50,50))
    health2 = font.render("health"+str(red_health),True,(0,0,255))
    screen.blit(health2,(700,50))
    screen.blit(yellow_spaceship,(yellow.x,yellow.y))
    screen.blit(red_spaceship,(red.x,red.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,y,bullet)
    for bullet in red_bullets:
        pygame.draw.rect(screen,r,bullet)
    pygame.display.update()
def yellow_movement(keypress,yellow):
    if keypress[pygame.K_a]and yellow.x-vel > 0:
        yellow.x-=vel
    if keypress[pygame.K_d]and yellow.x+vel+yellow.width < border.x:
        yellow.x+=vel
    if keypress[pygame.K_w]and yellow.y-vel > 0:
        yellow.y-=vel
    if keypress[pygame.K_s]and yellow.y+vel+yellow.height < 785:
        yellow+=vel
def red_movement(keypress,red):
    if keypress[pygame.K_LEFT]and red.x-vel > border.x+border.width:
        red.x-=vel
    if keypress[pygame.K_RIGHT]and red.x+vel+red.width < 800:
        red.x+=vel
    if keypress[pygame.K_UP]and red.y-vel > 0:
        red.y-=vel
    if keypress[pygame.K_DOWN]and red.y+vel+red.height < 785:
        red.y+=vel
def handeling_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x+=bulvel
        if red.collide(bullet):
            pygame.event.post(pygame.event.Event(redhit))
            yellow_bullets.remove(bullet)
        elif bullet.x > 800:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x-=bulvel
        if yellow.collide(bullet):
            pygame.event.post(pygame.event.Event(yellowhit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
    def main():
        red = pygame.Rect(700,400,space_ship_width,space_ship_height)
        yellow = pygame.Rect(100,400,space_ship_width,space_ship_height)
        redh = []
        yellowh = []
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(yellowh) < max_bull:
                        bullet = pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                        yellowh.append(bullet)






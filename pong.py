import pygame,os
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("pong")
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
fps = 60
vel = 5
bulvel = 7
max_bull = 3
pong1hit = pygame.USEREVENT+1
pong2hit = pygame.USEREVENT+2
pongwidth = 55
pongheight = 40
path1 = os.path.join("images","pong1.png")
path2 = os.path.join("images","pong2.png")
path3 = os.path.join("images","copy_of_space.png")
image1 = pygame.image.load(path1)
i1 = pygame.transform.scale(image1,(pongwidth,pongheight))
image2 = pygame.image.load(path2)
i2 = pygame.transform.scale(image2,(pongwidth,pongheight))
image3 = pygame.image.load(path3)
i3 = pygame.transform.scale(image3,(800,800))
pong1 = pygame.transform.rotate(i1,90)
pong2 = pygame.transform.rotate(i2,270)
border = pygame.Rect(395,0,10,800)
running = True
while running:
    screen.blit(i3,(0,0))
    screen.blit(pong1,(100,400))
    screen.blit(pong2,(700,400))
    pygame.draw.rect(screen,(0,0,0),border)
    pygame.display.update()
pygame.quit()
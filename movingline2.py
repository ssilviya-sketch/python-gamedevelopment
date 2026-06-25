import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("vertical moving line")
white = (255,255,255)
x = 400
screen.fill(white)
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-=20
            if event.key == pygame.K_RIGHT:
                x+=20
    screen.fill(white)
    pygame.draw.line(screen,(0,0,0),(x,500),(x,600),20)
    pygame.display.update()
pygame.quit()


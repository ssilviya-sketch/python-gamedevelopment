import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("moving line")
white = (255,255,255)
y = 400
screen.fill(white)
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y-=20
            elif event.key == pygame.K_DOWN:
                y+=20
    screen.fill(white)
    pygame.draw.line(screen,(0,0,0),(300,y),(500,y),20)
    pygame.display.update()
pygame.quit()
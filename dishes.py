import pygame,os,random,time
pygame.init()
screen = pygame.display.get_mode((800,800))
pygame.display.set_caption("dishes game")
path1 = os.path.join("images","dish1.jpg")
path2 = os.path.join("images","dish2.jpg")
path3 = os.path.join("images","dish3.jpg")
path4 = os.path.join("images","clean.jpg")
path5 = os.path.join("images","dishwasher.jpg")
path6 = os.path.join("images","bg.jpg")
i1 = pygame.image.load(path1)
i2 = pygame.image.load(path2)
i3 = pygame.image.load(path3)
i4 = pygame.image.load(path4)
i5 = pygame.image.load(path5)
bg = pygame.image.load(path6)
dishwasher = pygame.transform.scale(i5,(40,60))
clean = pygame.transform.scale(i4,(40,40))
d1 = pygame.transform.scale(i1,(30,30))
d2 = pygame.transform.scale(i2,(30,30))
d3 = pygame.transform.scale(i3,(30,30))
dirtydishimages = [d1,d2,d3]
rect = dishwasher.get_rect(center = (450,350))
items = []
for _ in range(50):
    img = random.choice(dirtydishimages)
    rect = img.get_rect(x = random.randrange(790),y = random.randrange(790))
    items.append((img,rect))
cleanlist = []
for _ in range(25):
    cleanrect = clean.get_rect(x = random.randrange(790),y = random.randrange(790))
    cleanlist.append(cleanrect)
red = (255,0,0)
blue = (0,0,255)
font = pygame.font.sysfont("Ariel",36)
score = 0
starttime = time.time()
running = True
def changeimg(gameend):
    p = os.path.join("images",gameend)
    b = pygame.image.load(p)
    bg = pygame.transform.scale(800,800)
    screen.blit(bg,(0,0))
clock = pygame.time.Clock()
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    elapsetime = time.time()-starttime
    if elapsetime >= 60:
        if score > 100:
            w = font.render("you won the game",True,(0,0,0))
            changeimg("youwin.jpg")
        else:
            l = font.render("you lost the game",True,(0,0,0))
            changeimg("youlose.jpg")
    else:
        changeimg("bg.jpg")
        timer = font.render("Time left:"+str(60-int(elapsetime)),True,(0,0,0))
import pgzrun,random
HEIGHT = 500
WIDTH = 1000
TITLE = "HEALTHY CLICKER"
apple = Actor("apple")
banana = Actor("banana")
pear = Actor("pear")
burger = Actor("burger")
fries = Actor("fries")
chicken = Actor("chicken")
apple.pos = random.randint(50,80),0
banana.pos = random.randint(100,200),0
pear.pos = random.randint(260,350),0
burger.pos = random.randint(450,575),0
fries.pos = random.randint(625,675),0
chicken.pos = random.randint(750,800),0

score = 0 
def draw():
    screen.fill(color = "white")
    screen.draw.text("the score is "+str(score),(800,50),fontsize = 25,color = "black")
    apple.draw()
    banana.draw()
    pear.draw()
    burger.draw()
    fries.draw()
    chicken.draw()
def update():
    global score
    apple.y+=5
    banana.y+=5
    pear.y+=5
    burger.y+=5
    fries.y+=5
    chicken.y+=5
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        score+=5
    if banana.collidepoint(pos):
        score+=3
    if pear.collidepoint(pos):
        score+=10
    if burger.collidepoint(pos):
        score-=5
    if fries.collidepoint(pos):
        score-=5
    if chicken.collidepoint(pos):
        score-=5
    '''apple.pos = random.randint(50,80),0
    banana.pos = random.randint(100,200),0
    pear.pos = random.randint(260,350),0
    burger.pos = random.randint(450,575),0
    fries.pos = random.randint(625,675),0
    chicken.pos = random.randint(750,800),0
    if apple.y > HEIGHT:
        apple.pos = random.randint(50,80),0
        apple.draw()
        apple.y+=5
    if banana.y > HEIGHT:
        banana.pos = random.randint(100,200),0
        banana.draw()
        banana.y+=5
    if pear.y > HEIGHT:
        pear.pos = random.randint(260,350),0
        pear.draw()
        pear.y+=5
    if burger.y > HEIGHT:
        burger.pos = random.randint(450,575),
        burger.draw()
        burger.y+=5
    if fries.y > HEIGHT:
        fries.pos = random.randint(625,675),0
        fries.draw()
        fries.y+=5
    if chicken.y > HEIGHT:
        chicken.pos = random.randint(750,800),0
        chicken.draw()
        chicken.y+=5'''
pgzrun.go()




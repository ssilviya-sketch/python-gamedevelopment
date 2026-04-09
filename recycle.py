import pgzrun,random
HEIGHT = 800
WIDTH = 800
TITLE = "recycle "
score = 0
items = ["lightbulb","paper","glass"]
waste = Actor(random.choice(items))
waste.pos = random.randint(50,WIDTH-50),0
bin = Actor("bin")
bin.pos = 400,750
def draw():
    screen.fill(color = "white")
    waste.draw()
    bin.draw()
    screen.draw.text("the score is "+str(score),(100,100),fontsize = 25,color = "black")
def update():
    global waste
    global score
    waste.y+=5
    if keyboard.left:
        bin.x = bin.x-5
    if keyboard.right:
        bin.x = bin.x+5
    if waste.colliderect(bin):
        if waste.image == "paper":
            score+=10
        if waste.image == "glass":
            score-=5
        if waste.image == "lightbulb":
            score-=5
        waste = Actor(random.choice(items))
        waste.pos = random.randint(50,WIDTH-50),0
    if waste.y > HEIGHT:
        waste = Actor(random.choice(items))
        waste.pos = random.randint(50,WIDTH-50),0
pgzrun.go()
            

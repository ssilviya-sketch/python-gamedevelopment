import pgzrun , random
HEIGHT = 800
WIDTH = 800
TITLE = "Bumblbee"
game_over = False
score = 0
bee = Actor("bee")
flower = Actor("flower")
bee.pos = 250,250
flower.pos = 100,400
def draw():
    screen.clear()
    screen.blit("background",(0,0))#this is how you add an background
    bee.draw()
    flower.draw()
    screen.draw.text("Score = "+str(score), center = (400,100),fontsize = (30))
    if game_over == True:
        screen.fill(color = "red")
        screen.draw.text("Time is up",center = (250,250),fontsize = (30))
def placing_flower():
    flower.x = random.randint(50,(WIDTH-50))
    flower.y = random.randint(50,(HEIGHT-50))
def time_is_up():
    global game_over
    game_over = True
def update():
    global score
    if keyboard.left:
        bee.x = bee.x-4
    if keyboard.right:
        bee.x = bee.x+4
    if keyboard.up:
        bee.y = bee.y-4
    if keyboard.down:
        bee.y = bee.y+4
    flowercollected = bee.colliderect(flower)
    if flowercollected == True:
        score = score+1
        placing_flower()
clock.schedule(time_is_up,60.0)#this function helps to call a function after a given time
pgzrun.go()


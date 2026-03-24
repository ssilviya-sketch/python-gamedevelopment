import pgzrun,random
HEIGHT = 800
WIDTH = 800
TITLE = "snowman"
game_over = False
score = 0
snowman = Actor("s1")
snowflake = Actor("snow1")
snowman.pos = 350,250
snowflake.pos = 400,400
def draw():
    screen.clear()
    screen.fill(color = "black")
    snowman.draw()
    snowflake.draw()
    screen.draw.text("The score ="+str(score),center = (400,100),fontsize = (30))
    if game_over == True:
       screen.fill(color = "red")
       screen.draw.text("Time is up",center = (250,250),fontsize = (30))
def placing_snowflake():
    snowflake.x = random.randint(50,(WIDTH-50))
    snowflake.y = random.randint(50,(HEIGHT-50))
def time_is_up():
    global game_over
    game_over = True
def update():
    global score
    if keyboard.left:
        snowman.x = snowman.x-4
    if keyboard.right:
        snowman.x = snowman.x+4
    if keyboard.up:
        snowman.y = snowman.y-4
    if keyboard.down:
        snowman.y = snowman.y+4
    snowflakecollected = snowman.colliderect(snowman)
    if snowflakecollected == True:
        score = score+1
        placing_snowflake()
clock.schedule(time_is_up,60.0)
pgzrun.go()




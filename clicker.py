import pgzrun,random 
HEIGHT = 500
WIDTH = 500
TITLE = "Circel clicker"
counter = 0
circle = Actor("smallcircle")
circle.pos = 100,100 
def draw() :
    screen.clear()
    screen.fill((0,252,255))
    circle.draw()
    screen.draw.text(str(counter),center = (400,10),fontsize = 30,color = "black")
def circle_placement() :
    circle.x = random.randint(50,WIDTH-50)
    circle.y = random.randint(50,HEIGHT-50)
def on_mouse_down(pos) :
    global counter 
    if circle.collidepoint(pos) :
        counter = counter+1
        circle_placement()
    else : 
        counter = counter+0
circle_placement()
pgzrun.go()
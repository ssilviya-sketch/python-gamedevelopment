import pgzrun,random 
HEIGHT = 500
WIDTH = 500
TITLE = "good shot"
alien = Actor("alien")#When we have to make an actor we do it like this.
alien.pos = 100,100 #.Pos gives the position to the actor.
message = ""
def draw() :
    screen.clear()
    screen.fill(color = (111,222,255))
    alien.draw()
    screen.draw.text(message,center = (400,10),fontsize = 30)
def place_alien() :
    alien.x = random.randint(50,WIDTH-50)
    alien.y = random.randint(50,HEIGHT-50)
def on_mouse_down(pos) :
    global message 
    if alien.collidepoint(pos) :#collide point checks the collition
        message = "Good shot!"
        place_alien()
    else :
        message = "You missed!"
place_alien()
pgzrun.go()


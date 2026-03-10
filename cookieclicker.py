import pgzrun
HEIGHT = 500
WIDTH = 500
TITLE = "cookie clicker"
counter = 0
cookie = Actor("cookie")
def draw() :
    screen.clear()
    screen.fill((150,75,0))
    cookie.draw()
    screen.draw.text(str(counter),center = (250,50),fontsize = 60,color = "black")
def cookie_placement() :
    cookie.x = 250
    cookie.y = 250
def on_mouse_down(pos) :
    global counter 
    if cookie.collidepoint(pos) :
        counter = counter+1
        cookie_placement()
    else : 
        counter = counter+0
cookie_placement()
pgzrun.go()

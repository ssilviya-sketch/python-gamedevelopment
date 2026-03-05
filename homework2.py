import pgzrun
HEIGHT = 500
WIDTH = 500 
TITLE = "rainbow circles"
def draw() :
    screen.clear()
    screen.draw.circle((100,100),100,"red")
    screen.draw.circle((100,100),90,"orange")
    screen.draw.circle((100,100),80,"yellow")
    screen.draw.circle((100,100),70,"green")
    screen.draw.circle((100,100),60,"blue")
pgzrun.go()
  
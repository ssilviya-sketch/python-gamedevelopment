import pgzrun #the origin of the cordinates is at the top left corner if you you go down y increases if you go up y decreases if you go right x in xreses if you go eft x increases
WIDTH = 500
HEIGHT = 500
TITLE = "shapes"
def draw() :
    screen.clear()
    screen.draw.line((100,100),(300,300),"white")
    screen.draw.circle((350,350),30,"white")
    screen.draw.filled_circle((200,200),35,"yellow")
    r = Rect((100,100),(200,100))
    screen.draw.rect(r,"white")
    screen.draw.filled_rect(r,"white")
    screen.draw.text("Hello",(250,250),color = "yellow")



pgzrun.go()# to make the title you write title in captital and = and the name in double codes
#to clear the screen use screen.clear() 
# to draw a line first screen.draw.line than brackets and first you write the starting point in brackets than ending point than the color
# to make it work you need 2 spaces in between first and than you write pgzrun.go
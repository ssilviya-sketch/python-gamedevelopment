import pgzrun,random,time
HEIGHT = 600
WIDTH = 800
TITLE = "Star GAME"
stars = []
lines = []
nextstar = 0
starttime = 0
totaltime = 0
endtime = 0
numberofstar = 10
def create():
    global starttime
    for i in range(0,numberofstar):
        star = Actor("star")
        star.pos = random.randint(50,(WIDTH-50)),random.randint(50,(HEIGHT-50))
        stars.append(star)
    starttime = time.time()
def draw():
    global totaltime
    screen.blit("space",(0,0))
    number = 1
    for star in stars:
        screen.draw.text(str(number),(star.pos[0],star.pos[1]+20))
        star.draw()
        number+= 1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    if nextstar < numberofstar:
        totaltime = time.time()-starttime
        screen.draw.text(str(totaltime),(10,10),fontsize = 20)
    else: 
        screen.draw.text(str(totaltime),(10,10),fontsize = 20)
def on_mouse_down(pos):
    global nextstar
    global lines
    if nextstar < numberofstar:
        if stars[nextstar].collidepoint(pos):
            if nextstar:
                lines.append((stars[nextstar-1].pos,stars[nextstar].pos))
            nextstar+=1
    else:
        lines = []
        nextstar = 0
create()
pgzrun.go()
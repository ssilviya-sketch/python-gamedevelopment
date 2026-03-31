import pgzrun,random,time
HEIGHT = 600
WIDTH = 800
TITLE = "SATELLITE GAME"
sattelites = []
lines = []
nextsattelite = 0
starttime = 0
totaltime = 0
endtime = 0
numberofsattelites = 10
def create():
    global starttime
    for i in range(0,numberofsattelites):
        sattelite = Actor("sattelite")
        sattelite.pos = random.randint(50,(WIDTH-50)),random.randint(50,(HEIGHT-50))
        sattelites.append(sattelite)
    starttime = time.time()
def draw():
    global totaltime
    screen.blit("space",(0,0))
    number = 1
    for sattelite in sattelites:
        screen.draw.text(str(number),(sattelite.pos[0],sattelite.pos[1]+20))
        sattelite.draw()
        number+= 1
    

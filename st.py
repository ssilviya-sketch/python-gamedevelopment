import pgzrun
HEIGHT = 600
WIDTH = 800
TITLE = "SATELLITE GAME"
satellites = []
lines = []
nextsattelite = 0
starttime = 0
totaltime = 0
endtime = 0
numberofsattelites = 10
def draw():
    screen.blit("space",(0,0))

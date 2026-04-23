import pgzrun
HEIGHT = 700
WIDTH = 900
TITLE = "quiz master"
markbox = Rect(0,0,890,80)
questionbox = Rect(0,0,700,150)
timerbox = Rect(0,0,150,150)
answerbox1 = Rect(0,0,300,150)
answerbox2 = Rect(0,0,300,150)
answerbox3 = Rect(0,0,300,150)
answerbox4 = Rect(0,0,300,150)
skipbox = Rect(0,0,150,330)
score = 0
timeleft = 10
questionfile = "question.txt"
markmessage =  " "
game_over = False
answerboxes = [answerbox1,answerbox2,answerbox3,answerbox4]
questions = []
questioncount = 0
questionindex = 0
#move_ip standds fot inplace move if you want to move horizontaly you will change the x cordinates if you want to move it verticaly you whil change the y cordinates
markbox.move_ip(0,0)
questionbox.move_ip(20,100)
timerbox.move_ip(700,100)
answerbox1.move_ip(20,270)
answerbox2.move_ip(370,270)
answerbox3.move_ip(20,450)
answerbox4.move_ip(370,450)
skipbox.move_ip(700,270)
def draw():
    global markmessage
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(markbox,"white")
    screen.draw.filled_rect(questionbox,"blue")
    screen.draw.filled_rect(timerbox,"red")
    screen.draw.filled_rect(skipbox,"yellow")
    for answer_box in answerboxes:
        screen.draw.filled_rect(answer_box,"orange")
    markmessage = "Welcome to quizmaster"
    markmessage = markmessage+f"Q:{questionindex}of{questioncount}"
    screen.draw.textbox(markmessage,markbox,"white")
    screen.draw.textbox(str(timeleft),timerbox,"white")
    screen.draw.textbox(questions[0].strip(),questionbox,"white")
    screen.draw.textbox("skip",skipbox,"white")
    index = 1
    for answer_box in answerboxes:
        screen.draw.textbox(questions[index].strip(),answer_box,"white")
        
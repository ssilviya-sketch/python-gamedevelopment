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
markmessage =  " "
gameover = False
answerboxes = [answerbox1,answerbox2,answerbox3,answerbox4]
questions = []
question = []
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
    screen.draw.text(markmessage,(20,20), color = "orange", fontsize = 30)
    screen.draw.text(str(timeleft),(740,140),color = "white",fontsize = 30)
    screen.draw.text("skip",(740,400),color = "black")
    if question:
        screen.draw.text(question[0],(40,130),color = "white",fontsize = 35)
        screen.draw.text(question[1],(50,320),color = "white",fontsize = 35)
        screen.draw.text(question[2],(400,320),color = "white",fontsize = 35)
        screen.draw.text(question[3],(50,500),color = "white",fontsize = 35)
        screen.draw.text(question[4],(400,500),color = "white",fontsize = 35)
def update():
    movemark()
def movemark():
    markbox.x = markbox.x-2
    if markbox.right < 0:
        markbox.left = WIDTH  
def read_question_file():
    global questioncount,questions
    with open("question.txt" , "r") as file:
        for i in file:
            questions.append(i.strip())
    questioncount = len(questions)

def read_next_question():
    global questionindex
    questionindex+=1
    if questions:       
        return questions.pop(0).split(",")
    return None
def on_mouse_down(pos):
    index = 1 
    for box in answerboxes:
        if box.collidepoint(pos):
            if index == int(question[5]):
                correctanswer()
            else:
                game_over()
        index+=1
    if skipbox.collidepoint(pos):
        skip_question()
def correctanswer():
    global score,question,timeleft,questions
    score+=1
    if questions:
        question = read_next_question()
        timeleft = 10
    else:
        game_over()
def game_over():
    global question,timeleft,gameover
    message = f"Game over u got {score} questions correct" 
    question = [message,"-","-","-","-",5]
    timeleft = 0
    gameover = True
def skip_question():
    global question,timeleft
    if questions and not gameover:
        question = read_next_question()
        timeleft = 10
    else:
        game_over()
def update_timeleft():
    global timeleft
    if timeleft:
        timeleft-=1
    else:
        game_over()
read_question_file()
question = read_next_question()
clock.schedule_interval(update_timeleft,1)
pgzrun.go()                              

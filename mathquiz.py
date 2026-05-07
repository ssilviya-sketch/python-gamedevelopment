import pgzrun
HEIGHT = 700
WIDTH = 900
TITLE = "Math quiz"
markbox = Rect(0,0,890,80)
questionbox = Rect(0,0,700,150)
timerbox = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skipbox = Rect(0,0,150,330)
score = 0
timeleft = 10
markmessage =  " "
gameover = False
answerboxes = [answer_box1,answer_box2,answer_box3,answer_box4]
questions = []
questioncount = 0
questionindex = 0
markbox.move_ip(0,0)
questionbox.move_ip(20,100)
timerbox.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skipbox.move_ip(700,270)
def draw():
    global markmessage
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(markbox,"orange")
    screen.draw.filled_rect(questionbox,"yellow")
    screen.draw.filled_rect(timerbox,"blue")
    screen.draw.filled_rect(skipbox,"White")
    for answer_box in answerboxes:
        screen.draw.filled_rect(answer_box,"yellow")
    markmessage = "Welcome to the mathquiz"
    markmessage = markmessage+f"Q:{questionindex}of{questioncount}"
    screen.draw.text(markmessage,(20,20),color = "orange", fontsize = 30)
    screen.draw.text(str(timeleft),(740,140),color = "white", fontsize = 30)
    screen.draw.text("skip",(740,400),color = "black", fontsize = 30)
    if question:
        screen.draw.text(question[0],(40,130),color = "black",fontsize = 35)
        screen.draw.text(question[1],(50,320),color = "black",fontsize = 35)
        screen.draw.text(question[2],(400,320),color = "black",fontsize = 35)
        screen.draw.text(question[3],(50,500),color = "black",fontsize = 35)
        screen.draw.text(question[4],(400,500),color = "black",fontsize = 35)
def update():
    movemark()
def movemark():
    markbox.x = markbox.x-2
    if markbox.right < 0:
        markbox.left = WIDTH 
def read_question_file():
    global questioncount,questions
    with open("mathquiz.txt" , "r") as file:
        for i in file:
            questions.append(i.strip())
    questioncount = len(questions)
def read_next_question():
    global questionindex
    questionindex+=1
    return questions.pop(0).split(",")
def on_mouse_down(pos):
    index = 1 
    for box in answerboxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
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
    message = f"Game over u have gotten {score} questions correct" 
    question = [message,"-","-","-","-",5]
    time_left = 0
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
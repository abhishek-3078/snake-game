from tkinter import*
import random
import time 
from playsound import playsound
import os
from PIL import Image,ImageTk

FOOD=10
SNAKE_LENGTH = 2
SIZE = 25
SNAKE_COLOR = "RED"
SPEED=100
HEIGHT=600
WIDTH=600
THEME="#7bff00"
root=Tk()
root.geometry(f"{HEIGHT}x{HEIGHT}-200+10")
root.resizable(False,False)
# createFrame(root)

class Snake:
    def __init__(self):
        self.bodyLength = SNAKE_LENGTH
        self.coordinates = [[250,250],[(250+SIZE),250]]
        # self.coordinates = [[250,250],[0,]]
        self.bodyParts = []
        
        for x,y in self.coordinates:
            bodyPart = canvas.create_rectangle(x,y,x+SIZE,y+SIZE,fill=SNAKE_COLOR,tag="snake")
            self.bodyParts.append(bodyPart)

class multiSnake:
    def __init__(self, player):
        self.player = player
        self.bodyLength = SNAKE_LENGTH
        self.coordinates = [[250, 250], [(250 + SIZE), 250]]
        self.bodyParts = []
        
        for x, y in self.coordinates:
            bodyPart = multi_canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=SNAKE_COLOR, tag=f"snake{player}")
            self.bodyParts.append(bodyPart)
multiCountFood=1
class multiFood:
    def __init__(self):
        global multiCountFood
        multiCountFood+=1
        x = random.randint(0, WIDTH // SIZE - 1) * SIZE
        y = random.randint(0, HEIGHT // SIZE - 1) * SIZE
        self.coordinates = [x, y]
        self.Foodmulti_canvas = multi_canvas.create_oval(x, y, x + SIZE, y + SIZE, fill="white", tag="food")


countFood = 0 
class Food:
    def __init__(self):
        global countFood
        countFood += 1
        # x=random.randint(0,(WIDTH-SIZE-100)/SIZE)*SIZE
        # y=random.randint(0,(HEIGHT-SIZE-100)/SIZE)*SIZE
        x=random.randint(0,WIDTH//SIZE-1)*SIZE
        y=random.randint(0,HEIGHT//SIZE-1)*SIZE
        # print(x,y)
        self.coordinates=[x,y]

        self.FoodCanvas=canvas.create_oval(x,y,x+SIZE,y+SIZE,fill="green",tag="food")

class BigFood:
    def __init__(self,canvas):
        x = random.randint(0,WIDTH//SIZE-1)*SIZE
        y = random.randint(0,HEIGHT//SIZE-1)*SIZE
        # print(x,y)
        self.coordinates=[x,y]
        self.FoodCanvas=canvas.create_oval(x,y,(x+SIZE),(y+SIZE),fill="cyan",tag="bigfood")  


# TODO:create next_move
isbigfood=True


def storeHighScore():
    f=open(f"snakeGame_high_score{returnMode()}.txt","a")
    f.close()
    f=open(f"snakeGame_high_score{returnMode()}.txt","r")
# f.read() has string return type
    data=f.read()                
    f.close()

    if(data==''):
        f=open(f"snakeGame_high_score{returnMode()}.txt","w")
        f.write(str(score))
        f.close()
    elif(score>int(data)):
        f=open(f"snakeGame_high_score{returnMode()}.txt","w")
        point=str(score)
        f.write(str(point))
        f.close()

def returnToMenu(player=1):
    print("ended")
    if(player==2):
        multi_f3.pack_forget()
        multi_f3.pack_forget()
        multi_f1.pack_forget()
        start()
        return
    f3.pack_forget()
    f1.pack_forget()
    start()
    
#Game_Over
def game_over(players=1):
    # playsound("gameover.mp3")
    global Mode,Players
    Mode="medium";Players=2
    if(players==2):
        multi_canvas.delete(ALL)
        multi_canvas.create_text(WIDTH/2,100,font="Verdana 30 bold",text=f'{"Red WON!!!" if (score1>score2)  else  "Green WON!!!" if(score2>score1) else "Draw"} ',fill="red" if(score1>score2) else "green")
        multi_canvas.create_text(WIDTH/2,((2*HEIGHT)/3),font="Verdana 15 bold",text=f"Red Score:{score1}",fill="red")
        multi_canvas.create_text(WIDTH/2,((2*HEIGHT)/3+50),font="Verdana 15 bold",text=f"Green Score:{score2}",fill="red")
        multi_canvas.create_text(WIDTH / 2, HEIGHT / 2, font="Verdana 40 bold", text="GAME OVER", fill="red")
        returnBtn=Button(multi_f3,text="Back To Menu",command=lambda:returnToMenu(2),fg="White",bg="green",cursor="hand2").place(x=250,y=500)
        

    presentScore = score
    storeHighScore()
    f=open(f"snakeGame_high_score{returnMode()}.txt","r")
    # f.read() has string return type
    high_score = f.read()                
    f.close()
    canvas.delete(ALL)
    canvas.create_text(WIDTH/2,HEIGHT/2,font="Verdana 40 bold",text="GAME OVER",fill="red")
    canvas.create_text(WIDTH/3,((2*HEIGHT)/3),font="Verdana 15 bold",text=f"YourScore:{score}",fill="red")
    canvas.create_text(((2*WIDTH)/3),((2*HEIGHT)/3),font="Verdana 15 bold",text=f"HighestScore:{high_score}",fill="red")
    if(presentScore == int(high_score)):
        canvas.create_text(((WIDTH)/2),((HEIGHT)/3),font="Verdana 25 bold",text=f"Congratulations",fill="green")

    returnBtn=Button(f3,text="Back To Menu",command=returnToMenu,fg="White",bg="green",cursor="hand2").place(x=250,y=400)


        

# update score
def updateScore(a=0):
    global score 
    if(a == 0):
        score += 1
    else:
        score += 5

    l["text"]=f"Score:{score}"
    # threading.Thread(target=playsound,args=("./audios/eating.mp3",),daemon=True).start()
    # playsound("gameover.mp3")



def Binding():
    root.bind("<Left>",lambda event:change_direction("L"))
    root.bind("<Right>",lambda event:change_direction("R"))
    root.bind("<Up>",lambda event:change_direction("U"))
    root.bind("<Down>",lambda event:change_direction("D"))


def Next_Move(snake,food):
    global isbigfood,countFood,bigfood
    
    # print(countFood)
    x,y=snake.coordinates[0]
    # print(x,y)
    if(direction=="L"):
        x=x-SIZE 
    elif(direction=="R"):
        x=x+SIZE 
    elif(direction=="U"):
        y-=SIZE 
    elif(direction=="D"):
        y+=SIZE
    
    snake.coordinates.insert(0,[x,y])
    snakeCanvas=canvas.create_rectangle(x,y,x+SIZE,y+SIZE,fill="red")
    snake.bodyParts.insert(0,snakeCanvas)

    if(x==food.coordinates[0] and y==food.coordinates[1]):
        canvas.delete(food.FoodCanvas)
        del food

        food=Food()
        updateScore()
    elif(isbigfood==True and x == bigfood.coordinates[0] and y == bigfood.coordinates[1]):
        canvas.delete(bigfood.FoodCanvas)
        # del bigfood 
        isbigfood=False
        countFood+=1
        updateScore(1)
    else:
        canvas.delete(snake.bodyParts[-1])
        snake.bodyParts.pop()
        snake.coordinates.pop()
    # print(isbigfood) 
    if(countFood % 10 == 0 and isbigfood==False):
            bigfood = BigFood(canvas)
            isbigfood=True
    if(check_collision(snake)):
        game_over()
        
    else:
        root.after(SPEED,Next_Move,snake,food)

def returnMode():
    if(SPEED == 200):
        return "Easy"
    elif(SPEED == 100):
        return "Medium"
    else:
        return "Hard"




def multi_Next_Move():
    global multi_direction1, multi_direction2, multi_canvas,bigfood

    x1, y1 = snake1.coordinates[0]
    x2, y2 = snake2.coordinates[0]

    if multi_direction1 == "L":
        x1 = x1 - SIZE
    elif multi_direction1 == "R":
        x1 = x1 + SIZE
    elif multi_direction1 == "U":
        y1 = y1 - SIZE
    elif multi_direction1 == "D":
        y1 = y1 + SIZE
    
    if multi_direction2 == "L":
        x2 = x2 - SIZE
    elif multi_direction2 == "R":
        x2 = x2 + SIZE
    elif multi_direction2 == "U":
        y2 = y2 - SIZE
    elif multi_direction2 == "D":
        y2 = y2 + SIZE
    
    global isbigfood,multiCountFood

    snake1.coordinates.insert(0, [x1, y1])
    snake2.coordinates.insert(0, [x2, y2])

    snakemulti_canvas1 = multi_canvas.create_rectangle(x1, y1, x1 + SIZE, y1 + SIZE, fill="red", tag=f"snake{snake1.player}")
    snakemulti_canvas2 = multi_canvas.create_rectangle(x2, y2, x2 + SIZE, y2 + SIZE, fill="green", tag=f"snake{snake2.player}")

    snake1.bodyParts.insert(0, snakemulti_canvas1)
    snake2.bodyParts.insert(0, snakemulti_canvas2)
    global food
    if x1 == food.coordinates[0] and y1 == food.coordinates[1]:
        multi_canvas.delete(food.Foodmulti_canvas)
        food.coordinates.pop()
        multi_canvas.delete(snake2.bodyParts[-1])
        snake2.bodyParts.pop()
        # food = Food()
        food=multiFood()
        multi_update_score(1,1)

    elif x2 == food.coordinates[0] and y2 == food.coordinates[1]:
        multi_canvas.delete(food.Foodmulti_canvas)
        food.coordinates.pop()
        multi_canvas.delete(snake1.bodyParts[-1])
        snake1.bodyParts.pop()
        # food = Food()
        food=multiFood()
        multi_update_score(2,1)
    elif(isbigfood==True and x1 == bigfood.coordinates[0] and y1 == bigfood.coordinates[1]):
        multi_canvas.delete(bigfood.FoodCanvas)
        # del bigfood 
        isbigfood=False
        multiCountFood+=1
        multi_update_score(1,5)
    elif(isbigfood==True and x2 == bigfood.coordinates[0] and y2 == bigfood.coordinates[1]):
        multi_canvas.delete(bigfood.FoodCanvas)
        # del bigfood 
        isbigfood=False
        multiCountFood+=1
        multi_update_score(2,5)
    else:
        multi_canvas.delete(snake1.bodyParts[-1])
        multi_canvas.delete(snake2.bodyParts[-1])
        snake1.bodyParts.pop()
        snake2.bodyParts.pop()
        snake1.coordinates.pop()
        snake2.coordinates.pop()

    if(multiCountFood % 10 == 0 and isbigfood==False):
            bigfood = BigFood(multi_canvas)
            isbigfood=True

    # if(check_collision(snake1)):
    #     multi_canvas.delete(snake1)
    global remainingPlayer
    if(remainingPlayer==[1,1]):
        if(check_collision(snake1)):
            multi_canvas.delete(snake1)
            remainingPlayer=[0,1]
        if(check_collision(snake2)):
            multi_canvas.delete(snake2)
            remainingPlayer=[1,0]
    if((remainingPlayer==[0,1] and check_collision(snake2)) or (remainingPlayer==[1,0] and check_collision(snake1))):
        game_over(2)
        return
        

    if remainingPlayer==0:
        game_over(2)

    else:
        root.after(SPEED, multi_Next_Move)


def multi_update_score(player,score):
    global score1, score2

    if player == 1:
        score1 += score
        l1["text"] = f"Red Score: {score1}"
    elif player == 2:
        score2 += score
        l2["text"] = f"Green Score: {score2}"

def multi_Binding():
    root.bind("<Left>", lambda event: multi_change_direction(1, "L"))
    root.bind("<Right>", lambda event: multi_change_direction(1, "R"))
    root.bind("<Up>", lambda event: multi_change_direction(1, "U"))
    root.bind("<Down>", lambda event: multi_change_direction(1, "D"))
    root.bind("<KeyPress-a>", lambda event: multi_change_direction(2, "L"))
    root.bind("<KeyPress-d>", lambda event: multi_change_direction(2, "R"))
    root.bind("<KeyPress-w>", lambda event: multi_change_direction(2, "U"))
    root.bind("<KeyPress-s>", lambda event: multi_change_direction(2, "D"))

def multi_change_direction(player, newDirection):
    global multi_direction1, multi_direction2

    if player == 1:
        if multi_direction1 == "U" and newDirection != "D":
            multi_direction1 = newDirection
        elif multi_direction1 == "D" and newDirection != "U":
            multi_direction1 = newDirection
        elif multi_direction1 == "L" and newDirection != "R":
            multi_direction1 = newDirection
        elif multi_direction1 == "R" and newDirection != "L":
            multi_direction1 = newDirection
    elif player == 2:
        if multi_direction2 == "U" and newDirection != "D":
            multi_direction2 = newDirection
        elif multi_direction2 == "D" and newDirection != "U":
            multi_direction2 = newDirection
        elif multi_direction2 == "L" and newDirection != "R":
            multi_direction2 = newDirection
        elif multi_direction2 == "R" and newDirection != "L":
            multi_direction2 = newDirection

def check_collision(snake):
    x, y = snake.coordinates[0]
    
    if (x < 0 or x >= WIDTH) or (y < 0 or y >= HEIGHT):
        return True
    
    for x1, y1 in snake.coordinates[1:]:
        if x1 == x and y1 == y:
            return True
    
    return False



multi_f1 = Frame(root, width=WIDTH)
score1 = 0
score2 = 0
l1 = Label(multi_f1, text=f"Red Score: {score1}", font="Verdana 18 bold")
l1.grid(row=0, column=0)
l2 = Label(multi_f1, text=f"Green Score: {score2}", font="Verdana 18 bold")
l2.grid(row=0, column=1)


def multi_countdown(seconds):
    if seconds > 0:
        timeLabel['text'] = seconds
        root.after(1000, multi_countdown, seconds - 1)
    else:
        timeLabel['text'] = "Go!"
        multi_f2.pack_forget()

        multi_f1.pack()
        multi_f3.pack()
        multi_Next_Move()

def setSingleUser():
    global isbigfood
    f1.pack()
    f2.pack()
    welcomeFrame.pack_forget()
    isbigfood=False
    countdown(1)


def setMulti():
    print("hello multi")
    global multi_f2,multi_f3,timeLabel,multi_direction1,multi_direction2
    global multi_canvas,remainingPlayer
    global snake1,snake2,food,bigfood,isbigfood

    remainingPlayer=[1,1]

    multi_f2 = Frame(root, height=550, width=600, bg="black")
    multi_f2.pack_propagate(False)
    Label(multi_f2,text="RED - arrows" ,font="Verdana 15 bold", bg="black",fg="red",relief=RAISED).place(relx=0.4,y=100)
    Label(multi_f2,text="Green - W A S D",font="Verdana 15 bold", bg="black",fg="green",relief=RAISED).place(relx=0.37,y=140)
    welcomeFrame.pack_forget()
    multi_f2.pack()

    timeLabel = Label(multi_f2, text="", font="Verdana 40 bold", bg="black", fg="white")
    timeLabel.place(relx=0.45, rely=0.45)

    multi_f3 = Frame(root, height=550, width=600, bg="black")
    multi_f3.pack_propagate(False)

    multi_canvas = Canvas(multi_f3, height=HEIGHT, width=WIDTH, bg="black")
    multi_canvas.pack()

    snake1 = multiSnake(1)
    snake2 = multiSnake(2)
    food = multiFood()
    isbigfood=False
    # bigfood=BigFood(multi_canvas)
    multi_direction1 = "R"
    multi_direction2 = "L"

    multi_Binding()
    
    multi_countdown(2)





############################################################################
def change_direction(newDirection):
    global direction
    if(direction == "U" and newDirection != "D"):
        direction = newDirection
            
    elif(direction == "D" and newDirection != "U"):
        direction = newDirection
        
    elif(direction == "L" and newDirection != "R"):
        direction = newDirection
            
    elif(direction == "R" and newDirection != "L"):
        direction = newDirection
    
    return direction

def check_collision(snake):
    x,y = snake.coordinates[0]
    
    if (x < 0 or x >= WIDTH) or (y<0 or y >= HEIGHT):
            # print(x,y)
            return True
    
    for x1,y1 in snake.coordinates[1:]:
        if x1 == x and y1 == y:
            return True
    
    return False   



#@main


# Import module
welcomeFrame = Frame(root,height=600,width=600,bg=THEME)
welcomeFrame.pack_propagate(False)

# Adjust size
def setMode(mode):

    global SPEED,Mode
    Mode=mode
    if(mode=="easy"):
        SPEED=200
        btn1["bg"]="red"
        btn2["bg"]="White"
        btn3["bg"]="white"
    elif(mode=="medium"):
        SPEED=100
        btn1["bg"]="white"
        btn2["bg"]="red"
        btn3["bg"]="white"
    else:
        SPEED=80
        btn1["bg"]="white"
        btn2["bg"]="white"
        btn3["bg"]="red"
    # startGame()
    

status = 1
def showHighScore():
    global status
    status *= -1
    data1,data2,data3 = 0,0,0
    if(os.path.isfile("snakeGame_high_scoreEasy.txt")):
        f1=open(f"snakeGame_high_scoreEasy.txt","r")
        data1 = f1.read()
    if(os.path.isfile("snakeGame_high_scoreMedium.txt")):
        f2=open(f"snakeGame_high_scoreMedium.txt","r")
        data2 = f2.read()
    if(os.path.isfile("snakeGame_high_scoreHard.txt")):
        f3=open(f"snakeGame_high_scoreHard.txt","r")
        data3 = f3.read()
    if(status == -1):
        global labelEasyHighScore
        labelEasyHighScore = Label(welcomeFrame,text=f"EasyMode : {data1}",font="Verdana 10 bold",relief="raised",bg="cyan").place(x=90,y=440)
        global labelMediumHighScore
        labelMediumHighScore = Label(welcomeFrame,text=f"MediumMode : {data2}",font="Verdana 10 bold",relief="raised",bg="cyan").place(x=80,y=460)
        global labelHardHighScore
        labelHardHighScore = Label(welcomeFrame,text=f"HardMode : {data3}",font="Verdana 10 bold",relief="raised",bg="cyan").place(x=90,y=480)
    if(status == 1):
          coverHighScore = Frame(welcomeFrame,width=160,height=120,bg=THEME).place(x=80,y=430)


def start():
    global Players,Mode,score1,score2
    score1=0
    score2=0
    Players=1;Mode="medium"
    print(Players,Mode)
    btn5["bg"]="white"
    btn4["bg"]="white"
    btn1["bg"]="white"
    btn2["bg"]="white"
    btn3["bg"]="white"
    welcomeFrame.pack()
    createCanvas()


def createCanvas():
    global canvas,f3,snake,food,bigfood
    f3=Frame(root,height=550,width=600,bg="black")
    f3.pack_propagate(False)
    canvas=Canvas(f3,height=HEIGHT,width=WIDTH,bg="black")
    canvas.pack()
    snake=Snake()
    food=Food()
    # bigfood=BigFood(canvas)
      

def countdown(seconds):
    
    if seconds > 0:
        timeLabel['text'] = seconds
        root.after(1000, countdown, seconds-1)
    else:
        timeLabel['text'] = "Go!"
        f2.pack_forget()
        f3.pack()
        Next_Move(snake,food)


def startGame():
    global Players,Mode
    root.title(f"Snake Game : Difficulty->{Mode} :: Players->{Players}")
    print(Players,Mode) 
    #TODO:need to change
    # Players=2
    # Mode=2
    if(Players!=0 and Mode!=0):
        print("hello befores df")
        (setSingleUser()) if (Players==1) else setMulti()
    

def MultiUser(players):
    global Players
    Players=players

    # startGame()
    if(players==1):
        btn4["bg"]="red"
        btn5["bg"]="white"
    else:
        btn5["bg"]="Red"
        btn4["bg"]="white"
        
def resetEasyHighScore():
    if(os.path.isfile("snakeGame_high_scoreEasy.txt")):
        f1=open(f"snakeGame_high_scoreEasy.txt","w")
        f1.write("0")

def resetMediumHighScore():
    if(os.path.isfile("snakeGame_high_scoreMedium.txt")):
        f2=open(f"snakeGame_high_scoreMedium.txt","w")
        f2.write("0")
def resetHardHighScore():
    if(os.path.isfile("snakeGame_high_scoreHard.txt")):
        f3=open(f"snakeGame_high_scoreHard.txt","w")
        f3.write("0")


status2 = 1
def resetHighScore():
    global status2
    status2 *= -1
    if(status2 == -1):
        resetEasyHighScoreBtn = Button(welcomeFrame,text="ResetEasy",relief="groove",bg="red",font="Verdana 10 bold",cursor="hand2",command=resetEasyHighScore).place(x=420,y=440)
        resetMediumHighScoreBtn = Button(welcomeFrame,text="ResetMedium",relief="groove",bg="red",font="Verdana 10 bold",cursor="hand2",command=resetMediumHighScore).place(x=410,y=470)
        resetHardHighScoreBtn = Button(welcomeFrame,text="ResetHard",relief="groove",bg="red",font="Verdana 10 bold",cursor="hand2",command=resetHardHighScore).place(x=420,y=500)
    else:
        coverReset = Frame(welcomeFrame,width=150,height=100,bg=THEME).place(x=410,y=430)


modeFrame=Frame(welcomeFrame,bg="yellow",height=155,width=155,relief="raised",borderwidth=4).place(x=387,y=200)
difficultyFrame=Frame(welcomeFrame,bg="pink",height=155,width=155,relief="raised",borderwidth=4).place(x=60,y=200)

lb1 = Label(welcomeFrame,text="SNAKE GAME",font="Verdana 50 bold",bg=THEME,fg="red",relief="raised",borderwidth=5).place(x=50,y=20)
lb2 = Label(difficultyFrame,text="DIFFICULTY",font="Verdana 15 bold",bg="pink",fg="Black").place(x=68,y=210)
btn1 = Button(difficultyFrame,relief="solid",text="Easy",cursor="hand2",font="Verdana 10 bold",command=lambda : setMode("easy"))
btn1.place(x=110,y=240)
btn2 = Button(difficultyFrame,relief="solid",text="Medium",cursor="hand2",font="Verdana 10 bold",command=lambda : setMode("medium"))
btn2.place(x=100,y=270)
btn3 = Button(difficultyFrame,relief="solid",text="Hard",cursor="hand2",font="Verdana 10 bold",command=lambda : setMode("hard"))
btn3.place(x=110,y=300)


lb3 = Label(modeFrame,text="MODE",font="Verdana 15 bold",bg="yellow",fg="black").place(x=425,y=210)
btn4 = Button(modeFrame,relief="solid",text="Single user",cursor="hand2",font="Verdana 10 bold",command=lambda : MultiUser(1))
btn4.place(x=415,y=240)
btn5 = Button(modeFrame,relief="solid",text="Multi user",cursor="hand2",font="Verdana 10 bold",command=lambda : MultiUser(2))
btn5.place(x=420,y=270)

btn6 = Button(welcomeFrame,text="High Score",cursor="hand2",activebackground="red",font="Verdana 10 bold",relief="raised",borderwidth=3,command=showHighScore).place(x=90,y=400)
btn7 = Button(welcomeFrame,text="Reset High Score",cursor="hand2",activebackground="red",font="Verdana 10 bold",relief="raised",borderwidth=3,command=resetHighScore).place(x=395,y=400)

img = ImageTk.PhotoImage(Image.open("img/snake9.png"))
lb4 = Label(welcomeFrame, image = img,relief="solid",borderwidth=0)
lb4.place(x=215, y=135)

lb5 = Label(welcomeFrame,text="DEVELOPED BY - @Aman  @Abhishek  @Amit" ,font="Verdana 14 bold",bg=THEME,fg="blue",relief="raised",borderwidth=3).place(x=55,y=560)

startbtn = Button(welcomeFrame,relief="solid",text="Start Game",activebackground="red",font="Verdana 12 bold",bg="cyan",fg="red",cursor="hand2",command=startGame).place(relx=0.41,rely=0.75)


f1=Frame(root,width=WIDTH)
score=0
l=Label(f1,text=f"Score:{score}",font="Verdana 18 bold")
l.grid(row=0,column=0)


root.update()

HEIGHT=550


f2=Frame(root,height=550,width=600,bg="black")
f2.pack_propagate(False)


timeLabel=Label(f2,text="",font="Verdana 40 bold",bg="black",fg="white")
timeLabel.place(relx=0.45,rely=0.45)



start()
Binding()

direction="R"


root.mainloop()

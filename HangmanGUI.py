from tkinter import *
from pyswip import Prolog
import random



chances = 6
letterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
vocabList = ['software','security','engineering','programmer','algorithm','data','network','logic']

global vocabStr,AIGuess,UserAns, AiChances
w=600
h=400
# Load Prolog file
#prolog = Prolog()
#prolog.consult("hangman")

# Draw the hangman if the AI guess the wrong letter
def drawHangman():
    print("No")
    hangmanCanvas.delete()
    global chances
    radius = 30
    #draw head
    if chances == 6:
        hangmanCanvas.create_oval(200-radius, 100-radius,200+radius, 100+radius)
        chances -= 1
    #draw body
    if chances == 5:
        hangmanCanvas.create_line(200,130,200,250)
        chances -= 1
    #draw first arm
    if chances == 4:
        hangmanCanvas.create_line(170,200,200,150)
        chances -= 1
    #draw second arm
    if chances == 3:
        hangmanCanvas.create_line(230,200,200,150)
        chances -= 1
    #draw first leg
    if chances == 2:
        hangmanCanvas.create_line(200,250,230,300)
        chances -= 1
    #draw second leg
    if chances == 1:
        hangmanCanvas.create_line(200,250,170,300)
        chances -= 1
        
        
     
#Start game
def startGame():
    hangmanCanvas.create_line(10,w-10,50,w-10)
    hangmanCanvas.create_line(30,w-10,30,50)
    hangmanCanvas.create_line(30,50,200,50)
    hangmanCanvas.create_line(200,50,200,70)
    input = inputText.get("1.0","end-1c")
    print(input)
    print(vocabGenerate())
    print(guessing())
    
# Answer the AI answer
def answerAI():
    print("Correct!")

# AI will guess the letter
def guessing():
    guessletter = random.choice(letterList)
    return guessletter

# Generate the vocabulary
def vocabGenerate():
    #vocab = random.choice(Prolog.consult)
    input = inputText.get("1.0","end-1c")
    UserAns = random.choice(vocabList)
    vocabStr = "_ "*len(UserAns)
    print(UserAns)
    if len(UserAns) == input:
        print(vocabStr)
    else:
        print("Length does not match")
    
    return vocabStr

# UI for the program
ws = Tk()
ws.title("Hangman")
ws.geometry("1280x720")

ws['bg']='#FF9CD1'

title = Label(ws,text="Enter the number of letters in your word:",font=('Arial',16))
title.pack()

inputText = Text(ws,height=2,width=5)
inputText.pack()

startbtn = Button(ws,text="Start",height=1,width=5,font=('Arial',16),command=startGame)
startbtn.pack()

guesswordLabel = Label(ws,text="Word: ",font=('Arial',16))
guesswordLabel.pack()

chanceLabel = Label(ws,text="Chances: ",font=('Arial',16))
chanceLabel.pack()

chanceNum = Entry(ws)
chanceNum.insert(END,chances)
chanceNum.pack()

hangmanCanvas = Canvas(ws,width=w,height=h)
hangmanCanvas.pack()

AiAsk = "Is it: "+guessing()

QuestionLabel = Label(ws,text=AiAsk,font=('Arial',16))
QuestionLabel.pack()

yesBtn = Button(ws,text="Yes",height=1,width=5,font=('Arial',16),bg='green',command=answerAI)
yesBtn.pack()

noBtn = Button(ws,text="No",height=1,width=5,font=('Arial',16),bg='red',fg='white',command=drawHangman)
noBtn.pack()

ws.mainloop()

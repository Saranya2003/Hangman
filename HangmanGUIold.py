from tkinter import *
from pyswip import Prolog
import random
from tkinter import messagebox

chances = 6
letterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
vocabList = ['software','security','engineering','programmer','algorithm','data','network','logic','computer','hardware']
worngGuess = []
global vocabStr,AIGuess,UserAns, AiChances,guessletter,missedLetter

#Height and width of the UI
w=600
h=300

prolog = Prolog()
prolog.consult("hangman.pl")

# Draw the hangman if the AI guess the wrong letter
def drawHangman():
    hangmanCanvas.delete()
    global chances
    radius = 30
    chances -= 1

    
    guessletter = random.choice(letterList)
    missedBox.insert(END,guessletter+", ")

    #draw head
    if chances == 5:
        hangmanCanvas.create_oval(200-radius, 100-radius,200+radius, 100+radius)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)
        alphabetLabel.insert(END,guessletter)

        
    #draw body
    if chances == 4:
        hangmanCanvas.create_line(200,130,200,250)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)
        alphabetLabel.insert(END,guessletter)

    #draw first arm
    if chances == 3:
        hangmanCanvas.create_line(170,200,200,150)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)
        alphabetLabel.insert(END,guessletter)

    #draw second arm
    if chances == 2:
        hangmanCanvas.create_line(230,200,200,150)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)
        alphabetLabel.insert(END,guessletter)

    #draw first leg
    if chances == 1:
        hangmanCanvas.create_line(200,250,230,300)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)
        alphabetLabel.insert(END,guessletter)

    #draw second leg
    if chances == 0:
        hangmanCanvas.create_line(200,250,170,300)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)
        alphabetLabel.insert(END,"You lose")
        print("You lose")
    
    #No chances left
    if chances<0:
        messagebox.showerror("You lose","No chances to guess, You lose")
        
        
        
     
#Start game
def startGame():
    # Load Prolog file
    
    hangmanCanvas.create_line(10,w-10,50,w-10)
    hangmanCanvas.create_line(30,w-10,30,50)
    hangmanCanvas.create_line(30,50,200,50)
    hangmanCanvas.create_line(200,50,200,70)
    input = inputText.get("1.0","end-1c")


    b = prolog.query('name')

    
# Answer the AI answer
def answerAI():
    global vocabStr
    print("Correct!")
    guessletter = random.choice(letterList)
    alphabetLabel.insert(END,guessletter)
    
    

# AI will guess the letter
def guessing():
    guessletter = random.choice(letterList)
    alphabetLabel.insert(END,guessletter)
    return guessletter

# Generate the vocabulary
def vocabGenerate():
    #vocab = random.choice(Prolog.consult)
    #UserAns = random.choice(vocabList)
    #vocabStr = "_ "*len(UserAns)
    bquery = prolog.query("getVocab(Ans)")
    a = next(bquery)
    print(a['Ans'])
    vocabStr = a['Ans']
    #print(UserAns)
    inputText.insert(END,vocabStr)
    UserText.insert(END,vocabStr)
    #UserText.insert(END,UserAns)
    
    return vocabStr

# UI for the program
ws = Tk()
ws.title("Hangman")
ws.geometry("1280x720")

ws['bg']='#FF9CD1'

title = Label(ws,text="User answer: ",font=('Arial',16))
title.pack()

UserText = Text(ws,height=1,width=20)
UserText.pack()

startbtn = Button(ws,text="Start",height=1,width=5,font=('Arial',16),command=startGame)
startbtn.pack()

guesswordLabel = Label(ws,text="Word: ",font=('Arial',16))
guesswordLabel.pack()

inputText = Text(ws,height=1,width=20)
inputText.pack()

missedLabel = Label(ws,text="Missed Letter: ",font=('Arial',16))
missedLabel.pack()

missedBox = Text(ws,height=1,width=20)
missedBox.pack()

chanceLabel = Label(ws,text="Chances: ",font=('Arial',16))
chanceLabel.pack()

chanceNum = Entry(ws)
chanceNum.insert(END,chances)
chanceNum.pack()

hangmanCanvas = Canvas(ws,width=w,height=h)
hangmanCanvas.pack()

QuestionLabel = Label(ws,text="Is it: ",font=('Arial',16))
QuestionLabel.pack()

alphabetLabel = Text(ws,height=2,width=10)
alphabetLabel.pack()

yesBtn = Button(ws,text="Yes",height=1,width=5,font=('Arial',16),bg='green',command=answerAI)
yesBtn.pack()

noBtn = Button(ws,text="No",height=1,width=5,font=('Arial',16),bg='red',fg='white',command=drawHangman)
noBtn.pack()

ws.mainloop()

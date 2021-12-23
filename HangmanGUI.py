from tkinter import *
from pyswip import Prolog
import random

chances = 6
global words
# Load Prolog file
#prolog = Prolog()
#prolog.consult("hangman")

# List of hangman image
'''
img1= PhotoImage(file='1.png')
img2= PhotoImage(file='2.png')
img3= PhotoImage(file='3.png')
img4= PhotoImage(file='4.png')
img5= PhotoImage(file='5.png')
img6= PhotoImage(file='6.png')
img7= PhotoImage(file='7.png')'''

# Draw the hangman if the AI guess the wrong letter
def drawHangman():
    pass
     
#Start game
def startGame():
    pass
# Answer the AI answer
def answerAI():
    pass

# AI will guess the letter
def guessing():
    pass
# Generate the vocabulary
def vocabGenerate():
    pass
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

hangmanCanvas = Canvas(ws,width=600,height=400)
hangmanCanvas.pack()

QuestionLabel = Label(ws,text="Is it:",font=('Arial',16))
QuestionLabel.pack()

yesBtn = Button(ws,text="Yes",height=1,width=5,font=('Arial',16),bg='green')
yesBtn.pack()

noBtn = Button(ws,text="No",height=1,width=5,font=('Arial',16),bg='red',fg='white',command=drawHangman)
noBtn.pack()

ws.mainloop()

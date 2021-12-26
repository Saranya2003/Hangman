from tkinter import *
from pyswip import Prolog
import random
from tkinter import messagebox

letterList = ['a','b','c','e','h','i','k','n','o','p','r','s','t','u','w']
vocabList = ['hurt','pear','rain','crab','rose','wave','kite','bear','care','fast']
blankletter = []
wrongletter = []
wordinlist=[]
strusedletter = ""
chances = 9

#Height and width of the UI
w=600
h=400

prolog = Prolog()
prolog.consult("hangman.pl")

def wordsplit(word):
    return [char for char in word]
   
#Start game
def startGame():
    # Load Prolog file
    
    global guessletter, blankletter, strusedletter, vocabStr, wordinlist, chances, letterList
    letterList = ['a','b','c','e','h','i','k','n','o','p','r','s','t','u']
    blankletter = []
    wordinlist=[]
    wrongletter = []
    strusedletter = ""
    chances = 9
    hangmanCanvas.delete("all")
    inputText.delete('1.0',END)
    alphabetLabel.delete('1.0',END)
    UserText.delete('1.0',END)
    chanceNum.delete(0, 'end')
    missedBox.delete('1.0',END)
    chanceNum.insert(END,chances)
    QuestionLabel.config(text="Is it: ")

    
    input = inputText.get("1.0","end-1c")
    print(input)
    word = vocabGenerate()
    print("word is: ", word)
    wordinlist = wordsplit(word)
    print(wordinlist)
    for i in range(len(word)):
        blankletter.append('_')
        strusedletter=strusedletter+",_"
    inputText.insert(END,str(blankletter))
    guessletter = guessing()
    b = prolog.query('name("'+word+'",AnsList)')

# Draw the hangman if the AI guess the wrong letter
def drawHangman():
    global guessletter
    letter = guessletter
    hangmanCanvas.delete()
    global chances
    
    radius = 30
    chances -= 1
    print(chances)
    alphabetLabel.delete('1.0',END)
    wrongletter.append(letter)
    missedBox.insert(END,letter+", ")
    letterList.remove(guessletter)

    #draw a pole
    if chances == 8:
        guessletter = guessing()
        hangmanCanvas.create_line(30,w-10,30,50)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)

    #draw attic
    if chances == 7:
        guessletter = guessing()
        hangmanCanvas.create_line(30,50,200,50)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)

    #draw hanging part
    if chances == 6:
        guessletter = guessing()
        hangmanCanvas.create_line(200,50,200,70)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)

    #draw head
    if chances == 5:
        guessletter = guessing()
        hangmanCanvas.create_oval(200-radius, 100-radius,200+radius, 100+radius)
        
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)
        
    #draw body
    if chances == 4:
        guessletter = guessing()
        hangmanCanvas.create_line(200,130,200,250)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)

    #draw first arm
    if chances == 3:
        guessletter = guessing()
        hangmanCanvas.create_line(170,200,200,150)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)

    #draw second arm
    if chances == 2:
        guessletter = guessing()
        hangmanCanvas.create_line(230,200,200,150)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)

    #draw first leg
    if chances == 1:
        guessletter = guessing()
        hangmanCanvas.create_line(200,250,230,300)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)

    #draw second leg
    if chances == 0:
        guessletter = guessing()
        hangmanCanvas.create_line(200,250,170,300)
        chanceNum.delete(0, 'end')
        chanceNum.insert(END,chances)
        alphabetLabel.delete('1.0',END)
        alphabetLabel.insert(END,"AI lose")
    
    #No chances left
    if chances<0:
        messagebox.showerror("AI lose","No chances to guess, AI lose")
        
    
# Answer the AI answer
def answerAI():
    global vocabStr, guessletter
    for i in range(len(wordinlist)):
        if wordinlist[i] == guessletter:
            blankletter[i] = guessletter
    letterList.remove(guessletter)
    guessletter = random.choice(letterList)
    inputText.delete('1.0',END)
    inputText.insert(END,str(blankletter))
    alphabetLabel.delete('1.0',END)
    
    if str(blankletter)==str(wordinlist):
        QuestionLabel.config(text="Result:")
        alphabetLabel.insert(END,"AI win!!")
    else:
        
        alphabetLabel.insert(END,guessletter)
    
    

# AI will guess the letter
def guessing():
    guessletter = random.choice(letterList)
    alphabetLabel.insert(END,guessletter)
    return guessletter

# Generate the vocabulary
def vocabGenerate():
    bquery = prolog.query("getVocab(Ans)") # Use the given Function in Prolog
    a = next(bquery) #Filter the result
    vocabStr = a['Ans']
    
    UserText.insert(END,vocabStr)
    
    return vocabStr

# UI for the program
ws = Tk()
ws.title("Hangman")
ws.geometry("1280x940")

ws['bg']='#FF9CD1'

windowtitle = Label(ws,text="Hangman AI",font=('Arial',16))
windowtitle.pack()

startbtn = Button(ws,text="Start",height=1,width=5,font=('Arial',16),command=startGame)
startbtn.pack()

title = Label(ws,text="User answer: ",font=('Arial',16))
title.pack()

UserText = Text(ws,height=1,width=20,font=('Arial',16))
UserText.pack()

guesswordLabel = Label(ws,text="Word: ",font=('Arial',16))
guesswordLabel.pack()

inputText = Text(ws,height=2,width=40,font=('Arial',16))
inputText.pack()

missedLabel = Label(ws,text="Missed Letter: ",font=('Arial',16))
missedLabel.pack()

missedBox = Text(ws,height=1,width=20,font=('Arial',16))
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

alphabetLabel = Text(ws,height=2,width=10,font=('Arial',16))
alphabetLabel.pack()

yesBtn = Button(ws,text="Yes",height=1,width=5,font=('Arial',16),bg='green',command=answerAI)
yesBtn.pack()



noBtn = Button(ws,text="No",height=1,width=5,font=('Arial',16),bg='red',fg='white',command=drawHangman)
noBtn.pack()

ws.mainloop()

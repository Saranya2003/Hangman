import random
from tkinter import * #Import tkinter
 
# Find if pressed letter is in word or not, update screen
def keyPressed(event):
    #modifying below global variable locally
    global count, latestStr, missedLetters
 
    current=event.char #get the pressed key
 
    # Check for non-letters
    if not current.isalpha():
        print("\t",current," is not a letter.")
        return
 
    # Check if current letter is already guessed and missed
    if current in missedLetters:
        print("\t",current," is already in missed list")
        return # Do nothing
 
    # Check if current alphabet is in original word
    if current in word:
        # Remove spaces if any in latestStr string
        # Convert it into a list
        latestStr_list=list(latestStr.replace("",""))
        for i in range(0,len(word)): #Traverse list
            # Check if current letter exist in word
 
            if word[i]==current:
                # Add the current alphabet in list
                latestStr_list[i] = word[i]
        latestStr = ''.join(latestStr_list)#Append space
 
        # Prepare message to display on screen
        msg1="Guess a word: "+ latestStr
        msg2="Missed letters: " +missedLetters
 
    else: # Current alphabet is not in original word
        missedLetters+=(current+'')#Add letter to missed
        count += 1 #Increment number of attempts
 
        if count < 7: #Attemtpt finished
            # Prepare message to display on screen
            msg1="Guess a word: "+latestStr
            msg2="Missed letter: "+missedLetters
        else: #Finished all attempts
            # Display failure message, check for continue?
            msg1="Sorry! The word is: "+word
            msg2="To continue the game, press ENTER"
 
    if'*' not in latestStr: #Finished with success
        # Display success message, check for 1 more round
        msg1="Congrts! The word is: "+word
        msg2="To continue the game, press ENTER"
 
    # Draw the latest hangman, display message and return
    draw(count,msg1, msg2)
    return
 
# Draw the latest hangman
def draw(count,msg1,msg2):
    canvas.delete("hang") # Delete previous picture, if any
    size=400 # Screen size
 
    # Draw base and hook
    canvas.create_line(10,size-10,50,size-10)
    canvas.create_line(30,size-10,30,50)
    canvas.create_line(30,50,200,50)
    radius = 30
    if count >= 1: #Draw sting to neck
        canvas.create_line(200,50,200,70,tags="hang")
    if count >= 2: #Draw face
        canvas.create_line(200-radius, 100-radius,
                           200+radius, 100+radius, tags="hang")
    if count >= 3: #Draw first arm
        canvas.create_line(170,100,100,150,tags="hang")
    if count >= 4: #Draw second arm
        canvas.create_line(230,100,300,150,tags="hang")
    if count >= 5: #Draw body length
        canvas.create_line(200,130,200,250,tags="hang")
    if count >= 6: #Draw one leg
        canvas.create_line(200,250,100,300,tags="hang")
    if count >= 7: #Draw second leg
        canvas.create_line(200,250,300,300,tags="hang")
 
    #Display message
    canvas.create_text(200,size-30,text=msg1,tags="hang")
    canvas.create_text(200,size-10,text=msg2,tags="hang")
 
#Start a new game
def newGame():
    #Modifying below global variable locally
    global count, latestStr, word, missedLetters
    # Randomly select a word from list
    word = random.choice(words)
    latestStr="* " *len(word)
    count = 0 #Counter for number of attempts
    missedLetters='' #List of missed alphabets
    msg1="Guess a word: " +latestStr
    msg2=""
    #Draw the latest hangman, display messages
    draw(count,msg1,msg2)
 
def play(event):
    newGame()
 
# Create a window, set its title
window = Tk()
window.title("Hangman")
 
#Global variables
word = latestStr = missedLetters = ''
count=0
 
# create a canvas, add it to window
size=400
canvas = Canvas(window, width = size, height = size)
canvas.pack() # Hold the pictue
 
# List of words
words = ["write", "that", "Program", "hello", "welcome"]
newGame() # play a new game
 
# Keep playing till users presses enter key
canvas.focus_set() # Required as usual focus is on mouse
canvas.bind("<KeyPress>", keyPressed) # bind all keys
canvas.bind("<space>", play) # override space
 
window.mainloop() #Create an event loop

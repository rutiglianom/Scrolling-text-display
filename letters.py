# Matthew Rutigliano
# ECEGR 3910
# November 17th, 2019
# AS.16b: Scrolling Text
# Description: User inputs phrase. Graphics screen generates circles printing the phrase in a scrolling manner.

from graphics import *
import time


#Define Constants
rows = 7
cols = 6
DOT_RAD = 15
OFFSET = 3
BUTTON_RAD = 30
WIN_CHARS = 8
WIN_X_CIRCS = cols * WIN_CHARS
WIN_WIDTH = (DOT_RAD*2 + OFFSET) * WIN_X_CIRCS #Pixels
WIN_HEIGHT = (DOT_RAD*2+ OFFSET) * rows + OFFSET   #Pixels

REFRESH_RATE = 30

win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setCoords(0, -WIN_HEIGHT, WIN_WIDTH, 0)
win.setBackground("grey")

letters = {"A":((0,1,1,1,0,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,1,1,1,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0)),
           "B":((1,1,1,1,0,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,1,1,1,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,1,1,1,0,0)),
           "C":((0,1,1,1,1,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (0,1,1,1,1,0)),
           "D":((1,1,1,0,0,0), (1,0,0,1,0,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,1,0,0), (1,1,1,0,0,0)),
           "E":((1,1,1,1,1,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,1,1,1,1,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,1,1,1,1,0)),
           "F":((1,1,1,1,1,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,1,1,1,1,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,0,0,0,0,0)),
           "G":((0,1,1,1,1,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,0,1,1,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (0,1,1,1,1,0)),
           "H":((1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,1,1,1,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0)),
           "I":((1,1,1,1,1,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (1,1,1,1,1,0)),
           "J":((1,1,1,1,1,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (1,1,0,0,0,0)),
           "K":((1,0,0,0,1,0), (1,0,0,1,0,0), (1,0,1,0,0,0), (1,1,0,0,0,0), (1,0,1,0,0,0), (1,0,0,1,0,0), (1,0,0,0,1,0)),
           "L":((1,0,0,0,0,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,1,1,1,1,0)),
           "M":((1,0,0,0,1,0), (1,1,0,1,1,0), (1,1,1,1,1,0), (1,0,1,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0)),
           "N":((1,0,0,0,1,0), (1,1,0,0,1,0), (1,1,1,0,1,0), (1,0,1,1,1,0), (1,0,0,1,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0)),
           "O":((0,1,1,1,0,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (0,1,1,1,0,0)),
           "P":((1,1,1,1,0,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,1,1,1,0,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (1,0,0,0,0,0)),
           "Q":((0,1,1,1,0,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,1,0,1,0), (1,0,0,1,1,0), (0,1,1,1,1,0)),
           "R":((1,1,1,1,0,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,1,1,1,0,0), (1,1,1,0,0,0), (1,0,0,1,0,0), (1,0,0,0,1,0)),
           "S":((0,1,1,1,1,0), (1,0,0,0,0,0), (1,0,0,0,0,0), (0,1,1,1,0,0), (0,0,0,0,1,0), (0,0,0,0,1,0), (1,1,1,1,0,0)),
           "T":((1,1,1,1,1,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0)),
           "U":((1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (0,1,1,1,0,0)),
           "V":((1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (0,1,0,1,0,0), (0,0,1,0,0,0)),
           "W":((1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,0,0,1,0), (1,0,1,0,1,0), (1,1,1,1,1,0), (1,1,0,1,1,0), (1,0,0,0,1,0)),
           "X":((1,0,0,0,1,0), (1,1,0,1,1,0), (0,1,0,1,0,0), (0,0,1,0,0,0), (0,1,0,1,0,0), (1,1,0,1,1,0), (1,0,0,0,1,0)),
           "Y":((1,0,0,0,1,0), (0,1,0,1,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0), (0,0,1,0,0,0)),
           "Z":((1,1,1,1,1,0), (0,0,0,0,1,0), (0,0,0,1,0,0), (0,0,1,0,0,0), (0,1,0,0,0,0), (1,0,0,0,0,0), (1,1,1,1,1,0)),
           " ":((0,0,0,0,0,0), (0,0,0,0,0,0), (0,0,0,0,0,0), (0,0,0,0,0,0), (0,0,0,0,0,0), (0,0,0,0,0,0), (0,0,0,0,0,0))}

myLetters = []
myPhrase = input("Enter phrase to display: ")
myPhrase = myPhrase.upper()

for elem in myPhrase:
    if elem in letters:
        myLetters.append(letters[elem])
        
for i in range(WIN_CHARS):
    myLetters.append(letters[' '])

circList = []

for i in range(WIN_X_CIRCS):
        circList.append([])
        for j in range(rows):
            circList[i].append(Circle(Point(((OFFSET+DOT_RAD*2)*i)+(OFFSET+DOT_RAD),((OFFSET+DOT_RAD*2)*-j)-(OFFSET+DOT_RAD)), DOT_RAD))
            circList[i][j].setFill('black')
            circList[i][j].draw(win)

try:
    while(1): 
        for scroll in range(len(myLetters)*cols): # Scrolls for length of myLetters
            for i in range(WIN_X_CIRCS):
                #circList.append([])
                if (i < WIN_X_CIRCS - scroll):
                    for j in range(rows):
                        circList[i][j].setFill('black')
                else:
                    for j in range(rows):
                        if (myLetters[(i - WIN_X_CIRCS + scroll)//cols][j][(i - WIN_X_CIRCS + scroll)-cols*((i - WIN_X_CIRCS + scroll)//cols)] == 1):
                            circList[i][j].setFill('red')
                        else:
                            circList[i][j].setFill('black')
             
            update(REFRESH_RATE)
            
except KeyboardInterrupt: 
    # This code runs on a Keyboard Interrupt <CNTRL>+C
    win.close()
    print('\n\n' + 'Program exited on a Keyboard Interrupt' + '\n') 

except: 
    # This code runs on any error
    win.close()
    print('\n' + 'Errors occurred causing your program to exit' + '\n')

finally: 
    # This code runs on every exit and sets any used GPIO pins to input mode.
    win.close()


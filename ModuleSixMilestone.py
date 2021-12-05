'''
Author: Joe Farrish
Title: Zorpion Infiltration.
GitHub: https://github.com/joejoe909/ZorpionInfiltration

Story: You are apart of scientific expedition into deep space when a part of the ship is breeched by a strange
creature that has killed off most of the crew. You have to lure it to a room with incineration vac to kill and
expunge it from the ship. 

Items you can get to help you.
		Jet pack – will increase space traveled to 1  capsules per move (2 sectors).
		An electric shock taser – Causes the Zorpion to lose movement.
		A shield increases damage points.
		Droid – can move in your place and can be used to lure the Zorpion to
		different parts of the ship.

'''
import os # For clearing the screen.
import  random
import sys


def clear(): # Function to clear the screen.
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#The International Life Survival in Space Experimentation Space Lab.
capsules = {
    #Center Hull
    '0,0': {'Go East': '0,1'},
    '0,1': {'Go North': '1,1', 'Go South': '-1,1', 'Go West': '0,0', 'Go East': '0,2'} ,
    '0,2': {'Go West': '0,1', 'Go East':'0,3'},
    '0,3': {'Go North': '1,3', 'Go South': '-1,3', 'Go West': '0,2', 'Go East': '0,5'},
    '0,4': {'Go West': '0,3', 'Go East': '0,5'},
    '0,5': {'Go West': '0,4'},

    #Wing 1 (x,1)
    '1,1': {'Go South': '0,1', 'Go North': '2,1'},
    '2,1': {'Go South': '1,1'},
    '-1,1': {'Go North:': '0,1', 'Go South': '-2,1'},
    '-2,1': {'Go North': '-1,1'},

    #Wing 2 (x,3)
    '1,3': {'Go South': '0,3', 'Go North': '2,3'},
    '2,3': {'Go South': '1,3'},
    '-1,3': {'Go North:': '0,3', 'Go South': '-2,3'},
    '-2,3': {'Go North': '-1,3'},
}

#prompt for name.
clear()
#global vars
doctor = ''
sector = 1
curLoc = '' # current location is a string with x,y values in it.
choices = [[],[],[],[]]

def getName():
    global doctor
    doctor= input('Please enter your name, you\'r a doctor so make it prestigeous (i.e. Dr. Dingus): ')

#Welcome Message


clear()

#Welcome the Dr.
def welcome(doctor):
    clear()
    print(f'Hello Dr. {doctor},\n\n','A strange creature has breeched the hull of the \n', 
            'International Study For Life Survial In Space Experimentation Lab, you\n',
            'must lure it into a capsule with incineration EVAC to expunge it fromt he ship.\n')

#this function will display location and available options based on location. 
def menu():
    clear()
    global capsules, curLoc, choices
    #Display Map.
    print(f'Dr. {doctor}, you are in Capsule {curLoc} you can:', end= '\n')
    #print( zorpion location )    
    #now setup capsule move menu from capsule[curLoc]
    #options = capsules[curLoc]
    kys = capsules[curLoc].keys()

    sel = 0
    gChcAmt = len(choices)

    choice = [[],[],[],[]]

    #Display movement operations available depending on location. 
    for z in kys:
        print(sel, z ,'to sector' ,capsules[curLoc][z], end='\n')
        choice[sel] = capsules[curLoc][z]
        sel+=1

    

    choices = choice  

#This Function gets the users input if the value is out of range it will loop unitl a valid choice is issued.
#Entering 5 will exit the loop. 
def getInp():
    global choices, curLoc, playing
    gtoLoc = -2

    while not ((gtoLoc >= 0) and (gtoLoc <= len(choices))):
        gtoLoc = int(input('Enter your Selection or type the number 5 exit the game:'))
        if gtoLoc == 5:
            print('Thanks for playing Zorpion Infiltration!')
            sys.exit()


    print(f'you selected: {choices[gtoLoc]}') 
    curLoc = choices[gtoLoc]
    print(f'moved to {curLoc}')


#randomly place the user and Zorpion on the map
def randomPlace():
    x = random.randrange(-2, 2)
    y = int

    if x ==0:
        y = random.randrange(0,5)
    else:
        y = random.randrange(1, 3, 1)
        if y == 2:
            y = 3
    return f'{x},{y}'


#main while loop.
running = 1
while(running):
    getName()
    welcome(doctor)
    curLoc = randomPlace()
    #movement loop
    mv = True
    chs = True
    playing = True
    while playing:
        while mv:
            menu()
            mv = False
            chs = True
        
        while chs:
            getInp()
            mv = True
            chs = False

    #print(capsules[randomPlace()])
    #ADD: Zorpion Moves




#randomly place in a capsule
#Hello Dr. Dingus you are now in randomly selected capsule.

#begin loop




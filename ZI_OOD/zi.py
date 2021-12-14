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

        Table of contents:
        The main gaime loop starts @ line 142.
        Zorpion Movment is on starts @ line -- (zorpMv())
        Input is controlled by getInp() on line 87
        Menu is on line 52

        TODO: We still need to get a good calculation for zorpion movement.


'''
import os # For clearing the screen.
import  random
import sys
import re #for regex

# Function to clear the screen.
def clear(): 
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Prompt for name.
def getName():
    global doctor
    doctor= input('Please enter your name, you\'r a doctor so make it prestigeous (i.e. Dr. Dingus): ')

# Print Welcome Message.
def welcome(doctor):
    clear()
    print(f'Hello Dr. {doctor},\n\n','A strange creature has breeched the hull of the \n', 
            'International Study For Life Survial In Space Experimentation Lab, you\n',
            'must lure it into a capsule with incineration EVAC to expunge it fromt he ship.\n')

# This function will display location and available options based on location. 
def menu():
    clear()
    global capsules, curLoc, curLocInt, choices, incRooms, zorpionLoc, zrpPath  # for OOD these will refer to the class.
    
    if(zCompelled):
        print('Warning Zorpion is compelled! Movement is * 2!')

    #Display Map.
    print(f'Incineration rooms are in capsules {incRooms[0]}, {incRooms[1]}, {incRooms[2]}', end ='\n') # These are generated on line:343. 
    print(f'Zorpion location is at: {zorpionLoc}, current path is: {zrpPath}\n')
    print(f'Dr. {doctor}, you are in Capsule {curLoc}, you can:', end= '\n')
    #print( zorpion location )    
    #now setup capsule move menu from capsule[curLoc]
    #options = capsules[curLoc]
    
    if type(curLoc) == str:
        kys = capsules[curLoc].keys()

 

    sel = 0
    gChcAmt = len(choices)

    choice = [[],[],[],[]]

    #Display movement operations available depending on location. 
    for z in kys:
        print(sel, z ,'to sector' ,capsules[curLoc][z], end='\n')
        if type(curLoc) == str:
            choice[sel] = capsules[curLoc][z]
        sel+=1
    choices = choice 

#This Function gets the users input if the value is out of range it will loop unitl a valid choice is issued.
#Entering 5 will exit the loop. 
def getInp():
    global choices, curLoc, playing, exitVal, curLocInt
    gtoLoc = -2

    while not ((gtoLoc >= 0) and (gtoLoc <= len(choices))):
        
        gtoLoc = int(input(f'Enter your Selection or type the number {exitVal} to exit the game:'))
        
        if gtoLoc == exitVal:
            print('Thanks for playing Zorpion Infiltration!')
            sys.exit()


    print(f'you selected: {choices[gtoLoc]}') 
    curLoc = choices[gtoLoc]
    print('147 is type of', type(curLoc))
    print('148: ' , curLoc)
    if type(curLoc) == str:
        curLocInt = locInInt(curLoc)
    print(f'moved to {curLoc}')
  
#randomly place the user and Zorpion on the map
def randomPlace():
    global curLocInt
    x = random.randrange(-2, 2)
    y = int

    if x ==0:
        y = random.randrange(0,5)   
    else:
        y = random.randrange(1, 3, 1)
        if y == 2:
            y = 3
    return f'{x},{y}'

# Remove unwanted characters from a string
def purifyLoc(loc):
    pl = '('
    pr = ')'
    
    if pl or pr in loc:
        loc = loc.replace(pl, '')
        loc = loc.replace(pr, '')        


    return loc

def locInInt(loc):
    a = loc.split(',')
    x=-1 # set as signed int
    y=-1
    x = int(a[0])
    y = int(a[1])
    return [x,y]

#---------------------------------------------------------
# Main game loop.
#---------------------------------------------------------
running = 1
while(running):
    getName()
    welcome(doctor)
    curLoc = randomPlace()
    curLocInt = locInInt(curLoc)
    incRooms = [randomPlace(), randomPlace(), randomPlace() ]
    zorpionLoc = randomPlace()
    zrpPath = stZorpPath()

    #Randomly place items
    mv = True
    chs = False #user move
      
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
            zrpmv = True    
        
        while zrpmv:
            zorpMv()
            zrpmv = False
            #based on zorpionLoc set a path 
                #if x is 0 then move west if y > 3
                    #setpath to a value west
            #user in the same axis axis as zorp zCompelled = True
    #print(capsules[randomPlace()])
    #ADD: Zorpion Moves

#randomly place in a capsule
#Hello Dr. Dingus you are now in randomly selected capsule.

#begin loop
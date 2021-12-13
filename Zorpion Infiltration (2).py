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
        The main gaime loop starts @ line 325.
        Zorpion Movment is on starts @ line 174 (zorpMv())
        Input is controlled by getInp() on line 139
        Menu is on line 104

'''
import os # For clearing the screen.
import  random
import sys
import re #for regex


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


clear()
#------------------------global vars
#setup user.
doctor = ''
sector = 1
curLoc = '' # current location is a string with x,y values in it.
curLocInt = [] #[x,y] 
choices = [[],[],[],[]]
exitVal = 99


#set Zorpion
zorpionLoc = ''
zrpLocInt = []# [x, y]  setLoc loc in int list.  
zrpmv = False #zrp move
zMv = 1 #The amount of capsules the zorpion can move per move can be 1 or 2. 
zCompelled = False
zrpPath = [] # [x, y]  setZPath. 

#------------------------prompt for name.
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

#setup Zorpion
# def setZorp(*args):
#     global zorpionLoc ,zrpmv, zCompelled, zrpLoc, zrpPath   
#     zorpionLoc = args[0]
#     zrpmv = args[1]
#     zCompelled = args[2]
#     zrpLoc = args[3]
#     zrpPath = args[4]

#this function will display location and available options based on location. 
def menu():
    clear()
    global capsules, curLoc, curLocInt, choices, incRooms, zorpionLoc, zrpPath  
    
    if(zCompelled):
        print('Warning Zorpion is compelled! Movement is * 2!')

    #Display Map.
    print(f'Incineration rooms are in capsules {incRooms[0]}, {incRooms[1]}, {incRooms[2]}', end ='\n')
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

# Manage Logical Movement of the Zorpion
def zorpMv():
    # Based on current location make way to the path which is random at first but then 
    # Should change based on the user falling on axis or the path point is reached and then
    # A new path is randomly generated.
    global zrpLoc, zrpLocInt, zorpionLoc,curLocInt,zCompelled,zMv, curLoc, curLocInt, zrpPath, capsules 
    print(curLoc)
    
    if zrpPath == zrpLocInt:
        # get new path.
        zrpPath = stZorpPath()
    
    if type(zorpionLoc) == str:
        print('181',zorpionLoc)
        zLoc = purifyLoc(zorpionLoc)
        zrpLocInt = locInInt(zLoc)
    if type(curLoc) == str:
        print('184', curLoc)
        zLoc = purifyLoc(curLoc)
        curLocInt = locInInt(zLoc)
        
    zx = zrpLocInt[0]
    zy = zrpLocInt[1]

    mvs = []
    # Zorpion Move value
    zorpMovVal = []

    quadPoint1 = [0,1]
    quadPoint2 = [0,3]

    cx = curLocInt[0]
    cy = curLocInt[1]

    if (zx == cx) or (zy == cy):
        zCompelled = True
        zMv = 2
        zrpPath = curLocInt
        # print('Warning The Zorpion is Compelled! Movement * 2 !!! Bro you better run!!')

    #get to location
    #get choices
    chc = str(f'{zx},{zy}')
    choices = capsules[chc].values()
    print('choices:', len(choices))
    numChoice = len(choices)
    for i in capsules[chc].values():
        print('zorpion can go:', i)
        mvs.append(i)

    # if 1 choice
    if numChoice == 1:
        #move there
        zrpLocInt = locInInt(mvs[0])
        print('loc chnged to:', zrpLocInt)
        zorpionLoc = f'{zrpLocInt[0], zrpLocInt[1]}'
    # if 2 choices
    if numChoice > 1:
        choice1 = locInInt(mvs[0])
        choice2 = locInInt(mvs[1]) 
        # testing how to move on a path
        zorpMovVal = [zrpLocInt[0] - zrpPath[0], zrpLocInt[1] - zrpPath[1]] # this is the movement intention
        print('230: zorpMovVal', zorpMovVal)
        zorpMovVal[0] = zorpMovVal[0] * -1
        zorpMovVal[1] = zorpMovVal[1] * -1
        print("we need to move", zorpMovVal[0], zorpMovVal[1])
        # if(zorpMovVal[0] > zrpPath[0]):
        # compare zrpPath to each quad sector
        # if both are close
        # if both are further away

    # # if 4 choices. we are at a quad point.
    # if numChoice == 4:
    #     print('4 choices')


    #move zorpion
    if zorpMovVal != []:

        moves = 0
        while(moves < zMv):
            #which of those allow a value closer to zrpPath
            print('250: zorpMovVal', zorpMovVal)
            zmvX = zorpMovVal[0]
            zmvY = zorpMovVal[1]
            print('253: zmvX is type of: ', type(zmvX), zmvX, 'zmvY is type of: ', type(zmvY), zmvY)
            if abs(zorpMovVal[0]) and (moves < zMv):
                zrpLocInt[0] = zrpLocInt[0] + zorpMovVal[0]
                moves+=1
                if moves >= zMv:
                    break
            if abs(zorpMovVal[1]) and (moves < zMv):
                zrpLocInt[1] = zrpLocInt[1] + zorpMovVal[1]    
                moves+=1
                if moves >= zMv:
                    break
                
            moves+=1

    # Limit values to ship
    if(zrpLocInt[0] > 5):
        zrpLocInt[0] = 5
    elif(zrpLocInt[0] < 0):
        zrpLocInt[0] = 0

    if(zrpLocInt[1] > 2):
        zrpLocInt[1] = 2
    elif(zrpLocInt[1] < -2):
        zrpLocInt[1] = -2    



    if zorpionLoc != f'{zrpLocInt[0], zrpLocInt[1]}':
        zorpionLoc = f'{zrpLocInt[0], zrpLocInt[1]}'
        print('zrp loc is now: ', zorpionLoc)
    elif zorpionLoc[0] == 0 and zorpionLoc[1] == 0:
        rndchc = len(0,len(mvs))
        zorpionLoc = mvs[rndchc]
        zrpLocInt = locInInt(purifyLoc(zorpionLoc))
        print('zrp loc is now: ', zorpionLoc)

    

# Remove unwanted characters from a string
def purifyLoc(loc):
    pl = '('
    pr = ')'
    
    if pl or pr in loc:
        loc = loc.replace(pl, '')
        loc = loc.replace(pr, '')        


    return loc


  
# Sets the Zorpion Path in which he will traverse.
def stZorpPath():
        x = random.randrange(-2, 2)
        y = int

        if x ==0:
            y = random.randrange(0,5)
        else:
            y = random.randrange(1, 3, 1)
            if y == 2:
                y = 3
        return [x,y]

def locInInt(loc):
    a = loc.split(',')
    x=-1 # set as signed int
    y=-1
    x = int(a[0])
    y = int(a[1])
    return [x,y]


# Main game loop.
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
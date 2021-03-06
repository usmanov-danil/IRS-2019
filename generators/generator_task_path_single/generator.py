''' 
    This code generates the fields for the task "The path in the maze without verifying the optimality".
    source.xml - template with walls and regions.
    localization_generator.py - python script for generate fields with input .txt files.

    Via consloe input, enter the number of tests to generating.    

    If you have any qestions write me via:
        telegram: @usmanov_d
        email: usmanovdanilr@gmail.com
'''
import random

MAX_CELL = 7 #The maximum number of cells in width and height. In this case it is 7
MAX_DIR = 3 #The maximum number of directions. In this case it is 3
OFFSET = 200 #Scaling the cell size in a maze
NUM_CELLS = 64 #The number of cells in the maze

n = int(input("Enter number of fields: ")) #The number of fields
block = {"60","11","41","62","13","43","64","15","35","46","66","17"} #Blocked cells
used = set() #Set of generated start cells
data = open('source.xml').read() #The source file with regions and walls 

if n > (NUM_CELLS - len(block)): #Excecption
    print("The number of tests is bigger than number of free cells!")
    print("The number of tests will be equal to " + str(NUM_CELLS - len(block)) + "!")
    n = (NUM_CELLS - len(block))

for i in range(n):
    code = data #Copy the sorce code 
    xmlFile = open('task2_' + str(i) + '.xml', 'w') #Create a fields with .xml type
    txtFile = open('task2_' + str(i) + '.txt', 'w') #Create an input .txt file with start, finish coordinates and start direction

    #Generate start cell
    startX = random.randint(0, MAX_CELL)
    startY = random.randint(0, MAX_CELL)
    while(True): #Check this cell on validality
        if str(startX * 10 + startY) in block or str(startX * 10 + startY) in used: #If this cell is blocked or is generated yet
            startX = random.randint(0, MAX_CELL)
            startY = random.randint(0, MAX_CELL)
        else:
            break
    used.add(str(startX * 10 + startY))  #Add new valid cell in used set

    #Generate finish cell
    finishX = random.randint(0, MAX_CELL)
    finishY = random.randint(0, MAX_CELL)
    while (True): #Check this cell on validality
        if str(finishX * 10 + finishY) in block or str(finishX * 10 + finishY) in used: #If this cell is blocked or is generated yet
            finishX = random.randint(0, MAX_CELL)
            finishY = random.randint(0, MAX_CELL)
        else:
            break
    used.add(str(finishX * 10 + finishY))  #Add new valid cell in used set
    direction = random.randint(0, MAX_DIR) #Get random direction

    #Start region
    start = '<region type="rectangle" filled="true" ' \
            'x="' + str(int(startX) * OFFSET) + '" ' \
            'y="' + str(int(startY) * OFFSET) + '" visible="true" height="200" width="200" textX="0" ' \
            'id="start" color="#0000ff" text="Start" textY="0"/>\n'
    #Finish region
    finish = '<region type="rectangle" filled="true" ' \
            'x="' + str(int(finishX) * OFFSET) + '" ' \
            'y="' + str(int(finishY) * OFFSET) + '" visible="true" height="200" width="200" textX="0" ' \
            'id="finish" color="#ff0000" text="Finish" textY="0"/>\n'

    #Robot's start position
    robot = str(int(startX) * OFFSET + 75) + ":" + str(int(startY) * OFFSET + 75)
    startPosX = str(int(startX) * OFFSET + 100)
    startPosY = str(int(startY) * OFFSET + 100)

    #Replace all keywords on generated data
    code = code.replace('START', start)
    code = code.replace('FINISH', finish)
    code = code.replace('ROBOT', robot)
    code = code.replace('STPOSX', startPosX)
    code = code.replace('STPOSY', startPosY)
    code = code.replace('DIR', str(direction * 90))

    text = str(startX) + " " + str(startY) + " " + str((direction + 1) % 4) + "\n" + \
           str(finishX) + " " + str(finishY)
    #Write finite code in .xml field
    xmlFile.write(code)
    txtFile.write(text)
    xmlFile.close()
    txtFile.close()
    print("test" + str(i) + " success")
print("all success")
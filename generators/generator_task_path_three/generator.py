''' 
    This code generates the fields for the task "The path in the maze for three robots without verifying the optimality".
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
NUM_CELLS = 64 #The number of cells in the maze
NUM_ROBOTS = 3 #The number of robots

n = int(input("Enter number of fields: ")) #The number of fields
block = {"60","11","41","62","13","43","64","15","35","46","66","17"} #Blocked cells
used = set() #Set of generated start cells
data = open('source.xml').read() #The source file with regions and walls 

if n > (NUM_CELLS - len(block)): #Excecption
    print("The number of tests is bigger than number of free cells!")
    print("The number of tests will be equal to " + str(NUM_CELLS - len(block)) + "!")
    n = (NUM_CELLS - len(block))

for i in range(n):
    xmlFile = open('task3_' + str(i) + '.xml', 'w') #Create .xml file
    txtFile = open('task3_' + str(i) + '.txt', 'w') #Create .txt file 
    used = set() #Set of generated cells
    test = ""

    for _ in range(NUM_ROBOTS): #Generate starts and finishes for all 3 robots
        startX = random.randint(0, MAX_CELL)
        startY = random.randint(0, MAX_CELL)
        while(True): #Check this cell on validality
            if str(startX * 10 + startY) in block or str(startX * 10 + startY) in used: #If this cell is blocked or is generated yet
                startX = random.randint(0, MAX_CELL)
                startY = random.randint(0, MAX_CELL)
            else:
            	break 
        used.add(str(startX * 10 + startY)) #Add new valid cell in used set

        finishX = random.randint(0, MAX_CELL)
        finishY = random.randint(0, MAX_CELL)
        while (True): #Check this cell on validality
            if str(finishX * 10 + finishY) in block or str(finishX * 10 + finishY) in used: #If this cell is blocked or is generated yet
                finishX = random.randint(0, MAX_CELL)
                finishY = random.randint(0, MAX_CELL)
            else:
            	break
        used.add(str(finishX * 10 + finishY)) #Add new valid cell in used set

        direction = random.randint(0, MAX_DIR) #Get random direction
        text = str(startX) + " " + str(startY) + " " + str(direction) + " " + str(finishX) + " " + str(finishY) + "\n" #Create an input

    #Write the input in a .txt file
    xmlFile.write(code)
    txtFile.write(text)
    xmlFile.close()
    txtFile.close()
    print("test" + str(i) + " success")
print("all success")
import random
import time
from termcolor import colored

# ======= FUNCTIONS =======
def nameGenerator():
    # List of characters
    chars = ["a", "i", "u", "e", "o",
    "ka", "ki", "ku", "ke", "ko",
    "sa", "shi", "su", "se", "so",
    "ta", "chi", "tsu", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo",
    "ra", "ri", "ru", "re", "ro",
    "wa", "wo"]

    # Determine syllables per name
    firstSyl = random.randint(2, 4)
    lastSyl = random.randint(2, 4)

    firstName = ""
    lastName = ""

    # Generate names
    for i in range(firstSyl):
        firstName += chars[random.randint(0, len(chars)-1)]

    for i in range(lastSyl):
        lastName += chars[random.randint(0, len(chars)-1)]

    return firstName.capitalize() + " " + lastName.capitalize()

def ultGenerator():
	return "Ultimate " + ultimates[random.randint(0, len(ultimates)-1)]

def cyan(str):
    return colored(str, "cyan")

def yel(str):
    return colored(str, "yellow")

def red(str):
    return colored(str, "red")

def blue(str):
    return colored(str, "blue")

def mag(str):
    return colored(str, "magenta")

# Print colored graphic depicting remaining students
def printStudents(students, alive):
    numAlive = 16
    print()
    for name in students:
        # If alive, print normally
        if name in alive:
            print(mag(name) + cyan(" the ") + yel(students[name]))
        # Otherwise, mark red
        else:
            print(red(name + " the " + students[name]))
            numAlive -= 1
        time.sleep(0.25)
    print(blue("         ========================"))
    print(blue("          Remaining Students: ") + str(numAlive))
    print(blue("         ========================"))

def printDay(dayNum):
    print(mag("==================================================================================="))
    if (dayNum < 10):
        print(mag("================================ [ D A Y   " + str(dayNum) + " ] ===================================="))
    else:
        print(mag("================================ [ D A Y   " + str(dayNum) + " ] ==================================="))
    print(mag("==================================================================================="))
    print()

def printTrial(trialNum):
    print(yel("==================================================================================="))
    if (trialNum < 10):
        print(yel("============================== [ T R I A L   " + str(trialNum) + " ] =================================="))
    else:
        print(yel("============================== [ T R I A L   " + str(trialNum) + " ] ================================="))
    print(yel("==================================================================================="))
    print()

def ringBell():
    time.sleep(1)
    print(blue("DING"))
    time.sleep(0.5)
    print(blue("DONG"))
    time.sleep(0.5)
    print(blue("BING"))
    time.sleep(0.5)
    print(blue("BONG"))
    time.sleep(1)


# ========================= GAME CODE ==============================

# Prep Ultimates list
f = open("ultimates.txt")
ultimates = f.readlines()
f.close()

# Prep Kill List
f2 = open("killMethods.txt")
killList = f2.readlines()
f2.close()

# Prep Dialogue lists
f3 = open("dialogue1.txt")
d1List = f3.readlines()
f3.close()

f4 = open("dialogue2.txt")
d2List = f4.readlines()
f4.close()

f5 = open("dialogue3.txt")
d3List = f5.readlines()
f5.close()

# INTRO: Ask User for Info
print()
print(colored("===================================================================================", "red"))
print(colored("===================[ D A N G A N R O N P A     V - P Y T H O N ]===================", "red"))
print(colored("===================================================================================", "red"))
print()
input(colored("                            ~ Press any key to START ~", "red"))
print()

playerName = input(colored("Welcome to Python Danganronpa. Please enter your FULL name: ", "blue"))
playerUlt = input(colored("Please enter your Ultimate talent (starting with 'Ultimate'): ", "blue"))
time.sleep(1)
print()
print(colored("Welcome, " + playerName + ", the " + playerUlt + ".", "cyan"))
print()

# Create Player and Alive Dictionaries
students = {playerName: playerUlt}
alive = {playerName: playerUlt}
records = {}

for i in range(15):
    newName = nameGenerator()
    newUlt = ultGenerator().strip('\n')
    students[newName] = newUlt
    alive[newName] = newUlt

# Introduce other players
input(cyan("Meet your fellow students! (Press Enter)"))

for name in students:
    print(mag(name) + cyan(" the ") + yel(students[name]))
    time.sleep(1)

print()
input(blue("Tutorial Time!"))
input(blue("On each day, you will be prompted to type in ") + yel("what you do for the day."))
input(blue("Type in whatever you want!"))
input(blue("Although... you can also choose to kill someone, by typing ") + red("KILL ") + blue("in all caps."))
input(blue("You'll then be prompted to type the ") + yel("full name ") + blue("of the person you want to kill."))
input(blue("You'll also be asked to describe how you killed the person! Yikes!"))
input(blue("As you can see, each day there's a chance someone might get ") + red("killed") + blue(", even ") + yel("you!"))
input(blue("When this occurs, everyone will go through a ") + yel("class trial."))
input(blue("The group will determine ") + yel("3 ") + red("blackened ") + blue("students, and vote for one of them!"))
input(blue("The ") + yel("true killer ") + blue("will always be among these 3. Vote carefully! Majority rules."))
input(blue("Whether or not the verdict is correct, the game will continue. (Don't worry, you'll be told if you were right or not!)"))
input(blue("The game continues for ") + yel("17 ") + blue("days... how many of you will survive by then?"))
input(blue("Well, have fun!"))
print()
time.sleep(1)

# Set up Day and Trial systems
dayNum = 1
killChance = 3
goToTrial = False
trialNum = 1

# ====================== DAILY ROUTINE ============================
# Game ends on day 20, or if only two survivors.
while(dayNum < 18 and len(alive) > 2):
    printDay(dayNum)
    ringBell()

    # Special Messages
    if (dayNum == 13):
        print(blue("5 days left. You're all almost there! Except for whoever's gonna die soon, puhuhu..."))
    if (dayNum == 17):
        print(blue("You made it to the ") + yel("final day.") + blue(" Will you survive it though?"))
    # Player's choice (if alive)
    if (playerName in alive):
        dayChoice = input(cyan("Good morning ") + playerName + cyan("! What will do you do today? "))

        # Kill route
        if (dayChoice == "KILL"):
            victim = input(cyan("Puhuhu... very well. ") + yel("Who ") + cyan("would you like to ") + red("kill? "))

            while (victim not in alive):
                victim = input(cyan("I think you misspelled... or they're already dead? Type it in again: "))
            
            killMethod = input(cyan("And ") + yel("how ") + cyan("would you like to kill them? (Start the sentence with 'by') "))
            time.sleep(1)
            print(cyan("You decided to ") + red("kill ") + yel(victim) + " " + yel(killMethod))
            time.sleep(1)

            goToTrial = True
            alive.pop(victim)
            killer = playerName
            records[victim] = "Killed by " + playerName

        # Regular route
        else:
            input(cyan("How fun! ") + playerName + cyan(" decided to ") + yel(dayChoice) + " ")
    
    # Determine if someone else did a kill
    if (goToTrial == False):
        if (random.randint(0, killChance) == 0):

            # Determine the victim
            victim = random.choice(list(alive.keys()))
            alive.pop(victim)

            # Determine killer
            killer = random.choice(list(alive.keys()))

            # Make sure it's not the player!
            while(killer == playerName):
                killer = random.choice(list(alive.keys()))
            
            # Determine cause of death 
            killMethod = killList[random.randint(0, len(killList)-1)].strip('\n')

            goToTrial = True
            records[victim] = "Killed by " + killer
        else:
            victim = "none"
            killer = "none"

    time.sleep(1)
    print(blue("The day turned into night..."))
    if (victim == playerName):
        time.sleep(1)
        input(blue("Suddenly, everything went black..."))
        input(blue("With the last moments of your life, you hear..."))

    ringBell()

    # ============================== TRIAL ROUTE ====================================
    if (goToTrial == True):
        input(blue("A body has been discovered!"))
        input(yel(victim) + cyan(" has been ") + red("killed!"))
        input(blue("The killer did it ") + yel(killMethod) + blue("!"))

        if (victim == playerName):
            input(red("Oops, you're DEAD. Puhuhu..."))
        
        input(blue("Everyone did their investigations..."))
        input(blue("And the ") + yel("class trial ") + blue("began."))
        print()
        printTrial(trialNum)

        input(blue("The trial for the murder of ") + mag(victim) + blue(" the ") + yel(students[victim]) + " ")
        print()
        input(blue("Everyone began debating..."))
        # Add some dialouge and options here
        dialogue = {}

        # Add player dialogue
        if (playerName in alive):
            playerLine = input(cyan("Would you like to say anything to the group? (If not, type 'no') "))
        else:
            playerLine = "no"

        # Determine other's dialogue
        # Get unique list of 3 people
        talkers = []

        # Edge case where player is alive with 2 other people
        if (len(alive) == 3 and playerName in alive):
            for talk in alive:
                # Don't add the player
                if (talk == playerName):
                    continue
                else:
                    talkers.append(talk)
            
            # Append each person to the dictionary with dialogue
            for i in range(2):
                if i == 0:
                    dialogue[talkers[i]] = d1List[random.randint(0, len(d1List)-1)].strip('\n')
                else:
                    dialogue[talkers[i]] = d2List[random.randint(0, len(d2List)-1)].strip('\n')
        
        # Otherwise, do the usual random 3
        else:
            for i in range(3):
                talk = random.choice(list(alive.keys()))

                # Make sure it's not a repeat or the player
                while (talk in talkers or talk == playerName):
                    talk = random.choice(list(alive.keys()))
                
                talkers.append(talk)
            
            # Append each person to the dictionary with dialogue
            for i in range(3):
                if i == 0:
                    dialogue[talkers[i]] = d1List[random.randint(0, len(d1List)-1)].strip('\n')
                elif i == 1:
                    dialogue[talkers[i]] = d2List[random.randint(0, len(d2List)-1)].strip('\n')
                else:
                    accused = random.choice(list(alive.keys()))
                    # Make sure it's not themselves
                    while (accused == talkers[i]):
                        accused = random.choice(list(alive.keys()))
                    dialogue[talkers[i]] = d3List[random.randint(0, len(d3List)-1)].strip('\n') + " " + accused + "!"
        
        # Append user's dialogue if any
        if (playerLine != "no"):
            dialogue[playerName] = playerLine
        
        # Print the dialogue
        for name in dialogue:
            print(mag(name + ": ") + dialogue[name])
            time.sleep(2)
        
        print()
        input(blue("After some discussion, everyone was able to narrow it down to ") + yel("these 3 people:"))
        print()
        # Determine the 3 to vote on, include the killer
        bottom3 = []
        killerIndex = random.randint(0,2)
        bottom3Votes = [0, 0, 0]
        for i in range(3):
            if (i == killerIndex):
                bottom3.append(killer)
            else:
                innocent = random.choice(list(alive.keys()))

                # Make sure it's not the killer or a repeat
                while (innocent == killer or innocent in bottom3):
                    innocent = random.choice(list(alive.keys()))
                
                bottom3.append(innocent)

        j = 1
        for i in bottom3:
            print("Choice " + str(j) + ": " + mag(i) + cyan(" the ") + yel(students[i]))
            time.sleep(0.25)
            j += 1
        
        # Determine votes
        numVotes = len(alive)
        print()

        # Player vote
        if (playerName in alive):
            numVotes -= 1
            playerVote = int(input(cyan("Well, ") + playerName + cyan(", who will you vote for? (type their number): ")))

            while (playerVote < 1 or playerVote > 3):
                playerVote = int(input(cyan("That isn't one of the choices. Type it in again (their number): ")))
            
            bottom3Votes[playerVote-1] += 1
            print()
            
        # Determine everyone else's votes
        # TODO - Make this more complicated based on relationships/other factors during free time
        for i in range(numVotes):
            cpuChoice = random.randint(0, 2)
            bottom3Votes[cpuChoice] += 1
    
        time.sleep(1)
        input(blue("The votes are in..."))
        input(blue("Who did you all choose to be the blackened?"))

        # Determine the blackened
        maxIndex = 0
        for i in range(1, 3):
            if bottom3Votes[maxIndex] < bottom3Votes[i]:
                maxIndex = i
            elif bottom3Votes[maxIndex] == bottom3Votes[i]:
                input(blue("Looks like there was a tie... oh well! I'll just choose someone at random!"))
                if (random.randint(0, 1) == 0):
                    maxIndex = i

        # Print out final vote
        for i in range(3):
            print(mag(bottom3[i]) + cyan(" the ") + yel(students[bottom3[i]]) + " === (" + str(bottom3Votes[i]) + ")")
            time.sleep(0.25)
        
        print()
        loser = bottom3[maxIndex]

        input(mag(loser) + cyan(" the ") + yel(students[loser]) + blue("!!!"))
        
        if (loser == killer):
            input(blue("Congrats everyone! They were the ") + yel("true killer!"))
            records[loser] = "Executed"
        else:
            input(blue("Puhuhu... the ") + yel("true killer ") + blue("got away with this one..."))
            if (killer == playerName):
                input(red("Lucky one, aren't ya?"))
            records[loser] = "Wrongfully Executed " + "(true killer was " + killer + ")"
        
        input(blue("I've got a special punishment for you!"))
        input(blue(loser + " was ") + red("punished") + blue(", and the game continued."))
        if (loser == playerName):
            input(red("Oops, you're DEAD. Puhuhu..."))
        alive.pop(loser)
        trialNum += 1
        killChance = 3
        
    
    # No killings
    else:
        input(blue("Good evening everyone! You all survived another day. Get some rest."))
        killChance -= 1
    
    # End the day
    dayNum += 1
    goToTrial = False
    time.sleep(1)
    printStudents(students, alive)
    time.sleep(1)
    print()

print(blue("All the remaining students were able to work together..."))
time.sleep(2)
print(blue("...and escaped the killing game!"))
print()
time.sleep(2)
print(colored("===================================================================================", "red"))
time.sleep(0.25)
print(colored("===================[ D A N G A N R O N P A     V - P Y T H O N ]===================", "red"))
time.sleep(0.25)
print(colored("===================================================================================", "red"))
time.sleep(0.25)
print(colored("================================[ G A M E    E N D ]===============================", "yellow"))
time.sleep(0.25)
print(colored("===================================================================================", "red"))
print()
time.sleep(2)
print(yel("SURVIVORS: "))
print(yel("--------------"))
time.sleep(1)
for name in alive:
    print(mag(name) + cyan(" the ") + yel(students[name]))
    time.sleep(0.25)
print()
time.sleep(2)
# Reverse the dictionary so order is accurate
records = dict(reversed(list(records.items())))

place = 2
print(red("DEATHS: "))
print(red("--------------"))
time.sleep(1)
for name in records:
    if (place == 3):
        suffix = "rd)"
    elif (place == 2):
        suffix = "nd)"
    else:
        suffix = "th)"
    print("(" + str(place) + suffix + " " + mag(name) + cyan(" the ") + yel(students[name]) + " === " + red(records[name]))
    place += 1
    time.sleep(0.25)
print()
#In this project, I will make a virtual pet game with fish!

from time import sleep
from random import randint

water = [] #an array to store the habitat of underwater pet
deadWater = []

#creating the water body
def createFish(fish):
    water.append(["~"] * 10)
    water.append([" " + str(fish)])
    water.append([" "] * 10)
    water.append(["~"] * 10)

#display only if fish has died
def deadFish(fish):
    deadWater.append(["~"] * 10)
    deadWater.append([" "] * 10)
    deadWater.append([" " + str(fish) + " RIP"])
    deadWater.append(["~"] * 10)

#function to print the board
def printBoard(board):
    for row in board:
        print ("".join(row))

Fish1 = '><((\'>'
Fish2 = '>O'
Fish3 = '>(>\')'
Turtle = '(__)o'

#prompting the user to choose a fish
def userChooseAnimal():
    print('You are buying an underwater pet . . .')
    sleep(1)
    print('1. {}\n2. {}\n3. {}\n4. {}'.format(Fish1,Fish2,Fish3,Turtle))
    
    animalChoice = input('Which animal to do you take?: ')
    if (animalChoice == '1'):
        return str(Fish1)
    elif (animalChoice == '2'):
        return str(Fish2)
    elif (animalChoice == '3'):
        return str(Fish3)
    elif (animalChoice == '4'):
        return str(Turtle)
    else:
        print('Not a valid animal.')
        return userChooseFish()

#function to keep track of fish's health
def health(currentHealth):
    health = currentHealth
    print('Health: {} / 10'.format(health))

    if (health <= 2):
        print('Your pet is sick!')
        choice = input('Take your pet to the vet? (Y or N): ')
        if choice == 'Y' or choice == 'y':
            print('You took your pet to the vet!')
            sleep(1)
            print('It feels much better now.')
            health += 10
        else:
            print('You decided not to take your pet to the vet.')
            health -= 1
    else:
        print('Your pet is in good health.')
    if (health == 0):
        print('. . .')
        print('Your pet got sick.')
        print('Your pet died!')

    return health

#function to keep track of hunger
def hunger(currentHunger):
    hunger = currentHunger
    print('Hunger: {} / 10'.format(hunger))

    if (hunger >= 8):
        print('Your pet is very hungry!')
        choice = input('Feed your pet? (Y or N): ')
        if choice == 'Y' or choice == 'y':
            print('You fed your pet!')
            sleep(1)
            print('It feels much better now.')
            hunger -= 10
        else:
            print('You decided not to feed your pet.')
            hunger += 1
    else:
        print('Your pet is not too hungry.')
    if (hunger == 10):
        print('. . .')
        print('Your pet starved.')
        print('Your pet died!')

    return hunger


#function to keep track of hunger
def happiness(currentHappiness):
    happiness = currentHappiness
    print('Happiness: {} / 10'.format(happiness))

    if (happiness <= 2):
        print('Your pet is unhappy!')
        choice = input('Play with your pet? (Y or N): ')
        if choice == 'Y' or choice == 'y':
            print('You played with your pet!')
            sleep(1)
            print('It is much happier now.')
            happiness += 10
        else:
            print('You decided not to play with your pet.')
            happiness -= 1
    else:
        print('Your pet is happy.')
    if (happiness == 0):
        print('. . .')
        print('Your pet took its own life.')
        print('Your pet died!')

    return happiness

#function to check on user's pet
def checkFishStatus():
    alive = True #the pet is alive
    currentHealth = randint(1,10) #random start health
    currentHunger = randint(1,10) #random start hunger
    currentHappiness = randint(1,10) #random start happiness
    
    while(alive):
        print('1. Check Health\n2. Check Hunger\n3. Check Happiness\n4. Abandon Pet')
        userOption = input('What would you like to do with your pet?: ')
        
        if userOption == '1':
            currentHealth = health(randint(1,currentHealth))
            print('. . . ')
            if (currentHealth == 0):
                alive = False #the pet is not alive
                
        elif userOption == '2':
            currentHunger = hunger(randint(currentHunger,10))
            print('. . . ')
            if (currentHunger == 10):
                alive = False #the pet is not alive
            
        elif userOption == '3':
            currentHappiness = happiness(randint(1,currentHappiness))
            print('. . . ')
            if (currentHappiness == 0):
                alive = False #the pet is not alive
            
        elif userOption == '4':
            print('You\'ve abandoned your pet! It died.')
            alive = False #the pet is not alive
            
        else:
            print('Invalid option.')
            return checkFishStatus()

def replay():
    choice = input('Would you like to play again? (Y or N): ')
    if (choice == 'y' or choice == 'Y'):
        return True
    elif (choice == 'n' or choice == 'N'):
        return False
    else:
        print('Not a valid option.')
        return replay()

#defining the actual game
def Game():
    i = 0
    animal = userChooseAnimal() #user chooses a pet
    sleep(1)

    #creating the pet
    createFish(animal)
    printBoard(water)
    
    print('This is your pet.')
    print('. . .')

    #allowing user to choose what they want with their fish
    checkFishStatus()
    print('. . .')
    return animal

#setting a variable to true
play = True

#while play is true, user will continue to play the game
while (play):
    #setting game to a variable fish
    fish = Game()
    
    #game ends when fish dies
    deadFish(fish)
    printBoard(deadWater)
    play = replay()

print('Thank you for playing my virtual pet game!')


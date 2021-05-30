# PlayGame.py
from RoomAdventure import *
import random
# Create item objects from Item class
Sword = Item('Starter Sword','Weapon','A handy shiny weapon')
Axe =  Item('Rusty Axe','Weapon','An axe whose state seems deplorable at best')
Pickaxe = Item('Incredible Pickaxe','Weapon','An incredible pickaxe')
Staff = Item('Starter Staff','Weapon','A handy weapon that does magic')
Medal = Item('Gold Medal','Artifact','A medal made out of Gold')
Potion = Item('Unknown Potion','Consumable','A potion whose recipe is unknown')
Dynamite = Item('Dynamite','Explosive','An item with incredible destructive power')
Fire_SpellBook = Item('Fire Spell Book','Spell','A spell book with the power to light things up on fire')
Water_SpellBook = Item('Water Spell Book','Spell','A spell book with the power to flood an entire room')
Flag = Item('Flag','Salvageable','A flag that if you salvage gives you cloth in return')
# Create room objects from Room class
StarterRoom = Room(['North','West','East','South'],"Starters Room", 'Start')
NorthRoom = Room(['Start','North West','North East','Puzzle'], "North Room", 'North')
NorthEastRoom = Room(['North','East'], "North East Room", 'North East')
NorthWestRoom = Room(['North','West'], "North West Room", 'North West')
EastRoom = Room(['Start','North East','South East'], "East Room", 'East')
WestRoom = Room(['Start','North West','South West'], "West Room",'West')
SouthRoom = Room(['Start','South East','South West'], "South Room", 'South')
SouthEastRoom = Room(['South','East'], "South East Room",'South East')
SouthWestRoom = Room(['South','West'], "South West Room", 'South West')
PuzzleRoom = Room(['North'],
                  'Puzzle Room, in order to solve the puzzle you need to place the correct items',
                  'Puzzle')
# Add items to those rooms
StarterRoom.build([Sword, Staff])
NorthRoom.build([Pickaxe])
NorthEastRoom.build([Potion])
NorthWestRoom.build([Fire_SpellBook])
EastRoom.build([Dynamite])
WestRoom.build([Axe])
SouthRoom.build([Medal])
SouthEastRoom.build([Flag])
SouthWestRoom.build([Water_SpellBook])

# Create player object from Player Class and assign it a starting Room by retrieving the location of the Room.
MainPlayer = Player("", StarterRoom.getLocation())

room_list = [StarterRoom, NorthRoom, NorthEastRoom, NorthWestRoom, EastRoom, WestRoom, SouthRoom, SouthEastRoom,
             SouthWestRoom, PuzzleRoom]


# Keep program updated by letting it know where the player is.
def find_room(roomList, playerLocation):
    for room in roomList:
        if room.getLocation() == playerLocation:
            return room

# This function chooses a random riddle from a dictionary.
def question_chooser(dictionary):
    questions = random.choice(list(dictionary))
    solutions = dictionary.get(questions)
    dictionary = {questions: solutions}

    return dictionary
# This function checks whether the user has successfully solved the puzzle
def isSolved(pl,sol):
    an = dict()
    an['Placed'] = pl

    if set(list(an.values())[0]) == set(list(sol.values())[0]):

        print('Items Placed:', set(list(an.values())[0]))
        print('Solution:', set(list(sol.values())[0]))

        return True

    else:
        return False

player_action = ''
# list of actions available to the user
actions = ['choose direction','pick up item','exit game','inventory']
# Dictionary with riddles paired with their solutions
questions_sol = {'What does a Wizard usually carry with him?': ['Starter Staff','Fire Spell Book','Water Spell Book'],
                 'Its name comes from the Greek word that means power': ['Dynamite'],
                 'Has to do with alchemy': ['Unknown Potion'],
                 'Something you are proud of':['Gold Medal'],
                 'Minecrafts most iconic tool':['Incredible Pickaxe'],
                 'Notorious for having been used as a weapon by vikings': ['Rusty Axe'],
                 'Soldiers toolkit': ['Starter Sword','Flag']}

selected_question = question_chooser(questions_sol)

print('Player is in',MainPlayer.position)
print(StarterRoom.getDesc())
print(StarterRoom.showItems())

# Keep the program running until player action is equal to Exit
while player_action != 'Exit':
    checkLoc = MainPlayer.position
    player_action = str(input("Enter action:\n1. choose direction\n2. pick up item\n3. inventory\n4. exit game\n"))

    currentRoom = find_room(room_list, MainPlayer.position)

    if player_action not in actions:
        print('Invalid Action, Please Try Again')

    elif player_action == 'exit game':
        print('Thank you for playing')
        player_action = 'Exit'

    elif player_action == 'inventory':

        MainPlayer.showInventory()

    elif player_action == 'pick up item':
        player_action = str(input("Which item do you wish to pick up:\n"))
        # If player action does not match any of the items in current room, print invalid item
        if player_action not in [i.getIname() for i in currentRoom.items]:

            print("Invalid item")

        else:
            # otherwise add item to inventory
            print("Player successfully picked up {}".format(player_action))
            MainPlayer.addItem(player_action)
            currentRoom.removeItem(player_action)

    else:
        player_action = str(input("Which direction do you want to go: {} \n".format(currentRoom.doors)))
        if player_action not in currentRoom.doors:
            print('Unable to go in that direction')

        else:
            MainPlayer.setPosition(player_action)
            print('Player is in',MainPlayer.position)
            currentRoom = find_room(room_list, MainPlayer.position)
            print(currentRoom.getDesc())
            print(currentRoom.showItems())

            if MainPlayer.position == 'Puzzle':
                print('Puzzle Riddle:',list(selected_question.keys())[0])
                player_action = str(input("Would you like to try solving the puzzle: "))


                if player_action == 'yes':
                    placed = []
                    while player_action != 'quit':
                        print('Puzzle Riddle:',list(selected_question.keys())[0])
                        player_action = str(input("1. place items \n2. solve puzzle \n3. quit\n"))

                        if player_action == 'place items':

                            MainPlayer.showInventory()

                            player_action = str(input("Choose items you would like to place:\n"))

                            if player_action not in MainPlayer.inventory:
                                print('Invalid Item')

                            else:

                                placed.append(player_action)
                                MainPlayer.discard(player_action)
                                print('Currently placed items:',placed)


                        elif player_action == 'solve puzzle':
                            print('Currently placed items:',placed)

                            if isSolved(placed,selected_question):

                                print('Congratulations, you solved the Puzzle')
                                exit()

                            else:
                                print('Incorrect answer, please try again')

                                for i in placed:
                                    MainPlayer.addItem(i)

                                placed.clear()

                        elif player_action == 'quit':

                            for i in placed:
                                MainPlayer.addItem(i)

                            placed.clear()



                        else:
                            print('Invalid Action')




                else:
                    print("Returning to game")
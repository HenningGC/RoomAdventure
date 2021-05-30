# RoomAdventure.py

# Item Class
class Item:
    # Instanced Variables, includes name of item, type and description
    def __init__(self, iname, type, description):

        self.iname = iname
        self.type = type
        self.description = description
    # Method to print description
    def getDescription(self):

        return("Item: {}, Type: {}, Description: {}".format(self.iname,self.type,self.description))
    # Method to retrieve name of item
    def getIname(self):

        return self.iname

# Player Class, has the ability to return position, add item to inventory, discard item, show items in inventory
# and pick up items
class Player:

    def __init__(self, name, position):

        self.name = name
        self.position = position
        self.inventory = [] # Inventory in the form of list

    def getName(self):
        return self.name

    def setName(self,value):
        self.name = value

    def getPosition(self):
        return self.position

    def setPosition(self, value):
        self.position = value

    def addItem(self, value):

        self.inventory.append(value)

    def discard(self, value):

        self.inventory.remove(value)

    def showInventory(self):
        # if inventory is empty, print a message that tells the user that the inventory list is empty
        if not self.inventory:
            print("Inventory is empty")
        # otherwise print the player's name and its inventory
        else:
            print("{}'s inventory: \n{}".format(self.name,self.inventory))

# Room class
class Room:
    # Includes the following variables: doors (exits the Room has), description, location of said Room
    # Also includes an instanced Method where everytime it is entered, it shows a list of items that can be found in
    # the Room
    def __init__(self,doors, desc, location):

        self.doors = doors
        self.desc = desc
        self.location = location
        self.items = []
        self.showItems()

    def getDesc(self):

        return self.desc

    def getLocation(self):

        return self.location

    def getDoors(self):

        return self.doors

    # if player picks up an item from a Room, remove item from Room.
    def removeItem(self, value):

        for i in self.items:
            if i.getIname() == value:
                self.items.remove(i)
    # Add items to room
    def build(self, values):

        for n in values:
            self.items.append(n)

    # For items in the Room, print a description from said items
    def showItems(self):

        for item in self.items:
            print(item.getDescription())
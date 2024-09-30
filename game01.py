import sys
import random 
import time

# Player config. Only items will be of use in this game.
# Stone and Wood will be appended to "items" later on in the game
# stone_count and wood_count will be called to print the amount the player currently has.
player = { 
    "items" : ["[Shortsword]","[Pickaxe]","[Axe]"],
    "stone_count": 0,
    "wood_count": 0,
}

# Function to print text per character and to define the speed at which it prints out.
def char_print(text, charDelay=0.025):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(charDelay)

# Function that will be used for the entire game, calls on char_print and defines delay before the next line prints.
def funky_print(text, delay=0.5):
    char_print(text + "\n")
    time.sleep(delay)

# Function that is used for input. Also strips all letter cases from the player input to ensure it matches the boolean definition.
def funky_input(text):
    funky_print(text)
    return input().strip().lower()

# Praise be RNGesus
def rollDice(minNum, maxNum):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print ("You roll a: " + str(result) + " out of " + str(maxNum))

    return result


def title():
    funky_print("Welcome to Terraria.",)
    funky_print("Not really, it's a text based attempt of it.",)
    funky_print("That's because the person programming this can't code for jackshit.\n",)
    funky_print("But he will get there one day.\n",)
    funky_print("Before we proceed, let's lay some ground rules.",1)
    groundRules()


def groundRules():
    funky_print("This game is choice based and will require you, as the player,", 0)
    funky_print("to input the number of the option presented to progress.\n",1)
    playerInput = funky_input("[1] Gotcha\n" + "[2] No Bueno\n")

    if playerInput == "1":
        funky_print("Sweet, you're a sharp one aren't you.")
        funky_input("Shall we proceed? [Press Enter]")
        intro()

    else:
        cmonMan()
        groundRules()

# This function will be called throughout the game as the default fallback route should there be an errant input.
def cmonMan():
    funky_print("Cmon man, you gotta respond with either 1 or 2, let's try again.")

def intro():
    funky_print("You find yourself in a forest clearing")
    funky_print("To your right you see \"Guide\".") 
    funky_print("He idly paces back and forth, surely he will be of help in the future.")
    inventory()

# This is a stage of the game that follows from above.    
def inventory():
    funky_print("You check to see what you currently have on you\n")
    playerInput = funky_input("[1] Open Inventory\n" + "[2] Do Nothing\n")
    
    if playerInput == "1":
        inventoryOpen()

    elif playerInput == "2": 
        funky_print("You decide not to open your inventory")
        funky_print("Unsure of what you are equipped to handle, you ponder proceeding forward round the forest clearing")
        playerInput = funky_input("Do you proceed without checking your inventory?\n\n"\
            + "[1] Proceed\n" + "[2] Check Inventory\n")

        if playerInput == "1":
            postIntro()

        else:
            funky_print("That was wise of you")
            inventoryOpen()

    else: 
        cmonMan()
        inventory()

def inventoryOpen():
    funky_print("You open your inventory and see the following items: \n" + listInventory())
    funky_print("You feel well equipped as you buckle the flap of your rucksack",1)
    postIntro()

# This is a function that will be called throughout the game to list what is currently in player["items"]
# It starts off by removing Stone and Wood from the inventory.
# Then it prints the inventory, and IF player has stone and wood which will mean the counts are > 0, it will append stone and wood
# back to the inventory list but with the current count as a string. 
def listInventory():
    items = player['items']
    
    if player['stone_count'] > 0:
        items.remove("[Stone]")
    if player['wood_count'] > 0:
        items.remove("[Wood]")

    inventory = " | ".join(player['items'])
    
    if player['stone_count'] > 0:
        inventory += " | " + str(player['stone_count']) + " [Stone]"
    if player['wood_count'] > 0:
        inventory += " | " + str(player['wood_count']) + " [Wood]"

    return inventory

def postIntro():
    funky_print("It will soon be dark")
    funky_print("You get a sinking feeling knowing you will not survive the night without shelter.")
    funky_print("You look around and find yourself surrounded by thick trees for miles.")
    funky_print("At your feet, there's hard rock")
    gatherMats()

# A simple function that calls upon the ['items'] that player has as defined at the beginning of the program. 
def gatherMats():
    playerInput = funky_input("You reach for your\n\n" + "[1]" + player['items'][1] + "\n" + "[2]" + player['items'][2] + "\n")
    
    if playerInput == "1":
        funky_print("Pickaxe in hand, you begin to hack at the rock at your feet.")
        stoneMining()


    elif playerInput == "2":
        funky_print("Axe in hand, you begin to chop at the tree closest to you.")
        woodChopping()
    
    else: 
        cmonMan()
        gatherMats()

# A core mechanic of the game.
# It starts off with an RNG that returns a value of 2-5.
# The player will obtain 2-5 stone per attempt.
# Upon obtaining stone, appends to ["items"] and also adds to ['stone_count']        
def stoneMining():
    stone = random.randint(2,5)
    funky_print("Tic...",.7)
    funky_print("Tic...",.7)
    funky_print("Tic...",.7)
    funky_print("\nYou obtain " + str(stone) + " stone!")
    player["items"].append("[Stone]")
    player['stone_count'] += stone
    funky_print("You have a total of " + str(player['stone_count']) + " stone")

    # This checks if the player chose to gather wood first, and forks out to provide slightly different options.
    if "[Wood]" in player['items']: 
        stoneMiningHaveWood()

    # This assumes the player chose to mine stone first. 
    else:
        playerInput = funky_input("\n[1] Mine more Stone" + "\n[2] I'm done gathering Stone")
        if playerInput == "1":
            stoneMining()

        # This returns the player to the choice to mine stone or chop wood.
        elif playerInput =="2":
            gatherMats()

# This is the forked function that presents itself when the player possesses both stone and wood
# and then provides options that would progress the game. 
def stoneMiningHaveWood():
    playerInput = funky_input("\nIt seems like you have both Stone and Wood.\n" + \
            "\n[1] Mine more Stone" + "\n[2] Chop for more Wood" + \
            "\n[3] I'm done gathering Materials" + "\n[4] Check Inventory\n")
        
    if playerInput == "1":
        stoneMining()

    elif playerInput == "2":
        woodChopping()

    elif playerInput == "3":
        haveStoneAndWood()
        postGatherMats()

    elif playerInput== "4":
        funky_print("You look within your rucksack and find" + listInventory())
        stoneMiningHaveWood()

# Wood chopping mechanic of the game.
# Follows the same logic as stone mining.
def woodChopping():
    wood = random.randint(2,5)
    funky_print("Twack!",.7)
    funky_print("Twack!",.7)
    funky_print("Twack!",.7)
    funky_print("\nYou obtain " + str(wood) + " wood!")
    player["items"].append("[Wood]")
    player['wood_count'] += wood
    funky_print("You have a total of " + str(player['wood_count']) + " wood")

    if "[Stone]" in player['items']: 
        woodChoppingHaveStone()

    else:
        playerInput = funky_input("\n[1]Chop for more wood\n" + "[2] I'm done gathering Wood")
        if playerInput == "1":
            woodChopping()

        elif playerInput == "2":
            gatherMats()

def woodChoppingHaveStone():
    playerInput = funky_input("\nIt seems like you have both Stone and Wood.\n" + \
        "\n[1] Chop for more Wood" + "\n[2] Mine for more Stone" + \
        "\n[3] I'm done gathering Materials" + "\n[4] Check Inventory\n")

    if playerInput == "1":
        woodChopping()
            
    elif playerInput == "2":
        stoneMining()

    elif playerInput == "3":
        haveStoneAndWood()
        postGatherMats()

    elif playerInput == "4":
        funky_print("You look within your rucksack and find " + listInventory())
        woodChoppingHaveStone()

# A derivative of listInventory() that just prints stone and wood instead of the entire inventory.
def countMats():
    funky_print("You look within your rucksack and find a total of "+ \
        str(player['stone_count']) + " stone and "+ \
        str(player['wood_count']) + " wood.")

def haveStoneAndWood():
    funky_print("Phew, you feel yourself weighed down with Stone and Wood")
    countMats()
    funky_print("It is time to put them to good use.")
    postGatherMats()

def postGatherMats():
    funky_print("You start to think of the logistics of building a shelter, " +\
        "and come to a realisation that you will require 5 stone and 15 wood.")
    postGatherMatsOpt()

# The fork in the path for the second core mechanic of the game.
def postGatherMatsOpt():
    playerInput = funky_input("\n[1] Build Shelter\n" + "[2] Check Inventory\n" + "[3] Gather more materials\n")

    if playerInput == "1":
        buildShelter()

    elif playerInput == "2":
        countMats()
        funky_print("You require 5 stone and 15 wood to construct the shelter")
        postGatherMatsOpt()

    elif playerInput == "3":
        gatherMats()

    else: 
        cmonMan()
        postGatherMats()

# The second core mechanic of the game.
# This function checks if the player has 5 stone and 15 wood.
def buildShelter():
    
    # This checks if the player has sufficient stone but not enough wood.
    if player['stone_count'] >= 5 and player ['wood_count'] < 15:
        funky_print("With a slap to the forehead, you realise that you do not have enough resources to construct the shelter.")

        # This then prints out exactly how much more wood the player requires.
        funky_print("You have enough stone but require " + \
            str(15 - player['wood_count']) + " more wood.")

        # This returns the player back to the option of gathering materials.
        postGatherMatsOpt()

    # This checks if the player has sufficient wood but not enough stone.
    elif player['stone_count'] < 5 and player ['wood_count'] >= 15:
        funky_print("With a slap to the forehead, you realise that you do not have enough resources to construct the shelter.")

        # This then prints out exactly how much more stone the player requires.
        funky_print("You have enough wood but require " + \
            str(5 - player['stone_count']) + " more stone.")
        
        # This returns the player back to the option of gathering materials.
        postGatherMatsOpt()

    # This checks if the player has both insufficient stone and wood.
    elif player['stone_count'] < 5 or player ['wood_count'] < 15:
        funky_print("With a slap to the forehead, you realise that you do not have enough resources to construct the shelter.")
        funky_print(str(5 - player['stone_count']) + " more stone and " + \
            str(15 - player['wood_count']) + " more wood is what you currently require.")
        postGatherMatsOpt()

    # If all of the above are false, it means the player has enough stone and wood.
    # Proceed to build.
    else:
        build()

def build():
    funky_print("With sufficient materials in hand, you map out the structure in your head.\n")
    playerInput = funky_input("You decide to:\n" + "[1] Lay the stone foundation.\n" + "[2] Build the four wooden walls")
    if playerInput == "1":
        stoneBuild()

    elif playerInput== "2":
        funky_print("That ain't quite right, the walls will not stand without a foundation.")
        funky_print("You resign yourself to laying the foundation, even if it wasn't your initial intention.")
        stoneBuild()

    else:
        cmonMan()
        build()

# A derivative of the char_print function but further delayed to represent the slow printing of the blocks.
def char_print_build(text, charDelay=0.5):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(charDelay)

# I'm done with this.
def stoneBuild():
    char_print_build("■ ■ ■ ■ ■\n")
    funky_print("Well done! Consider the shelter well built with both you and \"Guide\"  having moved in and are safe from the surroundings and night.")
    funky_print("I would like to take the time now to learn more about P5.js and Loops and as such, this will be how the game ends.")
    funky_print("Peace out.\n",1)
    title()

def main():
    title()

main()


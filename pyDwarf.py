#!/usr/bin/python3.4
#-----------------------------------------------------------------------------------------------
# Name:        A tunnel building program for the avid Minecraft Pi dwarf.
# Purpose:     Designed to build descending, ascending and straight tunnels in Minecraft Pi.
#              This is written very simply for debugging/learning purposes.
#              Most of this code is designed to handle user input.
#              Eventually this will be integrated into a user interface with QT and pyQT.
# Version:     Development
# Author:      benjo charlie
# Created:     2016
#              This is an octothorp # Spread the word.
#-----------------------------------------------------------------------------------------------


# Import libraries and set up the globals
import mcpi.minecraft as minecraft
from random import randrange
mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()

mc.postToChat("Immeasurable halls, filled with an everlasting music of")
mc.postToChat("water that tinkles into pools, as fair as Kheled-Zaram")
mc.postToChat("in the starlight.")


#############################################################################################################


class UserInput(object):

    # Get the data from the user:
    def getinput(self, i):
        # Python likes a Global declared in every DEF to be sure you know what you're playing with.
        global tunnel
        global compass
        global length
        global elevation
        global deep
        elevation = "Z"

        # Loop through the options until all requirements are satisfied.
        while i:
            if i == 1:
                tunnel = input("\nWhat type of tunnel are we building, a Hallway or Steps? H, S >> ")
                if tunnel in ("H", "S", "h", "s", "hall", "stairs"):
                    if tunnel in ("H", "h", "hall"):
                        tunnel = "H"
                        i += 2
                        tunneltype="Hallway"
                        # Debug: print(tunneltype)
                    elif tunnel in ("S", "s", "stairs"):
                        tunnel = "S"
                        i += 1
                        tunneltype = "Stairwell"
                        # Debug: print(tunneltype)
                else:
                    print("Usage ", i)
                    i = printscreen.usage(1)
            elif i == 2:
                if tunnel in ("S", "s", "stairs"):
                    elevation = input("\nDo you want the stairs to go up or down? U,D >> ")
                    if elevation in ("U", "D", "u", "d", "Up", "Down", "up", "down"):
                        if elevation in ("U", "u", "Up", "up"):
                            elevation = "U"
                        elif elevation in ("D", "d", "Down", "down"):
                            elevation = "D"
                        i += 2
                    else:
                        i = printscreen.usage(2)
                else:
                    i += 2

            elif i == 3:
                if tunnel == "H":
                    elevation = input("\nDo you want a Glass Hallway or Lighted? G,L >> ")
                    if elevation in ("G", "L", "g", "l", "glass", "lighted", "Glass", "Lighted"):
                        i += 1
                        if elevation in ("G", "g", "glass", "Glass"):
                            elevation = "G"
                        elif elevation in ("L", "l", "lighted", "Lighted"):
                            elevation = "L"
                    else:
                        i = printscreen.usage(3)
                        print("Usage ", i)
            elif i == 4:
                compass = input("\nWhat direction shall we dig? N,E,S or W? >> ")
                if compass in ("N", "E", "S", "W", "n", "e", "s", "w", "north", "east", "south", "west"):
                    i += 1
                    if compass in ("N", "n", "north"):
                        compass = "N"
                        direction = "Northerly"
                    elif compass in ("E", "e", "east"):
                        compass = "E"
                        direction = "Easterly"
                    elif compass in ("S", "s", "south"):
                        compass = "S"
                        direction = "Southerly"
                    elif compass in ("W", "w", "west"):
                        compass = "W"
                        direction = "Westerly"
                else:
                    i = printscreen.usage(4)
                    print("Usage ", i)
            elif i == 5:
                while True:
                    try:
                        print("\nHow deep/far do you want to dig?\n")
                        length = int(input("[keypad] 1-128 >> "))
                        if length in (range(1, 129)):
                            break
                    except:
                        i = printscreen.usage(5)
                
                deep = length
                i += 1
            else:
                print("\n *** Building a ", tunneltype, ",", deep, "blocks deep in a ", direction, " direction. ***\n")
                return length, compass, elevation


#############################################################################################################


class OutputToScreen(object):

    def usage(self, u):
        if u == 1:
            print("""\
    Usage: Tunnel type [H, S]
         -H Hallway               Build a hallway type tunnel 
         -S Steps                 Build a stairwell type tunnel 
    """)
            return 1
        elif u == 2:
            print("""\
    Usage: Up or Down [U, D]
         -U Upward staircase      Build a stairwell going up 45 degrees 
         -D Downward staircase    Build a stairwell going down 45 degrees 
    """)
            return 2
        elif u == 3:
            print("""\
    Usage: Glass or Lighted [G, L]
         -G Glass Walls           Build a hallway with glass walls 
         -L Glowstone Walls       Build a hallway with Glowstone 
    """)
            return 3
        elif u == 4:
            print("""\
    Usage: Direction [N, E, S, W]
         -N North                 Build a tunnel in the northern direction 
         -E East                  Build a tunnel in the eastern direction 
         -S South                 Build a tunnel in the southern direction 
         -W West                  Build a tunnel in the western direction 
    """)
            return 4
        elif u == 5:
            print("""\
    Usage: Length [1-128]
         -Integer input ranging 1-128
    """)
            mc.postToChat("The Dwarves delved too greedily and too deep.")
            return 5
        else:
            print("Something went terribly wrong. We shouldn't be here!!!")
            mc.postToChat("This new Gandalf is more grumpy than the old one.")
            raise SystemExit


    # Random dwarf quote generator
    def gimli(self):
        
        # Everyone should have a Random dwarf quote generator.
        quote = [
            "I'm always last, and I don't like it.",
            "Faithless is he who says farewell when the road darkens.",
            "They had no honor in life. They have none now in death.",
            "Whatever luck you live by... let's hope it lasts the night.",
            "It's true you don't see many dwarf women. And in fact, "
            "they are so alike in voice and appearance, that they "
            "are often mistaken for dwarf men.",
            "I cannot jump the distance, you'll have to toss me.",
            "And you know what this Dwarf says to that? Ishkhaqwi ai durugnul! I spit upon your grave!",
            "There is some good stonework here.",
            "You may do as you please in madness.",
            "I have but returned to take what is mine; for I am the last of my people.",
            "The new Gandalf is grumpier than the old one.", 
            "The Dwarves delved too greedily and too deep."
            "The air must be thin up there, elf, for ye are daft to come up with that plan"
            "Never turn down an ale, who knows if it may be your last."
            "Her beard is winking at me."
            "Wherever there are elves, there are lies!"
            "Nothing a hammer can't solve."
            "You can kill a dwarf, but you can never vanquish one!"
            "The stones will sing if you let them."
            "Dwarven women are like axes. As dangerous from the back as from the front."
            "A mead in the hand, is worth two goblin heads in the bush."
            "Leave iron to rest before you hammer it."
            "You are softer than sandstone and drier than talc!"
            "Cave toads speak little, but when they do, listen."
            "A pebble will stay dry inside, no matter how long it is submerged in a pool of water."
            "Nothing evens a race like an axe to the kneecaps."
            "The smallest pebble was once the biggest stone, the biggest stone was once bigger."]

        mc.postToChat(quote[randrange(0, len(quote))])


#############################################################################################################


class DwarfMiner(object):

    # Define 'drill' function
    def drill(self, L, D, A):

        # Set up the local variables.
        # Blocks are assigned from bottom left to upper right.
        # y1 is player level, y2 is up.
        # Default to MELONS for debuging
        roofBlock=103
        floorBlock=103
        wallBlock=103
        x1, y1, z1 = mc.player.getPos()
        x2, y2, z2 = x1, y1+2, z1
        R, F = 0, 0

        # xz1, xz2 : Set the step width (block breadth) to 5 blocks wide corresponding to direction.
        # R, F     : Set the roof and floor steps data value to correspond with the direction.
        if D == "N":
            x1, x2, R, F = x1-2, x1+2, 7, 2
        elif D == "E":
            z1, z2, R, F = z1-2, z1+2, 4, 1
        elif D == "S":
            x1, x2, R, F = x1+2, x1-2, 6, 3
        elif D == "W":
            z1, z2, R, F = z1+2, z1-2, 5, 0

        # Set the tiles for step type construction and orientate to corresponding direction.
        if A in ("U", "D"):
            roofBlock=156
            floorBlock=156
            wallBlock=89
            if A == "U":
                if D == "N":
                    R, F = 6, 3
                elif D == "E":
                    R, F = 5, 0
                elif D == "S":
                    R, F = 7, 2
                elif D == "W":
                    R, F = 4, 1
            elif A == "D":
                if D == "N":
                    R, F = 7, 2
                elif D == "E":
                    R, F = 4, 1
                elif D == "S":
                    R, F = 6, 3
                elif D == "W":
                    R, F = 5, 0
            else:
                #set to NETHER REACTOR CORE for debuging if things went terribly wrong.
                wallBlock=247
                roofBlock=247
                floorBlock=247

        if A in ("L", "G"):
            R, F = 0, 0
            if A == "L":
                wallBlock=89
                roofBlock=155
                floorBlock=155
            elif A == "G":
                wallBlock=20
                roofBlock=20
                floorBlock=20
            else:
                #set to CACTUS for debuging if things went terribly wrong.
                wallBlock=81
                roofBlock=81
                floorBlock=81

        # Build it
        for n in range(1, L):

            # xz1, xz2 : Set the step depth and starting point corresponding to direction
            if D == "N":
                z1, z2, = z1-1, z1-1
            elif D == "E":
                x1, x2, = x1+1, x1+1
            elif D == "S":
                z1, z2, = z1+1, z1+1
            elif D == "W":
                x1, x2, = x1-1, x1-1

            # Build the Roof-Floor-Tunnel-Walls using one 5x5x1 block at a time
            # Set the roof tiles. We do this first to stop that nasty sand falling in!
            mc.setBlocks(x1, y2+1, z1, x2, y2+1, z2, roofBlock, R)

            # Set the floor tiles.
            mc.setBlocks(x1, y1-1, z1, x2, y1-1, z2, floorBlock, F)

            # Dig between floor/roof tiles with a 3Wx3H block for each loop.
            mc.setBlocks(x1, y1, z1, x2, y2, z2, 0)

            # Build the walls.
            mc.setBlocks(x1, y1-1, z1, x1, y2+1, z1, wallBlock)
            mc.setBlocks(x2, y1-1, z2, x2, y2+1, z2, wallBlock)

            # Decrement/Increment the depth by 1 block and reset height for next loop
            if A in ("U", "D"):
                if A == "U":
                    y1 += 1
                elif A == "D":
                    y1 -= 1
                y2 = y1 + 2


#############################################################################################################


# Run it
printscreen = OutputToScreen()
userinput = UserInput()
length, compass, elevation = userinput.getinput(1)
miner = DwarfMiner()
miner.drill(length, compass, elevation)
printscreen.gimli()

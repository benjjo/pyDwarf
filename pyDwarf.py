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
# ChangeLog:   Changed block type to 155 instead of gold and obsidian.
#              Overwite the last line of Roof / Floor blocks for stairs.
#-----------------------------------------------------------------------------------------------


# Import libraries and set up the globals
import mcpi.minecraft as minecraft
from random import randrange
mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
mc.postToChat("Immeasurable halls, filled with an everlasting music of  "
              "water that tinkles into pools, as fair as Kheled-Zaram   "
              "in the starlight.")


#############################################################################################################


# Get the data from the user:
def getinput(i):
    # Python likes a Global declared in every DEF to be sure you know what you're playing with.
    global tunnel
    global compass
    global length
    global elevation
    global deep
    elevation = "Z"
    while i:
        if i == 1:
            tunnel = input("What type of tunnel are we building, a Hallway or Steps? H, S >> ")
            if tunnel in ("H", "S"):
                if tunnel == "H":
                    i += 2
                    tunneltype="Hallway"
                    # Debug: print(tunneltype)
                elif tunnel == "S":
                    i += 1
                    tunneltype = "Stairwell"
                    # Debug: print(tunneltype)
            else:
                print("Usage ", i)
                i = usage(1)
        elif i == 2:
            if tunnel == "S":
                elevation = input("Do you want the stairs to go up or down? U,D >> ")
                if elevation in ("U", "D"):
                    i += 2
                    # Debug: print("Elevation is ", elevation)
                    # Debug: print("var i = ", i)
                else:
                    i = usage(2)
                    # Debug: print("Usage ", i)
            else:
                i += 2
                # Debug: print("How did we get here?")
            # Debug: print("Did we get here?")

        elif i == 3:
            if tunnel == "H":
                elevation = input("Do you want a Glass Hallway or Lighted? G,L >> ")
                if elevation in ("G", "L"):
                    i += 1
                else:
                    i = usage(3)
                    print("Usage ", i)
        elif i == 4:
            compass = input("What direction shall we dig? N,E,S or W? >> ")
            if compass in ("N", "E", "S", "W"):
                i += 1
                if compass == "N":
                    direction = "Northerly"
                elif compass == "E":
                    direction = "Easterly"
                elif compass == "S":
                    direction = "Southerly"
                elif compass == "W":
                    direction = "Westerly"
            else:
                i = usage(4)
                print("Usage ", i)
        elif i == 5:
            while True:
                try:
                    length = int(input("How deep/far do you want to dig? 1-256 >> "))
                    if length in (range(1, 257)):
                        break
                except:
                    i = usage(5)
                    # Debug: print("Except was passed")
            # Debug: print("The try loop broke here.")
            deep = length
            i += 1
        else:
            print(" *** Building a ", tunneltype, ", ", deep, " blocks deep in a ", direction, " direction. ***")
            break


#############################################################################################################


def usage(u):
    if u == 1:
        print("""\
Usage: Tunnel type [H, S]
     -H Hallway               Build a hallway type tunnel (Uppercase only)
     -S Steps                 Build a stairwell type tunnel (Uppercase only)
""")
        return 1
    elif u == 2:
        print("""\
Usage: Up or Down [U, D]
     -U Upward staircase      Build a stairwell going up 45 degrees (Uppercase only)
     -D Downward staircase    Build a stairwell going down 45 degrees (Uppercase only)
""")
        return 2
    elif u == 3:
        print("""\
Usage: Glass or Lighted [G, L]
     -G Glass Walls           Build a hallway with glass walls (Uppercase only)
     -L Glowstone Walls       Build a hallway with Glowstone (Uppercase only)
""")
        return 3
    elif u == 4:
        print("""\
Usage: Direction [N, E, S, W]
     -N North                 Build a tunnel in the northern direction (Uppercase only)
     -E East                  Build a tunnel in the eastern direction (Uppercase only)
     -S South                 Build a tunnel in the southern direction (Uppercase only)
     -W West                  Build a tunnel in the western direction (Uppercase only)
""")
        return 4
    elif u == 5:
        print("""\
Usage: Length [1-256]
     -Integer input ranging 1-256
""")
        mc.postToChat("The Dwarves delved too greedily and too deep.")
        return 5
    else:
        print("Something went terribly wrong. We shouldn't be here!!!")
        mc.postToChat("This new Gandalf is more grumpy than the old one.")
        raise SystemExit


#############################################################################################################


# Define 'drill' function
def drill(L, D, A):

    # Debug: print("L = ", L)
    # Debug: print("D = ", D)
    # Debug: print("A = ", A)
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

    gimli(randrange(10))


#############################################################################################################


# Random gimli quote generator
def gimli(n):

    # Everyone should have a Random Gimli quote generator.
    if n == 0:
        mc.postToChat("I'm always last, and I don't like it.")
    elif n == 1:
        mc.postToChat("Faithless is he who says farewell when the road          darkens.")
    elif n == 2:
        mc.postToChat("They had no honor in life. They have none now in death.")
    elif n == 3:
        mc.postToChat("Whatever luck you live by... let's hope it lasts the        night.")
    elif n == 4:
        mc.postToChat("It's true you don't see many dwarf women. And in fact,   "
                      "they are so alike in voice and appearance, that they     "
                      "are often mistaken for dwarf men.")
    elif n == 5:
        mc.postToChat("I cannot jump the distance, you'll have to toss me.")
    elif n == 6:
        mc.postToChat("And you know what this Dwarf says to that? Ishkhaqwi ai  durugnul! I spit upon your grave!")
    elif n == 7:
        mc.postToChat("There is some good stonework here.")
    elif n == 8:
        mc.postToChat("You may do as you please in madness.")
    else:
        mc.postToChat("I have but returned to take what is mine; for I am the   last of my people.")


#############################################################################################################


# Run the definitions
getinput(1)
print("Call the drill function.")
drill(length, compass, elevation)

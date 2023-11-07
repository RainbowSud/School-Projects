import random
import time

class Game:
    def __init__(self):
        self.__size = 22  # Used to calculate the size of the board - could be changed to any size of board if wanted
        self.__CGBoard = []  # Current Generation Board - Turns it into a list
        self.__NGBoard = []  # Next Generation Board - Turns it into a list

    def boardCreation(self):  # Creates a 2x2 array for both boards by adding lists into the original list
        for i in range(0, self.__size):
            self.__CGBoard.append([])
            self.__NGBoard.append([])

    def NGboardAddition(self):  # This adds only blanks to the Next Generation Board
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                self.__NGBoard[i].append(" ")

    def CGboardAddition(self):  # This adds blanks or Xs to the Current Generation Board 1/3 chance of being an X
        for i in range(0, self.__size):  # And a 2/3 chance to be a blank
            for j in range(0, self.__size):
                # This section here cuts off the outer edge of the board due to the assignment description
                if i == 0 or i == self.__size - 1:
                    self.__CGBoard[i].append(" ")
                elif j == 0 or j == self.__size - 1:
                    self.__CGBoard[i].append(" ")
                else:
                    # This section decides if the space will be filled with an X or a empty space
                    n = random.randint(1, 3)
                    if n == 3:
                        self.__CGBoard[i].append("X")
                    else:
                        self.__CGBoard[i].append(" ")

    def CGboardPrinting(self):  # This function simply prints out the board in a nice easy to see manner
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print(self.__CGBoard[i][j], end=" ")
            print()

    def NGequalCG(self):  # This function sets the Next Generation Board to be equal to the Current Generation Board
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                self.__NGBoard[i][j] = self.__CGBoard[i][j]

    def CGequalNG(self):  # This function sets the Current Generation Board to be equal to the Next Generation Board
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                self.__CGBoard[i][j] = self.__NGBoard[i][j]

    def nextGeneration(self):  # BIG BOY function, this does all of the logic for the game of life
        for i in range(1, self.__size - 1):
            for j in range(1, self.__size - 1):
                # This entire section checks all 8 adjacent pieces of the current piece at i, j
                # If there is an alive tile next to it that gets made noted in the counter n
                # If there is no alive tile then n stays 0 and moves onto the next section
                n = 0
                if self.__CGBoard[i + 1][j] == "X":
                    n += 1
                if self.__CGBoard[i - 1][j] == "X":
                    n += 1
                if self.__CGBoard[i][j + 1] == "X":
                    n += 1
                if self.__CGBoard[i][j - 1] == "X":
                    n += 1
                if self.__CGBoard[i-1][j-1] == "X":
                    n += 1
                if self.__CGBoard[i-1][j+1] == "X":
                    n += 1
                if self.__CGBoard[i+1][j-1] == "X":
                    n += 1
                if self.__CGBoard[i+1][j+1] == "X":
                    n += 1

                # This section here determines what to do based on how many alive tiles are next to the piece at i, j
                # Depending on the n value assigned from above
                # Note I set the next generation board based off of the current, so I can calculate every tile based
                # off of the current generation without messing anything up
                if n <= 1 and self.__CGBoard[i][j] == "X":  # Kills if n <= 1
                    self.__NGBoard[i][j] = " "
                if n == 3 and self.__CGBoard[i][j] == " ":  # Revives if n = 3 and it's a dead tile
                    self.__NGBoard[i][j] = "X"
                if n >= 4 and self.__CGBoard[i][j] == "X":  # Kills if n >= 4
                    self.__NGBoard[i][j] = " "


def main():  # Main function to run all the code
    gol = Game()  # Sets up my object
    gol.boardCreation()  # Creates the board
    gol.CGboardAddition()  # Assigns values to the Current Generation Board
    gol.NGboardAddition()  # Assigns values to the Next Generation Board
    gol.NGequalCG()  # Makes the Next Generation Board equal to the Current Generation Board
    gol.CGboardPrinting()  # Prints out the Current Generation Board
    print("Generation: 1")  # Labels for Gen 1
    gen = 1  # Gives a default value to this function I use in the While loop
    while gen < 50:  # While loop to run 50 generations of the game
        gol.nextGeneration()  # This runs the Next Generation calculation
        gol.CGequalNG()  # Sets the Current Generation equal to the Next Generation
        gol.CGboardPrinting()  # Prints out the Current Generation
        gen += 1  # Adds one to the generation
        print("Generation:", gen)  # Labels the generation
        time.sleep(.3)  # Spaces out the generations nicely


main()

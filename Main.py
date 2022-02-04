#Credit Goes to Luigiteam on GitHub
#https://github.com/Luigiteam/Python-SWN-Generator

import mainLine
import visual
from tkinter import *


def main():
    # SAVE: array[4] P[0],E[1], and M[2]. array [5] AC[0], and AB[1] 
    # array [6], Effort[0], FullName[1], Backprint[2], and BackprintNUM[3],
    # array [7][War[0], Exp[1], and Psy[2],
    # Credits[8],Equipment[9],
    # Array[10] hp[0], ss[1]
    
    Character = mainLine.Gen()

    print("\n")
    print(Character)
    print("\n")

    visual.Window(Character,1)


if __name__ == '__main__':
    main()

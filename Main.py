import mainLine
import visual
from tkinter import *


def main():
    # 0 - Att, 1 - NSkills, 2 - PsySkills, 3 - Foci, 4 - [0] Name [1] Background [2] Backnum
    # 5 - Credits, 6 - Equipment
    
    Character = mainLine.Gen()

    print("\n")
    print(Character)
    print("\n")

    visual.Window(Character)


if __name__ == '__main__':
    main()
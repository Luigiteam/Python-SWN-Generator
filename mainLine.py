#Credit Goes to Luigiteam on GitHub
#https://github.com/Luigiteam/Python-SWN-Generator

import gen
import random
import Main
import name_gen


def Gen():
    rollGrowth = None
    rollLearn = None
    run = True
    while run:
        rollGrowth = random.randint(1, 2)
        rollLearn = random.randint(1, 2)

        if rollGrowth + rollLearn == 3:
            run = False

    War = 0
    Psy = 0
    Exp = 0

    # Class
    a = 2
    while a > 0:
        rand = random.randint(1, 3)
        if rand == 1:
            War += 1

        if rand == 2:
            Psy += 1

        if rand == 3:
            Exp += 1
        a -= 1
    # Normal Skills set

    # Indexes: 0 - Admin, 1 - Connenct, 2 - Exert, 3 - Fix, 4 - Heal, 5 - Know, 6 - Lead, 7 - Notice, 8 - Perform, 9 - Pilot
    # 10 - Program, 11 - Punch, 12 - Shoot, 13 - Sneak, 14 - Stab, 15 - Survive, 16 - Talk, 17 - Trade, 18 - Work

    # Psychic Skills set
    # Indexes: 0 - Biosionics, 1 - Metapsionics, 2 - Precognition, 3 - Telekinesis, 4 - Telepathy, 5 - Teleportation

    # Attributes
    STR = gen.attribute_gen()
    DEX = gen.attribute_gen()
    CON = gen.attribute_gen()
    INT = gen.attribute_gen()
    WIS = gen.attribute_gen()
    CHA = gen.attribute_gen()

    # Random 14
    randomNum = [0,0,0,0,0,0]
    run = True
    a = 15
    while a > 0:
        while run:
            if randomNum == [-1,-1,-1,-1,-1,-1]:
                a = 0
                break
            
            rand = random.randint(1, 6)

            if randomNum[rand - 1] == 0:
                run = False
            
        if rand == 1 & STR < 14:
            STR = 14
            a = 0
        elif rand == 2 & DEX < 14:
            DEX = 14
            a = 0
        elif rand == 3 & CON < 14:
            CON = 14
            a = 0
        elif rand == 4 & INT < 14:
            INT = 14
            a = 0
        elif rand == 5 & WIS < 14:
            WIS = 14
            a = 0
        elif rand == 6 & CHA < 14:
            CHA = 14
            a = 0

        a -= 1

    # Background pick
    BackprintNUM = random.randint(1, 16)
    Backprint = gen.background_pick(BackprintNUM)
    print(str(Backprint) + " and " + str(BackprintNUM))

    # Background Growth and Learning tables
    Abillities = [[STR, DEX, CON, INT, WIS, CHA],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    Abillities = gen.background_table(BackprintNUM, rollGrowth, rollLearn, Abillities)

    # Attributes Reset
    STR = Abillities[0][0]
    DEX = Abillities[0][1]
    CON = Abillities[0][2]
    INT = Abillities[0][3]
    WIS = Abillities[0][4]
    CON = Abillities[0][5]

    # Att Mod seq
    STRmod = gen.attribute_mod(0, STR)
    strMOD = gen.attribute_mod(1, STR)

    DEXmod = gen.attribute_mod(0, DEX)
    dexMOD = gen.attribute_mod(1, DEX)

    CONmod = gen.attribute_mod(0, CON)
    conMOD = gen.attribute_mod(1, CON)

    INTmod = gen.attribute_mod(0, INT)
    intMOD = gen.attribute_mod(1, INT)

    WISmod = gen.attribute_mod(0, WIS)
    wisMOD = gen.attribute_mod(1, WIS)

    CHAmod = gen.attribute_mod(0, CHA)
    chaMOD = gen.attribute_mod(1, CHA)

    # Foci Stage
    skill_Check = [0,0,0,0,0,0,0,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0]

    Abillities,skill_Check = gen.Foci(0, Psy, Abillities, skill_Check)

    if Exp >= 1:
        Abillities,skill_Check = gen.Foci(2, Psy, Abillities, skill_Check)

    if War >= 1:
        Abillities,skill_Check = gen.Foci(1, Psy, Abillities, skill_Check)

    # Extra Skill

    Abillities[1] = gen.Skills(0, Abillities[1])

    # Psychic Skills

    if Psy >= 1:
        Abillities[2] = gen.Skills(2, Abillities[2])
        if Psy == 2:
            Abillities[2] = gen.Skills(2, Abillities[2])

    # Other Attributes

    #   Effort
    if WISmod >= CONmod:
        Effort = 1 + gen.Array_Maximum(Abillities[2], len(Abillities[2])) + WISmod

    elif CONmod >= WISmod:
        Effort = 1 + gen.Array_Maximum(Abillities[2], len(Abillities[2])) + CONmod

    #   HP and SS
    hp = random.randint(1, 6) + CONmod

    if War >= 1:
        hp += 2

    if hp < 1:
        hp = 1

    #   AB

    if War >= 1:
        ab = 1
    else:
        ab = 0

    ss = Abillities[0][5]

    # Equipment
    Equipment = None
    Credits = None

    Equipment, Credits = gen.Equipment(Equipment, Credits)

    #   AC
    if Abillities[3][12] >= 1:
        ac = 15
    else:
        ac = 10 + DEXmod

    #   Saving Throws

    # Physical
    if STRmod >= CONmod:
        saveP = 15 - STRmod
    else:
        saveP = 15 - CONmod

    # Evasion
    if INTmod >= DEXmod:
        saveE = 15 - INTmod
    else:
        saveE = 15 - DEXmod

    # Mental
    if WISmod >= CHAmod:
        saveM = 15 - WISmod
    else:
        saveM = 15 - CHAmod

    # Name Stage
   
    FullName = name_gen.names()

    # Print Stage
    print(FullName)
    print(Backprint + " and " + str(BackprintNUM))
    print("STR: " + str(STR) + strMOD)
    print("DEX: " + str(DEX) + dexMOD)
    print("CON: " + str(CON) + conMOD)
    print("INT: " + str(INT) + intMOD)
    print("WIS: " + str(WIS) + wisMOD)
    print("CHA: " + str(CHA) + chaMOD)

    print("Skills:  ")
    print(Abillities)
    # SAVE: array[4] P[0],E[0], and M[0]. array [5] AC[0], and AB[1] 
    # array [6], Effort[0], FullName[1], Backprint[2], and BackprintNUM[3],
    # array [7][War[0], Exp[1], and Psy[2],
    # Credits[8],Equipment[9],
    # Array[10] hp[0], ss[1]
    return [Abillities[0], Abillities[1], Abillities[2], Abillities[3], 
    [saveP, saveE, saveM], [ac, ab], [Effort, FullName, Backprint, BackprintNUM], 
    [War,Exp,Psy],Credits, Equipment,[hp,ss]]


if __name__ == '__main__':
    Main.main()

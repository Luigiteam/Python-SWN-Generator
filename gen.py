# Credit Goes to Luigiteam on GitHub
# https://github.com/Luigiteam/Python-SWN-Generator

import random
import Main


def attribute_gen():
    """Simulates generating attributes with 3 seperate die"""
    i = 3
    att = 0
    while i > 0:
        att += random.randint(1, 6)
        i -= 1
    return att


def attribute_mod(type, att):
    """att is the Attribute you want to use"""
    """If Given 0 for the type, it'll return an int of the mod"""
    """If Given 1 for the type, it'll return a string of the mod"""
    if type == 0:

        if att == 3:
            return -2

        if att >= 4 and att <= 7:
            return -1

        if att >= 8 and att <= 13:
            return 0

        if att >= 14 and att <= 17:
            return 1

        if att == 18:
            return 2

    if type == 1:
        if att == 3:
            return " - 2"

        if att >= 4 and att <= 7:
            return " - 1"

        if att >= 8 and att <= 13:
            return " ± 0"

        if att >= 14 and att <= 17:
            return " + 1"

        if att == 18:
            return " + 2"


def background_pick(rand):
    """Returns the string form of a charactor's background"""
    """Does not have Clergy, Courtesan, Dilettante and Politican backgrounds"""
    if rand == 1:
        return "Barbarian"

    elif rand == 2:
        return "Criminal"

    elif rand == 3:
        return "Entertainer"

    elif rand == 4:
        return "Merchant"

    elif rand == 5:
        return "Noble"

    elif rand == 6:
        return "Official"

    elif rand == 7:
        return "Peasant"

    elif rand == 8:
        return "Physician"

    elif rand == 9:
        return "Pilot"

    elif rand == 10:
        return "Scholar"

    elif rand == 11:
        return "Soldier"

    elif rand == 12:
        return "Spacer"

    elif rand == 13:
        return "Technician"

    elif rand == 14:
        return "Thug"

    elif rand == 15:
        return "Vagabond"

    else:
        return "Worker"


def background_table(backnum, growth, learning, abilities):
    """This changes numbers in the array given 
       depending on what background is given"""
    """# Does not have Clergy, Courtesan, Dilettante and Politican backgrounds"""

    # Barbarian
    if backnum == 1:

        abilities[1][15] += 1

        while growth > 0:
            rand = random.randint(1, 6)
            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2 or rand == 3:
                abilities[0] = Att(1, abilities[0])
                growth -= 1

            if rand == 4:
                abilities[0] = Att(2, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][2] < 1:
                abilities[1][2] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

        while learning > 0:
            rand = random.randint(1, 8)
            if rand == 1:
                abilities[1] = Skills(1, abilities[1])
                learning -= 1

            if rand == 2 and abilities[1][1] < 1:
                abilities[1][1] += 1
                learning -= 1

            if rand == 3 and abilities[1][2] < 1:
                abilities[1][2] += 1
                learning -= 1

            if rand == 4 and abilities[1][6] < 1:
                abilities[1][6] += 1
                learning -= 1

            if rand == 5 and abilities[1][7] < 1:
                abilities[1][7] += 1
                learning -= 1

            if rand == 6 and abilities[1][11] < 1:
                abilities[1][11] += 1
                learning -= 1

            if rand == 7 and abilities[1][13] < 1:
                abilities[1][13] += 1
                learning -= 1

            if rand == 8 and abilities[1][15] < 1:
                abilities[1][15]
                learning -= 1

    # Criminal
    if backnum == 2:

        abilities[1][13] += 1
        while growth > 0:
            rand = random.randint(1, 6)
            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2 or rand == 4:
                abilities[0] = Att(2, abilities[0])
                growth -= 1

            if rand == 3:
                abilities[0] = Att(1, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][1] < 1:
                abilities[1][1] += 1
                growth -= 1

            if rand == 6:
                Skills(0, abilities[1])
                growth -= 1

        while learning > 0:
            rand = random.randint(1, 8)
            if rand == 1 and abilities[1][0]:
                abilities[1][0] += 1
                learning -= 1

            if rand == 2:
                abilities[1] = Skills(1, abilities[1])
                learning -= 1

            if rand == 3 and abilities[1][1] < 1:
                abilities[1][1] += 1
                learning -= 1

            if rand == 4 and abilities[1][7] < 1:
                abilities[1][7] += 1
                learning -= 1

            if rand == 5 and abilities[1][10] < 1:
                abilities[1][10] += 1
                learning -= 1

            if rand == 6 and abilities[1][13] < 1:
                abilities[1][13] += 1
                learning -= 1

            if rand == 7 and abilities[1][16] < 1:
                abilities[1][16] += 1
                learning -= 1

            if rand == 8 and abilities[1][17] < 1:
                abilities[1][17] += 1
                learning -= 1

    # Entertainer
    if backnum == 3:
        abilities[1][8] += 1
        while growth > 0:
            rand = random.randint(1, 6)
            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2 or rand == 3:
                abilities[0] = Att(2, abilities[0])
                growth -= 1

            if rand == 4:
                abilities[0] = Att(1, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][1]:
                abilities[1][1] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

    # Merchant/Nobal/Official 
    if backnum == 4 or backnum == 5 or backnum == 6:
        if backnum == 4:
            abilities[1][17] += 1

        if backnum == 5:
            abilities[1][6] += 1

        if backnum == 6:
            abilities[1][0] += 1

        while growth > 0:
            rand = random.randint(1, 6)

            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand >= 2 and rand <= 4:
                abilities[0] = Att(2, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][1] < 1:
                abilities[1][1] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

        if backnum == 4:
            while learning > 0:
                rand = random.randint(1, 8)
                if rand == 1 and abilities[1][0] < 1:
                    abilities[1][0] += 1
                    learning -= 1

                if rand == 2:
                    abilities[1] = Skills(1, abilities[1])
                    learning -= 1

                if rand == 3 and abilities[1][1] < 1:
                    abilities[1][1] += 1
                    learning -= 1

                if rand == 4 and abilities[1][3] < 1:
                    abilities[1][3]
                    learning -= 1

                if rand == 5 and abilities[1][5] < 1:
                    abilities[1][5] += 1
                    learning -= 1

                if rand == 6 and abilities[1][7] < 1:
                    abilities[1][7] += 1
                    learning -= 1

                if rand == 7 and abilities[1][17] < 1:
                    abilities[1][17] += 1
                    learning -= 1

                if rand == 8 and abilities[1][16] < 1:
                    abilities[1][16] += 1
                    learning -= 1

        if backnum == 5:
            while learning > 0:
                rand = random.randint(1, 8)

                if rand == 1 and abilities[1][0] < 1:
                    abilities[1][0] += 1
                    learning -= 1

                if rand == 2:
                    abilities[1] = Skills(1, abilities[1])
                    learning -= 1

                if rand == 3 and abilities[1][1] < 1:
                    abilities[1][1] += 1
                    learning -= 1

                if rand == 4 and abilities[1][5] < 1:
                    abilities[1][5] += 1
                    learning -= 1

                if rand == 5 and abilities[1][6] < 1:
                    abilities[1][5] += 1
                    learning -= 1

                if rand == 6 and abilities[1][7] < 1:
                    abilities[1][7] += 1
                    learning -= 1

                if rand == 7 and abilities[1][9] < 1:
                    abilities[1][9] += 1
                    learning -= 1

                if rand == 8 and abilities[1][16] < 1:
                    abilities[1][16] += 1
                    learning -= 1

        if backnum == 6:
            while learning > 0:

                rand = random.randint(1, 8)

                if rand == 1 and abilities[1][0] < 1:
                    abilities[1][0] += 1
                    learning -= 1

                if rand == 2:
                    abilities[1] = Skills(0, abilities[1])
                    learning -= 1

                if rand == 3 and abilities[1][1] < 1:
                    abilities[1][1] += 1
                    learning -= 1

                if rand == 4 and abilities[1][5] < 1:
                    abilities[1][5] += 1
                    learning -= 1

                if rand == 5 and abilities[1][6] < 1:
                    abilities[1][6] += 1
                    learning -= 1

                if rand == 6 and abilities[1][7] < 1:
                    abilities[1][7] += 1
                    learning -= 1

                if rand == 7 and abilities[1][16] < 1:
                    abilities[1][16] += 1
                    learning -= 1

                if rand == 8 and abilities[1][17] < 1:
                    abilities[1][17] += 1
                    learning -= 1

    # Peasent        
    if backnum == 7:

        abilities[1][2] += 1

        while growth > 0:

            rand = random.randint(1, 6)
            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2 or rand == 3 or rand == 4:
                abilities[0] = Att(1, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][2] < 1:
                abilities[1][2] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

        while learning > 0:

            rand = random.randint(1, 8)
            if rand == 1 and abilities[1][1] < 1:
                abilities[1][1] += 1
                learning -= 1

            if rand == 2 and abilities[1][2] < 1:
                abilities[1][2] += 1
                learning -= 1

            if rand == 3 and abilities[1][3] < 1:
                abilities[1][3] += 1
                learning -= 1

            if rand == 4 and abilities[1][7] < 1:
                abilities[1][7] += 1
                learning -= 1

            if rand == 5 and abilities[1][13] < 1:
                abilities[1][13] += 1
                learning -= 1

            if rand == 6 and abilities[1][15] < 1:
                abilities[1][15] += 1
                learning -= 1

            if rand == 7 and abilities[1][17] < 1:
                abilities[1][17] += 1
                learning -= 1

            if rand == 8 and abilities[1][18] < 1:
                abilities[1][18] += 1
                learning -= 1

    # Physician
    if backnum == 8:
        abilities[1][4] += 1

        while growth > 0:

            rand = random.randint(1, 6)
            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2:
                abilities[0] = Att(1, abilities[0])
                growth -= 1

            if rand == 3 or rand == 4:
                abilities[0] = Att(2, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][1] < 1:
                abilities[1][1] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

        while learning > 0:

            rand = random.randint(1, 8)
            if rand == 1 and abilities[1][0] < 1:
                abilities[1][0] += 1
                learning -= 1

            if rand == 2 and abilities[1][1] < 1:
                abilities[1][1] += 1
                learning -= 1

            if rand == 3 and abilities[1][3] < 1:
                abilities[1][3] += 1
                learning -= 1

            if rand == 4 and abilities[1][4] < 1:
                abilities[1][4] += 1
                learning -= 1

            if rand == 5 and abilities[1][5] < 1:
                abilities[1][5] += 1
                learning -= 1

            if rand == 6 and abilities[1][7] < 1:
                abilities[1][7] += 1
                learning -= 1

            if rand == 7 and abilities[1][16] < 1:
                abilities[1][16] += 1
                learning -= 1

            if rand == 8 and abilities[1][17] < 1:
                abilities[1][17] += 1
                learning -= 1

    # Pilot
    if backnum == 9:
        abilities[1][9] += 1

        while growth > 0:

            rand = random.randint(1, 6)

            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2 or rand == 3:
                abilities[0] = Att(1, abilities[0])
                growth -= 1

            if rand == 4:
                abilities[0] = Att(2, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][1] < 1:
                abilities[1][1] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

        while learning > 0:

            rand = random.randint(1, 8)

            if rand == 1 and abilities[1][1] < 1:
                abilities[1][1] += 1
                learning -= 1

            if rand == 2 and abilities[1][2] < 1:
                abilities[1][2] += 1
                learning -= 1

            if rand == 3 and abilities[1][3] < 1:
                abilities[1][3] += 1
                learning -= 1

            if rand == 4 and abilities[1][7] < 1:
                abilities[1][7] += 1
                learning -= 1

            if rand == 5 or rand == 6 and abilities[1][9] < 1:
                abilities[1][9] += 1
                learning -= 1

            if rand == 7 and abilities[1][12] < 1:
                abilities[1][12] += 1
                learning -= 1

            if rand == 8 and abilities[1][17] < 1:
                abilities[1][17] += 1
                learning -= 1

    # Scholar        
    if backnum == 10:

        abilities[1][5] += 1

        while growth > 0:

            rand = random.randint(1, 6)

            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2 or rand == 3 or rand == 4:
                abilities[0] = Att(2, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][1] < 1:
                abilities[1][1] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

        while learning > 0:

            rand = random.randint(1, 8)

            if rand == 1 and abilities[1][0] < 1:
                abilities[1][0] += 1
                learning -= 1

            if rand == 2 and abilities[1][1] < 1:
                abilities[1][1] += 1
                learning -= 1

            if rand == 3 and abilities[1][3] < 1:
                abilities[1][3] += 1
                learning -= 1

            if rand == 4 and abilities[1][5] < 1:
                abilities[1][5] += 1
                learning -= 1

            if rand == 5 and abilities[1][7] < 1:
                abilities[1][7] += 1
                learning -= 1

            if rand == 6 and abilities[1][8] < 1:
                abilities[1][8] += 1
                learning -= 1

            if rand == 7 and abilities[1][10] < 1:
                abilities[1][10] += 1
                learning -= 1

            if rand == 8 and abilities[1][16] < 1:
                abilities[1][16] += 1
                learning -= 1

    # Soldier
    if backnum == 11:
        abilities[1] = Skills(1, abilities[1])

        while growth > 0:

            rand = random.randint(1, 6)

            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2 or rand == 3 or rand == 4:
                abilities[0] = Att(1, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][2] < 1:
                abilities[1][2] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

        while learning > 0:

            rand = random.randint(1, 8)

            if rand == 1 and abilities[1][0] < 1:
                abilities[1][0] += 1
                learning -= 1

            if rand == 2:
                abilities[1] = Skills(1, abilities[1])
                learning -= 1

            if rand == 3 and abilities[1][2] < 1:
                abilities[1][2] += 1
                learning -= 1

            if rand == 4 and abilities[1][3] < 1:
                abilities[1][3] += 1
                learning -= 1

            if rand == 5 and abilities[1][6] < 1:
                abilities[1][6] += 1
                learning -= 1

            if rand == 6 and abilities[1][7] < 1:
                abilities[1][7] += 1
                learning -= 1

            if rand == 7 and abilities[1][13] < 1:
                abilities[1][13] += 1
                learning -= 1

            if rand == 8 and abilities[1][15] < 1:
                abilities[1][15] += 1
                learning -= 1

    # Spacer
    if backnum == 12:
        abilities[1][3] += 1

        while growth > 0:

            rand = random.randint(1, 6)

            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2 or rand == 3:
                abilities[0] = Att(1, abilities[0])
                growth -= 1

            if rand == 4:
                abilities[0] = Att(2, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][2] < 1:
                abilities[1][2] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

        while learning > 0:

            rand = random.randint(1, 8)

            if rand == 1 and abilities[1][0] < 1:
                abilities[1][0] += 1
                learning -= 1

            if rand == 2 and abilities[1][1] < 1:
                abilities[1][1] += 1
                learning -= 1

            if rand == 3 and abilities[1][2] < 1:
                abilities[1][2] += 1
                learning -= 1

            if rand == 4 and abilities[1][3] < 1:
                abilities[1][3] += 1
                learning -= 1

            if rand == 5 and abilities[1][5] < 1:
                abilities[1][5] += 1
                learning -= 1

            if rand == 6 and abilities[1][9] < 1:
                abilities[1][9] += 1
                learning -= 1

            if rand == 7 and abilities[1][10] < 1:
                abilities[1][10] += 1
                learning -= 1

            if rand == 8 and abilities[1][16] < 1:
                abilities[1][16] += 1
                learning -= 1

                # Technician

    # Technician
    if backnum == 13:
        abilities[1][3] += 1

        while growth > 0:

            rand = random.randint(1, 6)

            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2:
                abilities[0] = Att(1, abilities[0])
                growth -= 1

            if rand == 3 or rand == 4:
                abilities[0] = Att(2, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][1] < 1:
                abilities[1][1] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

        while learning > 0:

            rand = random.randint(1, 8)

            if rand == 1 and abilities[1][0] < 1:
                abilities[1][0] += 1
                learning -= 1

            if rand == 2 and abilities[1][1] < 1:
                abilities[1][1] += 1
                learning -= 1

            if rand == 3 and abilities[1][2] < 1:
                abilities[1][2] += 1
                learning -= 1

            if rand == 4 or rand == 5 and abilities[1][3] < 1:
                abilities[1][3] += 1
                learning -= 1

            if rand == 6 and abilities[1][5] < 1:
                abilities[1][5] += 1
                learning -= 1

            if rand == 7 and abilities[1][7] < 1:
                abilities[1][7] += 1
                learning -= 1

            if rand == 8 and abilities[1][9] < 1:
                abilities[1][9] += 1
                learning -= 1

    # Thug
    if backnum == 14:

        abilities[1] = Skills(1, abilities[1])

        while growth > 0:

            rand = random.randint(1, 6)

            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2:
                abilities[0] = Att(2, abilities[0])
                growth -= 1

            if rand == 3 or rand == 4:
                abilities[0] = Att(1, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][1] < 1:
                abilities[1][1] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

        while learning > 0:

            rand = random.randint(1, 8)

            if rand == 1:
                abilities[1] = Skills(1, abilities[1])
                learning -= 1

            if rand == 2 and abilities[1][1] < 1:
                abilities[1][1] += 1
                learning -= 1

            if rand == 3 and abilities[1][2] < 1:
                abilities[1][2] += 1
                learning -= 1

            if rand == 4 and abilities[1][7] < 1:
                abilities[1][7] += 1
                learning -= 1

            if rand == 5 and abilities[1][13] < 1:
                abilities[1][13] += 1
                learning -= 1

            if rand == 6:

                rand2 = random.randint(1, 2)

                if rand2 == 1:
                    abilities[1][14] += 1

                elif rand2 == 2:
                    abilities[1][12] += 1

                learning -= 1

            if rand == 7 and abilities[1][15] < 1:
                abilities[1][15] += 1
                learning -= 1

            if rand == 8 and abilities[1][16] < 1:
                abilities[1][16] += 1
                learning -= 1

    # Vagabond
    if backnum == 15:

        abilities[1][15] += 1

        while growth > 0:

            rand = random.randint(1, 6)

            if rand == 1:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 2 or rand == 3:
                abilities[0] = Att(1, abilities[0])
                growth -= 1

            if rand == 4:
                abilities[0] = Att(2, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][2] < 1:
                abilities[1][2] += 1
                growth -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                growth -= 1

        while learning > 0:

            rand = random.randint(1, 8)

            if rand == 1:
                abilities[1] = Skills(1, abilities[1])
                learning -= 1

            if rand == 2 and abilities[1][1] < 1:
                abilities[1][1] += 1
                learning -= 1

            if rand == 3 and abilities[1][7] < 1:
                abilities[1][7] += 1
                learning -= 1

            if rand == 4 and abilities[1][8] < 1:
                abilities[1][8] += 1
                learning -= 1

            if rand == 5 and abilities[1][9] < 1:
                abilities[1][9] += 1
                learning -= 1

            if rand == 6 and abilities[1][13] < 1:
                abilities[1][13] += 1
                learning -= 1

            if rand == 7 and abilities[1][15] < 1:
                abilities[1][15] += 1
                learning -= 1

            if rand == 8 and abilities[1][18] < 1:
                abilities[1][18] += 1
                learning -= 1

    # Worker
    if backnum == 16:

        abilities[1][18] += 1

        while growth > 0:

            rand = random.randint(1, 6)

            if rand >= 1 and rand <= 4:
                abilities[0] = Att(0, abilities[0])
                growth -= 1

            if rand == 5 and abilities[1][2] < 1:
                abilities[1][2] += 1
                learning -= 1

            if rand == 6:
                abilities[1] = Skills(0, abilities[1])
                learning -= 1

        while learning > 0:

            rand = random.randint(1, 8)

            if rand == 1 and abilities[1][0] < 1:
                abilities[1][0] += 1
                learning -= 1

            if rand == 2:
                abilities[1] = Skills(0, abilities[1])
                learning -= 1

            if rand == 3 and abilities[1][1] < 1:
                abilities[1][1] += 1
                learning -= 1

            if rand == 4 and abilities[1][2] < 1:
                abilities[1][2] += 1
                learning -= 1

            if rand == 5 and abilities[1][3] < 1:
                abilities[1][3] += 1
                learning -= 1

            if rand == 6 and abilities[1][9] < 1:
                abilities[1][9] += 1
                learning -= 1

            if rand == 7 and abilities[1][10] < 1:
                abilities[1][10] += 1
                learning -= 1

            if rand == 8 and abilities[1][18] < 1:
                abilities[1][18] += 1
                learning -= 1

    return abilities


def Att(type, abilities):
    """type - 0: This adds any attribute by 1
       type - 1: This adds pysical attributes by 2
       type - 2 or heigher: This adds metal attributes by 2"""

    # Any Attribute
    if type == 0:
        randoNum = [0, 0, 0, 0, 0, 0]
        run = True
        a = 10
        while a > 0:
            while run:
                rand = random.randint(0, 5)

                if randoNum[rand] == 0:
                    run = False

            for i in range(0, 6):
                if i == rand and abilities[i] < 18:
                    abilities[i] += 1
                    a = 0
                    break

                elif i == rand and abilities[i] >= 18:
                    randoNum[i] = -1
                    run = True
                    break

            a -= 1

    # Physical Attributes
    elif type == 1:
        randomNum = [0, 0, 0]
        run = True
        a = 10
        while a > 0:
            while run:
                rand = random.randint(0, 2)

                if randomNum[rand] == 0:
                    run = False

            for i in range(0, 3):
                if i == rand and abilities[i] < 17:
                    abilities[i] += 2
                    a = 0
                    break

                elif i == rand and abilities[i] >= 17:
                    randomNum[i] = -1
                    run = False
                    break

            a -= 1

    # Mental Attributes
    else:
        randomNum = [0, 0, 0, 0, 0, 0]
        run = True
        a = 10
        while a > 0:
            while run:
                rand = random.randint(3, 5)

                if randomNum[rand] == 0:
                    run = False

            for i in range(3, 6):
                if i == rand and abilities[i] < 17:
                    abilities[i] += 2
                    a = 0
                    break
                elif i == rand and abilities[i] < 17:
                    randomNum[i] = -1
                    run = True
                    break

            a -= 1

    return abilities


def Skills(type, Skills):
    # Any Skills
    if type == 0:
        randoNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a = 20
        run = True
        while a > 0:
            while run:
                rand = random.randint(1, 18)

                if randoNum[rand - 1] == 0:
                    run = False

            for i in range(0, 19):
                if i == rand and Skills[i] < 1:
                    Skills[i] += 1
                    a = 0
                    break
                elif i == rand and Skills[i] >= 1:
                    randoNum[i] = -1
                    run = True

            a -= 1

    # Combat Skills
    if type == 1:
        a = 6
        randoNum = [0, 0, 0, 0]
        run = True
        while a > 0:
            while run:
                rand = random.randint(0, 2)

                if randoNum[rand] == 0:
                    run = False

            if rand == 0 and Skills[11] < 1:
                Skills[11] += 1
                a = 0

            elif rand == 1 and Skills[12] < 1:
                Skills[12] += 1
                a = 0

            elif rand == 2 and Skills[14] < 1:
                Skills[14] += 1
                a = 0

            elif rand == 0 and Skills[11] >= 1:
                randoNum[0] = -1
                run = True

            elif rand == 1 and Skills[12] >= 1:
                randoNum[1] = -1
                run = True

            elif rand == 2 and Skills[14] >= 1:
                randoNum[2] = -1
                run = True

            a -= 1

    # Psychic Skills
    if type == 2:
        randoNum = [0, 0, 0, 0, 0, 0]
        run = True
        a = 7

        while a > 0:
            while run:
                rand = random.randint(0, 5)

                if randoNum[rand] == 0:
                    run = False

            for x in range(0, 6):
                if x == rand and Skills[x] < 1 and randoNum[x] == 0:
                    Skills[rand] += 1
                    a = 0
                    break

                elif x == rand and Skills[rand] >= 1:
                    randoNum[rand] = -1
                    run = True

            a -= 1

    # Non-Combat Skills
    if type == 3:
        randoNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, -1, 0, 0, 0, 0, 0]
        a = 20
        run = True
        while a > 0:
            while run:
                rand = random.randint(1, 18)

                if randoNum[rand - 1] == 0:
                    run = False

            for i in range(0, 19):
                if i == rand and Skills[i] < 1:
                    Skills[i] += 1
                    a = 0
                    break
                elif i == rand and Skills[i] >= 1:
                    randoNum[i] = -1
                    run = True

            a -= 1

    return Skills


def Foci(type, Psy, foci, skillCheck):
    # Any Foci
    if type == 0:
        randoNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        print(len(foci[3]))
        run = True
        a = 23
        while a > 0:
            while run:
                rand = random.randint(0, 23)
                rand = 13
                if randoNum[rand] == 0:
                    run = False

            for x in range(0, 24):
                if x == rand and x == 13 and foci[3][13] < 2 and Psy >= 1:
                    foci[3][13] += 1
                    a = 0
                elif x == rand and foci[3][x] < 2:
                    foci[3][x] += 1
                    a = 0
                elif x == rand and foci[3][x] == 2:
                    randoNum[x] = -1
                    run = True

            a -= 1

    # Combat only
    if type == 1:
        run = True
        randoNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a = 15
        while a > 0:
            while run:
                rand = random.randint(1, 11)

                if randoNum[rand - 1] == 0:
                    run = False

            for x in range(1, 12):

                if rand == 1 and foci[3][0] < 2:
                    foci[3][0] += 1
                    a = 0
                    break

                elif rand == 2 and foci[3][1] < 2:
                    foci[3][1] += 1
                    a = 0
                    break

                elif rand == 3 and foci[3][2] < 2:
                    foci[3][2] += 1
                    a = 0
                    break

                elif rand == 4 and foci[3][4] < 2:
                    foci[3][4] += 1
                    a = 0
                    break

                elif rand == 5 and foci[3][8] < 2:
                    foci[3][8] += 1
                    a = 0
                    break

                elif rand == 6 and foci[3][12] == 1:
                    foci[3][12] += 1
                    a = 0
                    break

                elif rand == 7 and foci[3][14] < 2:
                    foci[3][14] += 1
                    a = 0
                    break

                elif rand == 8 and foci[3][15] < 2:
                    foci[3][15] += 1
                    a = 0
                    break

                elif rand == 9 and foci[3][16] < 2:
                    foci[3][16] += 1
                    a = 0
                    break

                elif rand == 10 and foci[3][18] < 2:
                    foci[3][18] += 1
                    a = 0
                    break

                elif rand == 11 and foci[3][20] < 2:
                    foci[3][20] += 1
                    a = 0
                    break

                else:
                    randoNum[rand - 1] = -1
                    run = True

            a -= 1

    # Non-Psychic and Non-Combat
    if type == 2:
        randoNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        run = True
        a = 11
        while a > 0:
            while run:
                rand = random.randint(1, 10)

                if randoNum[rand - 1] == 0:
                    run = False

            if rand == 1 and foci[3][3] < 2:
                foci[3][3] += 1
                a = 0
                break

            elif rand == 2 and foci[3][5] < 2:
                foci[3][5] += 1
                a = 0
                break

            elif rand == 3 and foci[3][6] < 2:
                foci[3][6] += 1
                a = 0
                break

            elif rand == 4 and foci[3][7] < 2:
                foci[3][7] += 1
                a = 0
                break

            elif rand == 5 and foci[3][9] < 2:
                foci[3][9] += 1
                a = 0
                break

            elif rand == 6 and foci[3][10] < 2:
                foci[3][10] += 1
                a = 0
                break

            elif rand == 7 and foci[3][11] < 2:
                foci[3][11] += 1
                a = 0
                break

            elif rand == 8 and foci[3][17] < 2:
                foci[3][17] += 1
                a = 0
                break

            elif rand == 9 and foci[3][18] < 2:
                foci[3][18] += 1
                a = 0
                break

            elif rand == 10 and foci[3][19] < 2:
                foci[3][19] += 1
                a = 0
                break

            elif rand == 11 and foci[3][20] < 2:
                foci[3][20] += 1
                a = 0
                break

            else:
                randoNum[rand - 1] = -1
                run = True

            a -= 1

    # Skills Check

    if foci[3][0] == 1 and skillCheck[0] == 0 and foci[1][7] < 1:
        foci[1][7] += 1
        skillCheck[0] = -1

    if foci[3][1] == 1 and skillCheck[1] == 0 and foci[1][14] < 1:
        foci[1][14] += 1
        skillCheck[1] = -1

    if foci[3][2] == 1 and skillCheck[2] == 0 and foci[1][13] < 1:
        foci[1][13] += 1
        skillCheck[2] = -1

    if foci[3][3] == 1 and skillCheck[4] == 0 and foci[1][6] < 1:
        foci[1][6] += 1
        skillCheck[4] = -1

    if foci[3][4] and skillCheck[3] == 0:
        skillCheck[3] = -1
        a = 6
        randoNum = [0, 0, 0]
        run = True
        while a > 0:
            if randoNum == [0, 0, 0]:
                break

            while run:
                rand = random.randint(1, 3)

                if randoNum[rand - 1] == 0:
                    run = False

            if rand == 1 and foci[1][11] < 1:
                foci[1][11] += 1
                a = 0

            elif rand == 2 and foci[1][12] < 1:
                foci[1][12] += 1
                a = 0

            elif rand == 3 and foci[14] < 1:
                foci[1][14] += 1
                a = 0

            elif rand == 1 and foci[11] >= 1:
                randoNum[0] = -1
                run = True

            elif rand == 2 and foci[12] >= 1:
                randoNum[1] = -1
                run = True

            elif rand == 3 and foci[14] >= 1:
                randoNum[2] = -1
                run = True

            elif x == rand and foci[x] >= 2:
                randoNum[x] = -1
                run = True
                a = 0
                break

            a -= 1

    if foci[3][5] and skillCheck[4] == 0 and foci[1][1] < 1:
        foci[1][1] += 1
        skillCheck[5] -= 1

    # x = 6 is Die Hard which has no added skill
    skillCheck[6] = -1

    if foci[3][7] == 1 and skillCheck[7] == 0 and foci[1][16] < 1:
        foci[1][16] += 1
        skillCheck[7] = -1

    if foci[3][8] == 1 and skillCheck[8] == 0 and foci[1][12] < 1:
        foci[1][12] += 1
        skillCheck[8] = -1

    if foci[3][9] == 1 and skillCheck[9] == 0 and foci[1][10] < 1:
        foci[1][10] += 1
        skillCheck[9] = -1

    if foci[3][10] == 1 and skillCheck[10] == 0 and foci[1][4] < 1:
        foci[1][4] += 1
        skillCheck[10] = -1

    if foci[3][11] == 1 and skillCheck[11] == 0 and foci[1][6] < 1:
        foci[1][6] += 1
        skillCheck[11] = -1

    # Iron Hide [12], skillcheck[12] Does not have a free skill

    if foci[3][13] == 1 and skillCheck[13] == 0 and Psy >= 1:
        foci[3] = Skills(2, foci[3])
        skillCheck[13] = -1

    if foci[3][14] == 1 and skillCheck[14] == 0 and foci[1][14] < 1:
        foci[1][14] += 1
        skillCheck[14] = -1

    if foci[3][15] == 1 and skillCheck[15] == 0 and foci[1][11] < 1 or foci[1][14] < 1:
        a = 3
        randoNum = [0, 0]
        run = True
        while a > 0:
            while run:
                rand = random.randint(0, 1)

                if randoNum[rand] == 0:
                    run = False

            if rand == 0 and foci[1][11] < 1:
                foci[1][11] += 1
                break

            elif rand == 1 and foci[1][14] < 1:
                foci[1][14] += 1
                break

            elif rand == 0 and foci[1][11] >= 1:
                randoNum[0] = -1
                run = True

            elif rand == 1 and foci[1][14] >= 1:
                randoNum[1] = -1
                run = True
            
            if randoNum == [-1,-1]:
                break

    if foci[3][16] == 1 and skillCheck[16] == 0 and foci[1][12] < 1:
        foci[1][12] += 1
        skillCheck[16] = -1

    if foci[3][17] == 1 and skillCheck[17] == 0:
        foci[1] = Skills(3, foci[1])
        skillCheck[16] = -1

    if foci[3][18] == 1 and skillCheck[18] == 0 and foci[1][6] < 1:
        foci[1][6] += 1
        skillCheck[18] = -1

    if foci[3][19] == 1 and skillCheck[19] == 0 and foci[1][9] < 1:
        foci[1][9] += 1
        skillCheck[19] = -1

    if foci[3][20] == 1 and skillCheck[20] == 0 and foci[1][3] < 1:
        foci[1][3] += 1
        skillCheck[20] = -1

    if foci[3][21] == 1 and skillCheck[21] == 0 and foci[1][11] < 1:
        foci[1][11] += 1
        skillCheck[21] = -1

    if foci[3][22] == 1 and skillCheck[22] == 0 and Psy < 1:
        foci[3] = Skills(2, foci[3])
        skillCheck[22] = -1

    return foci, skillCheck


def Equipment(equip, credits):
    rand = random.randint(1, 10)

    if rand == 1:
        # Barbarian
        equip = ["Spear (1d6 + 1 damage)", "Primitive Hide Armor (AC 13)",
                 "Primitive Sheild (+1 AC)", "Knife (1d4 damage)", "Backpack", "7 Day Rations", "20m Rope"]
        credits = 500

    elif rand == 2:
        # Blade
        equip = ["Monoblade Sword (1d8 + 1 damage)", "Woven Body Armor (AC 15)",
                 "Secure Clothing (AC 13)", "Thermal Knife (1d6 damage)", "Backpack",
                 "Compad", "Lazarus Patch"]
        credits = 50

    elif rand == 3:
        # Theif
        equip = ["Laser Pistol (1d6 damage)", "Armored Undersuit (AC 13)", "Monoblade Knife (1d6 damage)",
                 "Climbing Harness", "Low-Light Goggles", "2 Type A Cells", "Backpack", "Compad", "Metatool"]
        credits = 25

    elif rand == 4:
        # Hacker
        equip = ["Laser Pistol (1d6 damage)", "Secure Clothing (AC 13)", "Postech Toolkit",
                 "3 Units of Spare Parts", "2 Type A Cells", "Dataslab", "Metatool", "2 Line Shunts"]
        credits = 100

    elif rand == 5:
        # Gunslinger
        equip = ["Laser Pistol (1d6 damage)", "Armor Undersuit (AC 13)", "Monoblade Knife (1d6 damage)",
                 "8 Type A Cells", "Backpack", "Compad"]
        credits = 100

    elif rand == 6:
        # Soldier
        equip = ["Combat Rifle (1d12 damage)", "Woven Body Armor (AC 15)", "Knife (1d4 damage)",
                 "80 Rounds of Ammo", "Backpack", "Compad"]
        credits = 100

    elif rand == 7:
        # Scout
        equip = ["Laser Rifle (1d10)", "Armored Vacc Suit (AC 13)", "Knife (1d4 damage)", "Survey Scanner",
                 "Survival Kit", "Binoculars", "8 Type A Cells", "Backpack", "Compad"]
        credits = 25

    elif rand == 8:
        # MEDIC
        equip = ["Laser Pistol (1d6 damage)", "Secure Clothing (AC 13)", "4 Lazarus Patches",
                 "2 Doses of Lift", "Backpack", "Medkit", "Compad", "Bioscanner"]
        credits = 25

    elif rand == 9:
        # Civilian
        equip = ["Secure Clothing (AC 13)", "Compad"]
        credits = 700

    elif rand == 10:
        # Technician
        equip = ["Laser Pistol (1d6 damage)", "Armored Undersuit (AC 13)", "Monoblade Knife (1d6 damage)",
                 "Postech Toolkit", "6 Units of Spare Parts", "4 Type A Cells", "Backpack", "Dataslab", "Metatool"]
        credits = 200

    return equip, credits


def Array_Maximum(Array, Length):
    """This returns the max number"""

    max = Array[0]

    for i in range(1, Length):
        if Array[i - 1] > max:
            max = Array[i]

    return max


if __name__ == '__main__':
    Main.main()

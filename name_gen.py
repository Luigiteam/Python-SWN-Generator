#Credit Goes to Luigiteam on GitHub
#https://github.com/Luigiteam/Python-SWN-Generator

from re import A
import Main
import random
import json


def names():
    data = json.load(open('JSON Files\\Names.json'))
    # 0 - Male, 1 - Female
    gender = random.randint(0, 1)

    tempF = 'null'
    tempL = 'null'
    for i in range(2):
        rand = random.randint(1, 5)
        if rand == 1:
            if i == 1:
                if gender == 0:
                    tempF = random.choice(data['AMF'])
                else:
                    tempF = random.choice(data['AFF'])
            else:
                tempL = random.choice(data["AL"])

        elif rand == 2:
            if i == 1:
                if gender == 0:
                    tempF = random.choice(data['CMF'])
                else:
                    tempF = random.choice(data['CFF'])
            else:
                tempL = random.choice(data['CL'])

        elif rand == 3:
            if i == 1:
                if gender == 0:
                    tempF = random.choice(data['EMF'])
                else:
                    tempF = random.choice(data['EFF'])
            else:
                tempL = random.choice(data['EL'])

        elif rand == 4:
            if i == 1:
                if gender == 0:
                    tempF = random.choice(data['GMF'])
                else:
                    tempF = random.choice(data['GFF'])
            else:
                tempL = random.choice(data['GL'])

        elif rand == 5:
            if i == 1:
                if gender == 0:
                    tempF = random.choice(data['IMF'])
                else:
                    tempF = random.choice(data['IFF'])
            else:
                tempL = random.choice(data['IL'])
        
        elif rand == 6:
            if i == 1:
                if gender == 0:
                    tempF = random.choice(data['JMF'])
                else:
                    tempF = random.choice(data['JFF'])
            else:
                tempL = random.choice(data['JL'])

    return tempF + tempL

if __name__ == '__main__':
    Main.main()

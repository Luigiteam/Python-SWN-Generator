#Credit Goes to Luigiteam on GitHub
#https://github.com/Luigiteam/Python-SWN-Generator

class main:
    
    import tkinter as tk
    import mainLine
    import gen

    run = True

    window = None

    Abillities = None

    def __init__(self,Abillities,level):

        # SAVE: array[4] P[0],E[1], and M[2]. array [5] AC[0], and AB[1] 
        # array [6], Effort[0], FullName[1], Backprint[2], and BackprintNUM[3],
        # array [7][War[0], Exp[1], and Psy[2],
        # Credits[8],Equipment[9],
        # Array[10] hp[0], ss[1]

        self.Abillities = Abillities

        while self.run:
            
            Abillities = self.Abillities

            self.window = self.tk.Tk()
                
            self.run = False
            
            self.window.title("SWN Character Generator 1.0")

            # Has Name, Level and class, background, hp and ss
            Other = self.tk.Frame(self.window,bd=9,highlightbackground="black",highlightthickness=2,height=175,width=150)
            Other = self.other_Print(Other,Abillities,level)
            Other.place(x = 5, y = 5)
            Other.propagate(0)

            self.window.update_idletasks()
            other_Width = Other.winfo_width()
            other_Height = Other.winfo_height()


            # Has Saving throws
            Saves = self.tk.Frame(self.window,bd=9,highlightbackground="black",highlightthickness=2,height=175,width=150)
            Saves = self.saves_Print(Saves,Abillities[4])
            Saves.place(x = other_Width + 10, y = 5)

            Skills = self.tk.Frame(self.window,bd=9,highlightbackground="blue",highlightthickness=2,height=175,width=150)
            self.tk.Label(Skills,text="Skills: ").grid(row=0,column=0)
            Skills = self.skills_Print(Skills,Abillities[1])
            Skills.place(x = 5, y = other_Height + 10)
            Skills.pack_propagate(0)
            
            self.window.update_idletasks()
            skill_Width = Skills.winfo_width()
            skill_Height = Skills.winfo_height()

            saves_Width = Saves.winfo_width()

            Foci = self.tk.Frame(self.window,bd=9,highlightbackground="blue",highlightthickness=2,height=175,width=150)
            self.tk.Label(Foci,text="Foci:").grid(row=0,column=0)
            Foci = self.foci_Print(Foci,Abillities[3])
            Foci.place(x=skill_Width + 10,y=other_Height + 10)

            Psy = self.tk.Frame(self.window,bd=9,highlightbackground="blue",highlightthickness=2,height=175,width=150)
            
            if Abillities[7][2] >= 1:
                self.tk.Label(Psy,text="Psionics: ").grid(row=0,column=0)
                Psy = self.psy_Print(Psy,Abillities[2]) 
                Psy.place(x = 5, y = skill_Height + other_Height + 15)

            Attributes = self.tk.Frame(self.window,bd=9,highlightbackground="black",highlightthickness=2,height=175,width=150)
            Attributes = self.attributes_Print(Attributes,Abillities[0])
            Attributes.place(x = other_Width + saves_Width + 15, y = 5)

            Equipment = self.tk.Frame(self.window,bd=9,highlightbackground="red",highlightthickness=2)
            Weapons = self.tk.Frame(self.window,bd=9,highlightbackground="red",highlightthickness=2,height=175,width=150)
            Armor = self.tk.Frame(self.window,bd=9,highlightbackground="red",highlightthickness=2,height=175,width=150)

            Equipment,Weapons,Armor = self.equipment_Print(Equipment,Weapons,Armor,Abillities[8],Abillities[9])
            self.window.update_idletasks()

            attributeSize = Attributes.winfo_x() + Attributes.winfo_width()

            Equipment.place(x = attributeSize + 20, y = 5)
            
            self.window.update_idletasks()
            equipHeight = Equipment.winfo_height()

            Weapons.place(x = attributeSize + 20, y = equipHeight + 10)
            self.window.update_idletasks()
            armor_Equip_Height = equipHeight + Weapons.winfo_height()

            Armor.place(x = attributeSize + 20, y = armor_Equip_Height + 15)

            self.window.update_idletasks()

            attributes_X_Width = Attributes.winfo_x() + Attributes.winfo_width()

            self.tk.Button(
                self.window,
                text="Press Me To Reshuffle\n The Character",
                command=self.reshuffle,
                width=20,
                height=5,
                font=("Arial",9),
                bg="#dbdbdb",
                activebackground="#dbdbdb",
                border=1
                ).place(x=attributes_X_Width - 150,y=80)

            self.window.geometry("975x600+0+5")
            self.window.resizable(0,0)

            self.window.mainloop()

    def reshuffle(self):
        self.run = True
        self.window.destroy()
        self.Abillities = self.mainLine.Gen()

    def recenter(self,stat,row):
        col = None
        if stat == 5:
            col = 1

        if stat == 10:
            col = 2
        
        if row == 6:
            row = 1
        
        return row,col

    def skills_Print(self,Frame,skills):
        Col = 0

        stat = 0

        Row = 1

        for i in range(1,19):

            if i == 1 and skills[0] >= 0:
                self.tk.Label(Frame,text=" Administer level " + str(skills[0]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 2 and skills[1] >= 0:
                self.tk.Label(Frame,text=" Connect level " + str(skills[1]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 3 and skills[2] >= 0:
                self.tk.Label(Frame,text=" Exert level " + str(skills[2]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 4 and skills[3] >= 0:
                self.tk.Label(Frame,text=" Fix level " + str(skills[3]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 5 and skills[4] >= 0:
                self.tk.Label(Frame,text=" Heal level " + str(skills[4]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 6 and skills[5] >= 0:
                self.tk.Label(Frame,text=" Know level " + str(skills[5]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 7 and skills[6] >= 0:
                self.tk.Label(Frame,text=" Lead level " + str(skills[6]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 8 and skills[7] >= 0:
                self.tk.Label(Frame,text=" Notice level " + str(skills[7]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 9 and skills[8] >= 0:
                self.tk.Label(Frame,text=" Perform level " + str(skills[8]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 10 and skills[9] >= 0:
                self.tk.Label(Frame,text=" Pilot level " + str(skills[9]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 11 and skills[10] >= 0:
                self.tk.Label(Frame,text=" Program level " + str(skills[10]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 12 and skills[11] >= 0:
                self.tk.Label(Frame,text=" Punch level " + str(skills[11]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 13 and skills[12] >= 0:
                self.tk.Label(Frame,text=" Shoot level " + str(skills[12]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 14 and skills[13] >= 0:
                self.tk.Label(Frame,text=" Sneak Level " + str(skills[13]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 15 and skills[14] >= 0:
                self.tk.Label(Frame,text=" Stab level " + str(skills[14]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 16 and skills[15] >= 0:
                self.tk.Label(Frame,text=" Survive level " + str(skills[15]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 17 and skills[16] >= 0:
                self.tk.Label(Frame,text=" Talk level " + str(skills[16]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 18 and skills[17] >= 0:
                self.tk.Label(Frame,text=" Trade level " + str(skills[17]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 19 and skills[18] >= 0:
                self.tk.Label(Frame,text=" Work level " + str(skills[18]) + " ").grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            Row,Col = self.recenter(stat,Row)


        return Frame

    def psy_Print(self,Frame,Psy):
        Row = 1
        Col = 0
        stat = 0
        for i in range(0,6):
            if i == 0 and Psy[0] >= 0:
                self.tk.Label(Frame,text="Biopsionics level " + str(Psy[0])).grid(row=Row,column=Col)
                Row += 1
                stat += 1

            if i == 1 and Psy[1] >= 0:
                self.tk.Label(Frame,text="Metapsionics level " + str(Psy[1])).grid(row=Row,column=Col)
                Row += 1
                stat += 1

            if i == 2 and Psy[2] >= 0:
                self.tk.Label(Frame,text="Precognition level " + str(Psy[2])).grid(row=Row,column=Col)
                Row += 1
                stat += 1
            
            if i == 3 and Psy[3] >= 0:
                self.tk.Label(Frame,text="Telekinesis level " + str(Psy[3])).grid(row=Row,column=Col)
                Row += 1
                stat += 1
            
            if i == 4 and Psy[4] >= 0:
                self.tk.Label(Frame,text="Telepathy level " + str(Psy[4])).grid(row=Row,column=Col)
                Row += 1
                stat += 1
            
            if i == 5 and Psy[5] >= 0:
                self.tk.Label(Frame,text="Teleportation level " + str(Psy[5])).grid(row=Row,column=Col)

            Row, Col = self.recenter(stat,Row)

        return Frame

    def foci_Print(self,Frame,foci):
        stat = 0

        Col = 0

        Row = 1

        for i in range(0,22):
            if i == 0 and foci[0] >= 1:
                self.tk.Label(Frame,text="Alert level " + str(foci[0])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 1 and foci[1] >= 1:
                self.tk.Label(Frame,text="Armsman level " + str(foci[1])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 2 and foci[2] >= 1:
                self.tk.Label(Frame,text="Assassin level " + str(foci[2]))
                stat += 1
                Row += 1
            
            if i == 3 and foci[3] >= 1:
                self.tk.Label(Frame,text="Authority level " + str(foci[3])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 4 and foci[4] >= 1:
                self.tk.Label(Frame,text="Close Combat level " + str(foci[4])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 5 and foci[5] >= 1:
                self.tk.Label(Frame,text="Connected level " + str(foci[5])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 6 and foci[6] >= 1:
                self.tk.Label(Frame,text="Die Hard level " + str(foci[6])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
                
            if i == 7 and foci[7] >= 1:
                self.tk.Label(Frame,text="Diplomat level " + str(foci[7])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 8 and foci[8] >= 1:
                self.tk.Label(Frame,text="Gunslinger level " + str(foci[8])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 9 and foci[9] >= 1:
                self.tk.Label(Frame,text="Hacker level " + str(foci[9])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 10 and foci[10] >= 1:
                self.tk.Label(Frame,text="Healer level " + str(foci[10])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 11 and foci[11] >= 1:
                self.tk.Label(Frame,text="Henchkeeper level " + str(foci[11])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 12 and foci[12] >= 1:
                self.tk.Label(Frame,text="Iron Hide level " + str(foci[12])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 13 and foci[13] >= 1:
                self.tk.Label(Frame,text="Psychic Training level " + str(foci[13])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 14 and foci[14] >= 1:
                self.tk.Label(Frame,text="Savage Fray level " + str(foci[14])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 15 and foci[15] >= 1:
                self.tk.Label(Frame,text="Shocking Assault level " + str(foci[15])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 16 and foci[16] >= 1:
                self.tk.Label(Frame,text="Sniper level " + str(foci[16])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 17 and foci[17] >= 1:
                self.tk.Label(Frame,text="Specialist level " + str(foci[17])).grid(row=Row,column=Col)
                stat += 1  
                Row += 1 
            
            if i == 18 and foci[18] >= 1:
                self.tk.Label(Frame,text="Star Captain level " + str(foci[18])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 19 and foci[19] >= 1:
                self.tk.Label(Frame,text="Starfarer level " + str(foci[19])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 20 and foci[20] >= 1:
                self.tk.Label(Frame,text="Tinker level " + str(foci[20])).grid(row=Row,column=Col)
                stat += 1
                Row += 1

            if i == 21 and foci[21] >= 1:
                self.tk.Label(Frame,text="Unarmed Combantaint level " + str(foci[20])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 22 and foci[22] >= 1:
                self.tk.Label(Frame,text="Wanderer level " + str(foci[22])).grid(row=Row,column=Col)
                stat += 1
                Row += 1
            
            if i == 23 and foci[23] >= 1:
                self.tk.Label(Frame,text="Wild Psychic Talent level " + str(foci[23])).grid(row=Row,column=Col)
                stat += 1
                Row += 1

            Row, Col = self.recenter(stat,Row)

        return Frame

    def other_Print(self,Frame,other,level):

        #Full Name
        self.tk.Label(Frame,text=other[6][1]).grid(row=0,column=0)

        #Level and Class
        if other[7][0] == 2:
            self.tk.Label(Frame,text="Level " + str(level) + " | Full Warrior").grid(row=1,column=0)
        
        elif other[7][1] == 2:
            self.tk.Label(Frame,text="Level " + str(level) + " | Full Expert").grid(row=1,column=0)
        
        elif other[7][2] == 2:
            self.tk.Label(Frame,text="Level " + str(level) + " | Full Psychic").grid(row=1,column=0)

        elif other[7][0] == 1 and other[7][1] == 1:
            self.tk.Label(Frame,text="Level " + str(level) + " | Half Warrior Half Expert").grid(row=1,column=0)
        
        elif other[7][0] == 1 and other[7][2] == 1:
            self.tk.Label(Frame,text="Level " + str(level) + " | Half Warrior Half Psychic").grid(row=1,column=0)
        
        elif other[7][1] == 1 and other[7][2] == 1:
            self.tk.Label(Frame,text="Level " + str(level) + " | Half Expert Half Psychic").grid(row=1,column=0)

        #Background
        self.tk.Label(Frame,text="Background: " + other[6][2]).grid(row=2,column=0)

        #HP and SS
        self.tk.Label(Frame,text="HP: " + str(other[10][0]) + "/" + str(other[10][0])
                + " | SS: 0/" + str(other[10][1])).grid(row=3,column=0)

        return Frame

    def saves_Print(self,Frame,saves):
        self.tk.Label(Frame, text="Saving Throws: ").grid(row=0,column=0)

        self.tk.Label(Frame,text="Physical: " + str(saves[0])).grid(row=1,column=0)
        self.tk.Label(Frame,text="Evasion: " + str(saves[1])).grid(row=2,column=0)
        self.tk.Label(Frame,text="Mental: " + str(saves[2])).grid(row=3,column=0)

        return Frame
        
    def attributes_Print(self,Frame,Stats):
        
        strMod = self.gen.attribute_mod(1,Stats[0])
        dexMod = self.gen.attribute_mod(1,Stats[1])
        conMod = self.gen.attribute_mod(1,Stats[2])
        intMod = self.gen.attribute_mod(1,Stats[3])
        wisMod = self.gen.attribute_mod(1,Stats[4])
        chaMod = self.gen.attribute_mod(1,Stats[5])
        
        self.tk.Label(Frame,text="Attributes").grid(row=0,column=0)

        self.tk.Label(Frame,text="STR: " + str(Stats[0]) + strMod).grid(row=1,column=0)
        self.tk.Label(Frame,text="DEX: " + str(Stats[1]) + dexMod).grid(row=1,column=1)
        self.tk.Label(Frame,text="CON: " + str(Stats[2]) + conMod).grid(row=1,column=2)
        self.tk.Label(Frame,text="INT: " + str(Stats[3]) + intMod).grid(row=1,column=3)
        self.tk.Label(Frame,text="WIS: " + str(Stats[4]) + wisMod).grid(row=1,column=4)
        self.tk.Label(Frame,text="CHA: " + str(Stats[5]) + chaMod).grid(row=1,column=5)
        
        return Frame
        
    def equipment_Print(self,equipFrame,weaponFrame,armorFrame,credits,equipment):
        i = len(equipment) - 1
        temp = [0]
        while i > 0:
            temp.append(0)
            i -= 1
        
        Row = 1
        
        #Weapons
        self.tk.Label(weaponFrame,text="Weapons: ").grid(row=0,column=0)
        i = len(equipment) - 1
        k = 0
        while i > -1:
            if equipment[i] == "Spear (1d6 + 1 damage)" or equipment[i] == "Knife (1d4 damage)" or equipment[i] == "Monoblade Sword (1d8 + 1 damage)" or equipment[i] == "Thermal Knife (1d6 damage)" or equipment[i] == "Laser Pistol (1d6 damage)" or equipment[i] == "Monoblade Knife (1d6 damage)" or equipment[i] == "Combat Rifle (1d12 damage)" or equipment[i] == "Laser Rifle (1d10)" and temp[i] == 0:
                self.tk.Label(weaponFrame,text=equipment[i]).grid(row=Row,column=0)
                temp[i] = -1
                Row += 1
                k += 1

            i -= 1
        
        if k == 0:
            self.tk.Label(weaponFrame,text="None").grid(row=1,column=0)

        Row = 1

        #Armor
        self.tk.Label(armorFrame,text="Armor: ").grid(row=0,column=0)
        ac = 10
        i = len(equipment) - 1
        while i > -1:
            if equipment[i] == "Primitive Hide Armor (AC 13)" and temp[i] == 0:
                ac = 13
                self.tk.Label(armorFrame,text=equipment[i]).grid(row=Row,column=0)
                Row += 1
                temp[i] = -1

            if equipment[i] == "Woven Body Armor (AC 15)" and temp[i] == 0:
                ac = 15
                self.tk.Label(armorFrame,text=equipment[i]).grid(row=Row,column=0)
                Row += 1
                temp[i] = -1

            if equipment[i] == "Secure Clothing (AC 13)" and temp[i] == 0:
                ac = 13
                self.tk.Label(armorFrame,text=equipment[i]).grid(row=Row,column=0)
                Row += 1
                temp[i] = -1

            if equipment[i] == "Armored Undersuit (AC 13)" and temp[i] == 0:
                ac = 13
                self.tk.Label(armorFrame,text=equipment[i]).grid(row=Row,column=0)
                Row += 1
                temp[i] = -1

            if equipment[i] == "Armored Vacc Suit (AC 13)" and temp[i] == 0:
                ac = 13
                self.tk.Label(armorFrame,text=equipment[i]).grid(row=Row,column=0)
                Row += 1
                temp[i] = -1

            if equipment[i] == "Primitive Sheild (+1 AC)" and temp[i] == 0:
                ac += 1
                self.tk.Label(armorFrame,text=equipment[i]).grid(row=Row,column=0)
                Row += 1
                temp[i] = -1
            
            i -= 1

        self.tk.Label(armorFrame,text="AC: " + str(ac)).grid(row=Row,column=0)

        #Equipment
        self.tk.Label(equipFrame,text="Equipment: ").grid(row=0,column=0)
        i = len(equipment) - 1
        while i > -1:

            if temp[i] == 0:
                self.tk.Label(equipFrame,text=equipment[i]).grid(row=Row,column=0)
                Row += 1
                temp[i] = -1
            
            i -= 1
        
        self.tk.Label(equipFrame,text="Credits: " + str(credits)).grid(row=Row,column=0)
        
        return equipFrame,weaponFrame,armorFrame

import Main

if __name__ == '__main__':
    Main.main()
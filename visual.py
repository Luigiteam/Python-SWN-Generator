#Credit Goes to Luigiteam on GitHub
#https://github.com/Luigiteam/Python-SWN-Generator

from tkinter import *
import Main

def Window(Abillities,level):

    window = Tk()    

    # Has Name, Level and class, background, hp and ss
    Other = Frame(window,bd=9,highlightbackground="black",highlightthickness=2,height=175,width=150)
    other_Print(Other,Abillities,level)
    Other.place(x = 5, y = 5)
    Other.propagate(0)

    window.update_idletasks()
    other_Width = Other.winfo_width()
    other_Height = Other.winfo_height()

    Saves = Frame(window,bd=9,highlightbackground="black",highlightthickness=2,height=175,width=150)
    Saves = saves_Print(Saves,Abillities[4])
    Saves.place(x = other_Width + 10, y = 5)



    Skills = Frame(window,bd=9,highlightbackground="black",highlightthickness=2,height=175,width=150)
    Label(Skills,text="Skills: ").grid(row=0,column=0)
    Skills = skills_Print(Skills,Abillities[1])
    Skills.place(x = 5, y = other_Height + 10)
    Skills.pack_propagate(0) 

    window.update_idletasks()
    skill_Width = Skills.winfo_width()

    Foci = Frame(window,bd=9,highlightbackground="black",highlightthickness=2,height=175,width=150)
    Label(Foci,text="Foci:").grid(row=0,column=0)
    Foci = foci_Print(Foci,Abillities[3])
    Foci.place(x=skill_Width + 10,y=other_Height + 10)

    Psy = None

    if Abillities[7][2] > 0:
        Psy = Frame(window,bd=9,highlightbackground="black",highlightthickness=2,height=175,width=150)   


    

    window.geometry("840x600")
    window.resizable(0,0)

    window.mainloop()
    

def recenter(stat,row):
    col = None
    if stat == 5:
        col = 1

    if stat == 10:
        col = 2
    
    if row == 6:
        row = 1
    
    return row,col

def skills_Print(Frame,skills):
    Col = 0

    stat = 0

    Row = 1

    for i in range(1,19):

        if i == 1 and skills[0] >= 0:
            Label(Frame,text=" Administer level " + str(skills[0]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 2 and skills[1] >= 0:
            Label(Frame,text=" Connect level " + str(skills[1]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 3 and skills[2] >= 0:
            Label(Frame,text=" Exert level " + str(skills[2]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 4 and skills[3] >= 0:
            Label(Frame,text=" Fix level " + str(skills[3]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 5 and skills[4] >= 0:
            Label(Frame,text=" Heal level " + str(skills[4]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 6 and skills[5] >= 0:
            Label(Frame,text=" Know level " + str(skills[5]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 7 and skills[6] >= 0:
            Label(Frame,text=" Lead level " + str(skills[6]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 8 and skills[7] >= 0:
            Label(Frame,text=" Notice level " + str(skills[7]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 9 and skills[8] >= 0:
            Label(Frame,text=" Perform level " + str(skills[8]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 10 and skills[9] >= 0:
            Label(Frame,text=" Pilot level " + str(skills[9]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 11 and skills[10] >= 0:
            Label(Frame,text=" Program level " + str(skills[10]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 12 and skills[11] >= 0:
            Label(Frame,text=" Punch level " + str(skills[11]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 13 and skills[12] >= 0:
            Label(Frame,text=" Shoot level " + str(skills[12]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 14 and skills[13] >= 0:
            Label(Frame,text=" Sneak Level " + str(skills[13]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 15 and skills[14] >= 0:
            Label(Frame,text=" Stab level " + str(skills[14]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 16 and skills[15] >= 0:
            Label(Frame,text=" Survive level " + str(skills[15]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 17 and skills[16] >= 0:
            Label(Frame,text=" Talk level " + str(skills[16]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 18 and skills[17] >= 0:
            Label(Frame,text=" Trade level " + str(skills[17]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 19 and skills[18] >= 0:
            Label(Frame,text=" Work level " + str(skills[18]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Row)


    return Frame

def psy_Print(Frame,Psy):
    pass

def foci_Print(Frame,foci):
    stat = 0

    Col = 0

    Row = 1

    for i in range(0,22):
        if i == 0 and foci[0] >= 1:
            Label(Frame,text="Alert level " + str(foci[0])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 1 and foci[1] >= 1:
            Label(Frame,text="Armsman level " + str(foci[1])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 2 and foci[2] >= 1:
            Label(Frame,text="Assassin level " + str(foci[2]))
            stat += 1
            Row += 1
        
        if i == 3 and foci[3] >= 1:
            Label(Frame,text="Authority level " + str(foci[3])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 4 and foci[4] >= 1:
            Label(Frame,text="Close Combat level " + str(foci[4])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 5 and foci[5] >= 1:
            Label(Frame,text="Connected level " + str(foci[5])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 6 and foci[6] >= 1:
            Label(Frame,text="Die Hard level " + str(foci[6])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
            
        if i == 7 and foci[7] >= 1:
            Label(Frame,text="Diplomat level " + str(foci[7])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 8 and foci[8] >= 1:
            Label(Frame,text="Gunslinger level " + str(foci[8])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 9 and foci[9] >= 1:
            Label(Frame,text="Hacker level " + str(foci[9])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 10 and foci[10] >= 1:
            Label(Frame,text="Healer level " + str(foci[10])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 11 and foci[11] >= 1:
            Label(Frame,text="Henchkeeper level " + str(foci[11])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 12 and foci[12] >= 1:
            Label(Frame,text="Iron Hide level " + str(foci[12])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 13 and foci[13] >= 1:
            Label(Frame,text="Psychic Training level " + str(foci[13])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 14 and foci[14] >= 1:
            Label(Frame,text="Savage Fray level " + str(foci[14])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 15 and foci[15] >= 1:
            Label(Frame,text="Shocking Assault level " + str(foci[15])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 16 and foci[16] >= 1:
            Label(Frame,text="Sniper level " + str(foci[16])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 17 and foci[17] >= 1:
            Label(Frame,text="Specialist level " + str(foci[17])).grid(row=Row,column=Col)
            stat += 1  
            Row += 1 
        
        if i == 18 and foci[18] >= 1:
            Label(Frame,text="Star Captain level " + str(foci[18])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 19 and foci[19] >= 1:
            Label(Frame,text="Starfarer level " + str(foci[19])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 20 and foci[20] >= 1:
            Label(Frame,text="Tinker level " + str(foci[20])).grid(row=Row,column=Col)
            stat += 1
            Row += 1

        if i == 21 and foci[21] >= 1:
            Label(Frame,text="Unarmed Combantaint level " + str(foci[20])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 22 and foci[22] >= 1:
            Label(Frame,text="Wanderer level " + str(foci[22])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        if i == 23 and foci[23] >= 1:
            Label(Frame,text="Wild Psychic Talent level " + str(foci[23])).grid(row=Row,column=Col)
            stat += 1
            Row += 1

        Row, Col = recenter(stat,Row)

    return Frame

def other_Print(Frame,other,level):

    #Full Name
    Label(Frame,text=other[6][1]).grid(row=0,column=0)

    #Level and Class
    if other[7][0] == 2:
        Label(Frame,text="Level " + str(level) + " | Full Warrior").grid(row=1,column=0)
    
    elif other[7][1] == 2:
        Label(Frame,text="Level " + str(level) + " | Full Expert").grid(row=1,column=0)
    
    elif other[7][2] == 2:
        Label(Frame,text="Level " + str(level) + " | Full Psychic").grid(row=1,column=0)

    elif other[7][0] == 1 and other[7][1] == 1:
        Label(Frame,text="Level " + str(level) + " | Half Warrior Half Expert").grid(row=1,column=0)
    
    elif other[7][0] == 1 and other[7][2] == 1:
        Label(Frame,text="Level " + str(level) + " | Half Warrior Half Psychic").grid(row=1,column=0)
    
    elif other[7][1] == 1 and other[7][2] == 1:
        Label(Frame,text="Level " + str(level) + " | Half Expert Half Psychic").grid(row=1,column=0)

    #Background
    Label(Frame,text="Background: " + other[6][2]).grid(row=2,column=0)

    #HP and SS
    Label(Frame,text="HP: " + str(other[10][0]) + "/" + str(other[10][0])
            + " | SS: 0/" + str(other[10][1])).grid(row=3,column=0)



    return Frame

def saves_Print(Frame,saves):
    # SAVE: array[4] P[0],E[1], and M[2]. array [5] AC[0], and AB[1] 
    # array [6], Effort[0], FullName[1], Backprint[2], and BackprintNUM[3],
    # array [7][War[0], Exp[1], and Psy[2],
    # Credits[8],Equipment[9],
    # Array[10] hp[0], ss[1]
    
    Label(Frame, text="Saving Throws: ").grid(row=0,column=0)

    Label(Frame,text="Physical: " + str(saves[0])).grid(row=1,column=0)
    Label(Frame,text="Evasion: " + str(saves[1])).grid(row=2,column=0)
    Label(Frame,text="Mental: " + str(saves[2])).grid(row=3,column=0)

    return Frame
    

if __name__ == '__main__':
    Main.main()
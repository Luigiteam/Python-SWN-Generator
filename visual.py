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
    skills_Print(Skills,Abillities[1])
    Skills.place(x = 5, y = other_Height + 10)
    Skills.pack_propagate(0) 

    Psy = None

    if Abillities[7][2] > 0:
        Psy = Frame(window,bd=9,highlightbackground="black",highlightthickness=2,height=175,width=150)   

    Foci = Frame(window,bd=9,highlightbackground="black",highlightthickness=2,height=175,width=150) 

    Label(Skills,text="Skills: ").grid(row=0,column=0)

    

    window.geometry("840x600")
    window.resizable(0,0)

    window.mainloop()
    

def recenter(stat,Col,Row):
    if stat == 5:
        Col = 1

    if stat == 10:
        Col = 2
    
    if Row == 6:
        Row = 1
    
    return Row,Col

def skills_Print(Frame,skills):
    Col = 0

    stat = 0

    Row = 1


    for i in range(1,19):

        if i == 1 and skills[0] >= 0:
            Label(Frame,text=" Administer level " + str(skills[0]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        Row,Col = recenter(stat,Col,Row)
        
        if i == 2 and skills[1] >= 0:
            Label(Frame,text=" Connect level " + str(skills[1]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 3 and skills[2] >= 0:
            Label(Frame,text=" Exert level " + str(skills[2]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        Row,Col = recenter(stat,Col,Row)

        if i == 4 and skills[3] >= 0:
            Label(Frame,text=" Fix level " + str(skills[3]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        Row,Col = recenter(stat,Col,Row)
        
        if i == 5 and skills[4] >= 0:
            Label(Frame,text=" Heal level " + str(skills[4]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 6 and skills[5] >= 0:
            Label(Frame,text=" Know level " + str(skills[5]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        Row,Col = recenter(stat,Col,Row)

        if i == 7 and skills[6] >= 0:
            Label(Frame,text=" Lead level " + str(skills[6]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 8 and skills[7] >= 0:
            Label(Frame,text=" Notice level " + str(skills[7]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 9 and skills[8] >= 0:
            Label(Frame,text=" Perform level " + str(skills[8]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 10 and skills[9] >= 0:
            Label(Frame,text=" Pilot level " + str(skills[9]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1

        Row,Col = recenter(stat,Col,Row)

        if i == 11 and skills[10] >= 0:
            Label(Frame,text=" Program level " + str(skills[10]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 12 and skills[11] >= 0:
            Label(Frame,text=" Punch level " + str(skills[11]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 13 and skills[12] >= 0:
            Label(Frame,text=" Shoot level " + str(skills[12]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 14 and skills[13] >= 0:
            Label(Frame,text=" Sneak Level " + str(skills[13]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 15 and skills[14] >= 0:
            Label(Frame,text=" Stab level " + str(skills[14]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 16 and skills[15] >= 0:
            Label(Frame,text=" Survive level " + str(skills[15]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 17 and skills[16] >= 0:
            Label(Frame,text=" Talk level " + str(skills[16]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)

        if i == 18 and skills[17] >= 0:
            Label(Frame,text=" Trade level " + str(skills[17]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)
        
        if i == 19 and skills[18] >= 0:
            Label(Frame,text=" Work level " + str(skills[18]) + " ").grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        Row,Col = recenter(stat,Col,Row)


    return Frame

def psy_Print(Frame,Psy):
    pass

def foci_Print(Frame,foci):
    pass

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
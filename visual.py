from tkinter import *
import Main

def Window(Abillities):

    window = Tk()

    Skills = Frame(window,bg="pink",bd=9,height=175,width=150)
    Skills.place(x = 160, y = 0)
    Skills.pack_propagate(0) 

    tagS = Label(Skills).grid(row=0,column=0)


    Label(Skills,text="Skills: ").grid(row=0,column=0)
    test = None
    test = skills_Print(Skills,Abillities[1])
    

    

    window.geometry("840x600")
    window.resizable(0,0)
    
    window.mainloop()

def skills_Print(Frame,skills):
    Col = 0

    stat = 1

    Row = 1

    for i in range(1,19):

        if stat == 5:
            Col = 1
        
        if Row == 6:
            Row = 1

        if i == 1 and skills[0] >= 0:
            Label(Frame,text="Administer level " + str(skills[0])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 2 and skills[1] >= 0:
            Label(Frame,text="Connect level " + str(skills[1])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 3 and skills[2] >= 0:
            Label(Frame,text="Exert level " + str(skills[2])).grid(row=Row,column=Col)
            stat += 1
            Row += 1

        elif i == 4 and skills[3] >= 0:
            Label(Frame,text="Fix level " + str(skills[3])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 5 and skills[4] >= 0:
            Label(Frame,text="Heal level " + str(skills[4])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 6 and skills[5] >= 0:
            Label(Frame,text="Know level " + str(skills[5])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
            
        elif i == 7 and skills[6] >= 0:
            Label(Frame,text="Lead level " + str(skills[6])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 8 and skills[7] >= 0:
            Label(Frame,text="Notice level " + str(skills[7])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 9 and skills[8] >= 0:
            Label(Frame,text="Perform level " + str(skills[8])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 10 and skills[9] >= 0:
            Label(Frame,text="Pilot level " + str(skills[9])).grid(row=Row,column=Col)
            stat += 1
            Row += 1

        elif i == 11 and skills[10] >= 0:
            Label(Frame,text="Program level " + str(skills[10])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 12 and skills[11] >= 0:
            Label(Frame,text="Punch level " + str(skills[11])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 13 and skills[12] >= 0:
            Label(Frame,text="Shoot level " + str(skills[12])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 14 and skills[13] >= 0:
            Label(Frame,text="Sneak Level " + str(skills[13])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 15 and skills[14] >= 0:
            Label(Frame,text="Stab level " + str(skills[14])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 16 and skills[15] >= 0:
            Label(Frame,text="Survive level " + str(skills[15])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 17 and skills[16] >= 0:
            Label(Frame,text="Talk level " + str(skills[16])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 18 and skills[17] >= 0:
            Label(Frame,text="Trade level " + str(skills[17])).grid(row=Row,column=Col)
            stat += 1
            Row += 1
        
        elif i == 19 and skills[18] >= 0:
            Label(Frame,text="Work level " + str(skills[18])).grid(row=Row,column=Col)
            stat += 1
            Row += 1

    return Frame

if __name__ == '__main__':
    Main.main()
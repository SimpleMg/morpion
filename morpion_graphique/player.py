from random import choice


class Player:
    def __init__(self):
        self.signe = ["X", "O"]
        self.name_user = ""

    def _name_user(self):
        name_user = input("votre nom de joueur: ")
        self.name_user = name_user
        return name_user

    
    def place_signe_ia(self,tabJeux, joue, canvas):
        copy_tabJeux = [j for i in tabJeux for j in i if type(j) == int]
        ia_choice = choice(copy_tabJeux)
        for i in range(len(tabJeux)):
            for j in range(len(tabJeux[i])):
                if tabJeux[i][j] == ia_choice:
                    ia_choice_x, ia_choice_y = i , j
                    break
        #partie du haut
        if tabJeux[0][0] == tabJeux[ia_choice_x][ia_choice_y]:
            if joue == 0:
                #croix
                canvas.create_line(0,0,660,340,fill="black")
                canvas.create_line(660,0,0,340,fill="black")
                tabJeux[0][0] = "X"
            else:
                #cercle
                canvas.create_oval(100,10,500,290,width=2,outline="red")
                tabJeux[0][0] = "O"

        elif tabJeux[0][1] == tabJeux[ia_choice_x][ia_choice_y]:
            if joue == 0:
                #croix
                canvas.create_line(660,0,1260,340,fill="black")
                canvas.create_line(1260,0,660,340,fill="black")
                tabJeux[0][1] = "X"
            else:
                #cercle
                canvas.create_oval(700,10,1200,290,width=2,outline="red")
                tabJeux[0][1] = "O"
        elif tabJeux[0][2] == tabJeux[ia_choice_x][ia_choice_y]:
            if joue == 0:
                #croix
                canvas.create_line(1260,0,1920,330,fill="black")
                canvas.create_line(1920,0,1260,340,fill="black")
                tabJeux[0][2] = "X"
            else:
                #cercle
                canvas.create_oval(1300,10,1800,290,width=2,outline="red")
                tabJeux[0][2] = "O"
        #partie du milieu
        elif tabJeux[1][0] == tabJeux[ia_choice_x][ia_choice_y]:
            if joue == 0:
                #croix
                canvas.create_line(0,340,660,640,fill="black")
                canvas.create_line(660,340,0,640,fill="black")
                tabJeux[1][0] = "X"
            else:
                #cercle
                canvas.create_oval(100,350,500,630,width=2,outline="red")
                tabJeux[1][0] = "O"
        elif tabJeux[1][1] == tabJeux[ia_choice_x][ia_choice_y]:
            if joue == 0:
                #croix
                canvas.create_line(1260,340,660,640,fill="black")
                canvas.create_line(660,340,1260,640,fill="black")
                tabJeux[1][1] = "X"
            else:
                #cercle
                canvas.create_oval(700,350,1200,630,width=2,outline="red")
                tabJeux[1][1]  = "O"
        elif tabJeux[1][2] == tabJeux[ia_choice_x][ia_choice_y]:
            if joue == 0:
                #croix
                canvas.create_line(1920,340,1260,640,fill="black")
                canvas.create_line(1260,340,1920,640,fill="black")
                tabJeux[1][2] = "X"
            else:
                #cercle
                canvas.create_oval(1300,350,1800,630,width=2,outline="red")
                tabJeux[1][2] = "O"
        #partie du bas
        elif tabJeux[2][0] == tabJeux[ia_choice_x][ia_choice_y]:
            if joue == 0:
                #croix
                canvas.create_line(660,640,0,1080,fill="black")
                canvas.create_line(0,640,660,1080,fill="black")
                tabJeux[2][0] = "X"
            else:
                #cercle
                canvas.create_oval(100,650,500,1070,width=2,outline="red")
                tabJeux[2][0] = "O"
        elif tabJeux[2][1] == tabJeux[ia_choice_x][ia_choice_y]:
            if joue == 0:
                #croix
                canvas.create_line(1260,640,660,1080,fill="black")
                canvas.create_line(660,640,1260,1080,fill="black")
                tabJeux[2][1] = "X"
            else:
                #cercle
                canvas.create_oval(700,650,1200,1070,width=2,outline="red")
                tabJeux[2][1] = "O"
        elif tabJeux[2][2] == tabJeux[ia_choice_x][ia_choice_y]:
            if joue == 0:
                #croix
                canvas.create_line(1920,640,1260,1080,fill="black")
                canvas.create_line(1920,1080,1260,640,fill="black")
                tabJeux[2][2] = "X"
            else:
                #cercle
                canvas.create_oval(1300,650,1800,1070,width=2,outline="red")
                tabJeux[2][2] = "O"
        #si nul part
        else:
            pass


    def place_signe(self, joue, xe, ye,calculGX1, calculGX2, tabJeux, canvas):
        #partie du haut
        if 0 < xe < calculGX1 and 0 < ye < 330 and type(tabJeux[0][0]) != str:
            if joue == 0:
                #croix
                canvas.create_line(0,0,660,340,fill="black")
                canvas.create_line(660,0,0,340,fill="black")
                tabJeux[0][0] = "X"
            else:
                #cercle
                canvas.create_oval(100,10,500,290,width=2,outline="red")
                tabJeux[0][0] = "O"
        elif calculGX1 < xe < calculGX2 and 0 < ye < 330 and type(tabJeux[0][1]) != str:
            if joue == 0:
                #croix
                canvas.create_line(660,0,1260,340,fill="black")
                canvas.create_line(1260,0,660,340,fill="black")
                tabJeux[0][1] = "X"
            else:
                #cercle
                canvas.create_oval(700,10,1200,290,width=2,outline="red")
                tabJeux[0][1] = "O"
        elif xe > calculGX2 and 0 < ye < 330 and type(tabJeux[0][2]) != str:
            if joue == 0:
                #croix
                canvas.create_line(1260,0,1920,330,fill="black")
                canvas.create_line(1920,0,1260,340,fill="black")
                tabJeux[0][2] = "X"
            else:
                #cercle
                canvas.create_oval(1300,10,1800,290,width=2,outline="red")
                tabJeux[0][2] = "O"
        #partie du milieu
        elif 0 < xe < calculGX1 and 330 < ye < 630 and type(tabJeux[1][0]) != str:
            if joue == 0:
                #croix
                canvas.create_line(0,340,660,640,fill="black")
                canvas.create_line(660,340,0,640,fill="black")
                tabJeux[1][0] = "X"
            else:
                #cercle
                canvas.create_oval(100,350,500,630,width=2,outline="red")
                tabJeux[1][0] = "O"
        elif calculGX1 < xe < calculGX2 and 330 < ye < 630 and type(tabJeux[1][1]) != str:
            if joue == 0:
                #croix
                canvas.create_line(1260,340,660,640,fill="black")
                canvas.create_line(660,340,1260,640,fill="black")
                tabJeux[1][1] = "X"
            else:
                #cercle
                canvas.create_oval(700,350,1200,630,width=2,outline="red")
                tabJeux[1][1]  = "O"
        elif xe > calculGX2 and 330 < ye < 630 and type(tabJeux[1][2]) != str:
            if joue == 0:
                #croix
                canvas.create_line(1920,340,1260,640,fill="black")
                canvas.create_line(1260,340,1920,640,fill="black")
                tabJeux[1][2] = "X"
            else:
                #cercle
                canvas.create_oval(1300,350,1800,630,width=2,outline="red")
                tabJeux[1][2] = "O"
        #partie du bas
        elif 0 < xe < calculGX1 and 650 < ye < 1080 and type(tabJeux[2][0]) != str:
            if joue == 0:
                #croix
                canvas.create_line(660,640,0,1080,fill="black")
                canvas.create_line(0,640,660,1080,fill="black")
                tabJeux[2][0] = "X"
            else:
                #cercle
                canvas.create_oval(100,650,500,1070,width=2,outline="red")
                tabJeux[2][0] = "O"
        elif calculGX1 < xe < calculGX2 and 650 < ye < 1080 and type(tabJeux[2][1]) != str:
            if joue == 0:
                #croix
                canvas.create_line(1260,640,660,1080,fill="black")
                canvas.create_line(660,640,1260,1080,fill="black")
                tabJeux[2][1] = "X"
            else:
                #cercle
                canvas.create_oval(700,650,1200,1070,width=2,outline="red")
                tabJeux[2][1] = "O"
        elif xe > calculGX2 and 650 < ye < 1080 and type(tabJeux[2][2]) != str:
            if joue == 0:
                #croix
                canvas.create_line(1920,640,1260,1080,fill="black")
                canvas.create_line(1920,1080,1260,640,fill="black")
                tabJeux[2][2] = "X"
            else:
                #cercle
                canvas.create_oval(1300,650,1800,1070,width=2,outline="red")
                tabJeux[2][2] = "O"
        #si nul part
        else:
            print("déjà attribuer ou pas dans la grille")
            self.test_pass = True
            self.si_pas_dans_grille = joue


    def choice_signe(self):
        for i in range(len(self.signe)):
            print("{} {}".format(i, self.signe[i]))
        choice_user = int(input("choisir un signe: "))
        return choice_user
    

    

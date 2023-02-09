from tkinter import *
from player import Player

class MyGame:
    def __init__(self):
        #signe et nom des joueurs
        self.player_1 = Player()
        self.player_2 = Player()
        self.signe_user1 =  self.player_1.choice_signe()
        self.tabJeux = [[0,1,2],[3,4,5],[6,7,8]]
        self.signe = ["X", "O"]
        if self.signe_user1 == 0:
            self.signe_user2 = 1
        else:
            self.signe_user2 = 0
        self.name_player1 = self.player_1._name_user()
        self.name_player2 = self.player_2._name_user()
        self.listJ = [self.name_player1, self.name_player2]
        self.dictJ = {self.name_player1:self.signe_user1, self.name_player2:self.signe_user2}
        #pour la fenetre tkinter
        self.calculGX1 = (1920/2) - 300
        self.calculGX2 = (1920/2) + 300
        self.calculGY1 = (1080/2) - 200
        self.calculGY2 = (1080/2) + 100
        self.fenetre = Tk()
        self.canvas = Canvas(self.fenetre, width=1920, height=1080)
        #fonction _tourPlay et _trace
        self.changementP = 0
        self.test_pass = False
        self.si_pas_dans_grille = 0

    def _horizontal_check(self):
        for i in range(len(self.tabJeux)):
            for j in range(len(self.tabJeux[i])):
                if len(set(self.tabJeux[i])) == 1:
                    return [True, self.signe.index(self.tabJeux[i][j])]
        return [False, False]


    def _ligne_check(self):
        f = []
        cpt = 0
        for i in range(3):
            for i in range(len(self.tabJeux)):
                for j in range(len(self.tabJeux[i])):
                    f.append(self.tabJeux[i][cpt])
            if len(set(f)) == 1:
                return [True, self.signe.index(f[0])]
            cpt += 1
            f = []
        return [False, False]


    def _diagonale_check(self,right=False):
        if not right:
            f = []
            cpt = 0
            for i in range(len(self.tabJeux)):
                f.append(self.tabJeux[i][cpt])
                cpt += 1
            if len(set(f)) == 1:
                return [True, self.signe.index(f[0])]
            return [False, False]
        else:
            f = []
            cpt = 2
            for i in range(len(self.tabJeux)):
                f.append(self.tabJeux[i][cpt])
                cpt -= 1
            if len(set(f)) == 1:
                return [True, self.signe.index(f[0])]
            return [False, False]



    def _find_key(self,j,v): 
        for k, val in self.dictJ.items(): 
            if self.tabJeux[j][v] == self.signe[val]: 
                return k 
        return "Key don't exist"


    def _change_play(self):
        for i in range(len(self.listJ)):
            if self.changementP == i:
                return self.listJ[i]


    def _tourPlay(self):
        if not self.test_pass: 
            j = self._change_play()
            print("joueur {} joue".format(j))
            if self.changementP == 0:
                self.changementP += 1
            else:
                self.changementP = 0
            return self.dictJ[j]
        return self.si_pas_dans_grille


    def _is_winner(self):
        checkH0 = self._horizontal_check()
        if checkH0[0]:
            return self._find_key(0,checkH0[1])
        checkH1 = self._horizontal_check()
        if checkH1[0]:
            return self._find_key(1,checkH0[1])
        checkH2 = self._horizontal_check()
        if checkH2[0]:
            return self._find_key(2,checkH0[1])
        checkL0 = self._ligne_check()
        if checkL0[0]:
            return self._find_key(0,checkL0[1])
        checkL1 = self._ligne_check()
        if checkL1[0]:
            return self._find_key(1,checkL1[1])
        checkL2 = self._ligne_check()
        if checkL2[0]:
            return self._find_key(2,checkL2[1])
        checkD0 = self._diagonale_check()
        if checkD0[0]:
            return self._find_key(0,checkD0[1])
        checkD1 = self._diagonale_check(True)
        if checkD1[0]:
            return self._find_key(1,checkD1[1])
        else:
            return False


    def _calcul_ia(self):
        pass
       

    def _trace(self,event):
        xe = event.x
        ye = event.y
        joue = self._tourPlay()
        self.test_pass = False
        d = self._is_winner()
        if d != False:
            print("le gagnant est ", d)
            self.fenetre.quit()
            return
        else:
            f = False
            for i in range(len(self.tabJeux)):
                for j in range(len(self.tabJeux[i])):
                    if type(self.tabJeux[i][j]) == int:
                        f = True
            if f:
                pass
            else:
                self.fenetre.quit()
        self.player_1.place_signe(joue, xe,ye,self.calculGX1, self.calculGX2, self.tabJeux, self.canvas)
        if self.name_player2 == "ia":
            joue = self._tourPlay()
            print("ia = {}".format(joue))
            self.player_2.place_signe_ia(self.tabJeux, joue, self.canvas)
        else:
            self.player_2.place_signe(joue, xe, ye,self.calculGX1, self.calculGX2, self.tabJeux, self.canvas)
        print("on est en x {} et y {}".format(xe,ye))
        print(self.tabJeux)


    def start_morpion(self):
        #ligne vertical
        self.canvas.create_line(self.calculGX1, 0, self.calculGX1, 1080)
        self.canvas.create_line(self.calculGX2, 0,self.calculGX2, 1080)
        #ligne horizontale
        self.canvas.create_line(0, self.calculGY1, 1920, self.calculGY1)
        self.canvas.create_line(0, self.calculGY2, 1920, self.calculGY2)
        self.canvas.pack()
        #coordonne et loop de la fneetre
        self.fenetre.bind('<Button-1>', self._trace)
        self.fenetre.mainloop()
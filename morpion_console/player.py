
class Player:
    def __init__(self,numJ):
        self.numJ = numJ
    

    def name_user(self):
        name_user = input("votre pseudo joueur {}: ".format(self.numJ))
        return name_user


    def choice_signe(self, signe):
        signe_user = -1
        for i in range(len(signe)):
            print("{} - {}".format(i, signe[i]))
        while signe_user < 0 or signe_user > 1:
            try:
                signe_user = int(input("joueur {} choisissez votre signe: ".format(self.numJ)))
            except:
                pass
        return signe[signe_user]
    
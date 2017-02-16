import json
import random

def load_db():
    with open("Game.json", "r") as file:
        db = json.loads(file.read())

    with open("Game_bosse.json", "r") as file:
        db_bosse = json.loads(file.read())

    return db, db_bosse

def save_db(db, db_bosse):
    with open("Game.json", "w") as file:
        file.write(json.dumps(db, indent=4))

    with open("Game_bosse.json", "w") as file:
        file.write(json.dumps(db_bosse, indent=3))

class createperso():
    def __init__(self, pseudo, passeword, life=50, attack=10, level=1, experience=0):
        self.pseudo = pseudo
        self.passeword = passeword
        self.life = life
        self.attack = attack
        self.level = level
        self.experience = experience

    def save(self):
        DataBase[pseudo] = {"passeword": self.passeword, "level": self.level,
                            "attack": self.attack, "life": self.life, "experience": self.experience}

        with open("Game.json", "w") as file:
            file.write(json.dumps(DataBase, indent=4))

    def stat(self):
        screen = "Pseudo: " + str(self.pseudo) + \
                 "\nNiveau: " + str(self.level) + "\nExperience: " + str(self.experience) + "\nVie: " + str(self.life) + \
                 "HP\nAttaque: " + str(self.attack)
        print(screen)

    def pex(self, xp):
        self.experience += xp
        if self.experience >= (50*int(self.level)):
            self.level += 1
            self.experience = 0
            self.life = round(100*(self.level-0.6))
            self.attack = round(50*(self.level-0.8))
            print("=========\nLevel up!\n=========")
            self.stat()

DataBase, DataBase_bosse = load_db()

while True:
    #connexion
    while True:
        ans_question = input("Etes-vous déjà enregistré? ")

        if ans_question == 'oui' or ans_question == 'yes':
            pseudo = input("Rentrer votre pseudo: ")
            passeword = input("Rentrer votre password: ")

            try:
                if DataBase[pseudo]["passeword"] == passeword:
                    play = DataBase[pseudo]
                    Player = createperso(pseudo, play["passeword"], play["life"],
                                         play["attack"], play["level"], play["experience"])
                    print("Connexion réussit\n")
                    break

            except:
                print("Ce compte n'éxiste pas\n")

        elif ans_question == 'non' or ans_question == 'no':
            answer = input("Souhaitez-vous vous enregistrer? ")

            if answer == "oui" or answer == 'yes':
                pseudo = input("Rentrer votre pseudo: ")
                passeword = input("Rentrer votre password: ")

                Gamer = createperso(pseudo, passeword)
                Gamer.save()
                Player = Gamer

                print("Votre compe à bien été créé\n")

                save_db(DataBase, DataBase_bosse)
                break

            elif answer == 'non' or answer == 'no':
                print("Bien")

    print("Pour connaître les commandes taper 'help'")

    #InGame
    while True:
        DataBase, DataBase_bosse = load_db()

        order = input("\n<Commande>: ")

        if order == 'help':
            print("     -Pour connaitre vos statistiques taper 'information'\n"
                  "     -Pour combattre taper 'combattre'\n"
                  "     -Pour vous deconnectez taper 'deconnexion'")

        if order == 'information':
            Player.stat()

        if order == 'combattre':
            mobs = DataBase_bosse[str(Player.level)]
            nbr = random.randint(0, len(mobs)-1)

            for i in mobs[nbr]:
                NameMob = i
                monster = mobs[nbr][i]

            print("     Vous étes tombé sur " + str(NameMob))
            print("     Vie: {}\n     Attaque: {}".format(monster["life"], monster['attack']))

            answer_comb = input("     Voulez vous combattre? ")

            if answer_comb == 'oui' or answer_comb == 'yes':
                HP = monster["life"]
                att = monster["attack"]

                while HP > 0:
                    HP -= Player.attack
                    Player.life -= att

                    if Player.life == 0:
                        print("     Vous étes mort")

                if Player.life > 0:
                    Player.pex(monster["experience"])

                Player.save()
                print("\n     Vous avez battu " + str(NameMob))
                print("     Il vous reste {}HP".format(Player.life))

        if order == 'deconnexion':
            break
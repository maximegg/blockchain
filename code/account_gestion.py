import hashlib
from blockchain import Blockchain

junglechain = Blockchain()


def account_exist(name):
    for position, line in enumerate(open("account/account_name", "r+")):
        if line == name + "\n":
            return True
    return False


def have_sold(name, m):
    for position, line in enumerate(open("account/" + name + ".txt", "r+")):
        if position in [1]:
            if m <= int(line):
                return True
            else:
                return False


class AccountGestion:

    def __init__(self):

        self.trade = []

        self.money = 0
        self.name = None

        while True:
            print("-----[Compte]-----")
            print("1: connection")
            print("2: s'inscrire")
            t = input("entrer le choix 1 ou 2:")
            if str(t) == "1":
                self.login()
                break
            elif str(t) == "2":
                self.login(self.register())
                break
            else:
                continue

    @staticmethod
    def erase():
        junglechain.erase()

    @staticmethod
    def display_chain():
        junglechain.display_chain()

    def getname(self):
        return self.name

    def getwallet(self):
        return self.money

    def setname(self, name):
        self.name = name

    def setwallet(self, name, n):
        file = open("account/"+name+".txt", "r+").readline()
        open("account/"+name+".txt", "w+").write(str(file)+str(n))
        if name == self.getname():
            self.money = n

    def login(self, account=None):
        if account is None:
            while True:
                print("----[connection]---")
                name = input("identifiant: ")
                if account_exist(name):
                    while True:
                        mdp = hashlib.sha256(input("entrer un mot de passe: ").encode()).digest()

                        file = open("account/" + name + ".txt", "r+").readline()
                        if str(file) == (str(mdp) + "\n"):
                            self.setname(name)
                            file = open("account/" + name + ".txt")
                            for position, line in enumerate(file):
                                if position in [1]:
                                    self.setwallet(name, int(line))
                            file.close()

                            print(self.getname())
                            print("solde: " + str(self.getwallet()))
                            break
                        else:
                            print("mot de passe incorrect!")
                    break

                else:
                    print("le compte n'existe pas.")

        else:
            name = account

            file = open("account/" + name + ".txt")
            for position, line in enumerate(file):
                if position in [1]:
                    self.setwallet(name, int(line))
            file.close()

    def register(self):
        print("----[S'incrire]----")
        while True:
            name = input("identifiant: ")
            if account_exist(name):
                print("le compte existe deja!")
            else:
                break
        while True:
            mdp = hashlib.sha256(input("entrer un mot de passe: ").encode()).digest()
            if mdp == hashlib.sha256(input("entrer a nouveau le mot de passe: ").encode()).digest():
                open("account/" + str(name) + ".txt", "w+").write(str(mdp) + "\n")
                open("account/" + str(name) + ".txt", "a+").write("0")
                open("account/account_name", "a+").write(str(name + "\n"))
                self.setwallet(name, 0)
                print("Compte créer")
                break
            else:
                print("le mot de passe ne correspond pas!")

        return name

    def gift(self, receiver, n):
        if account_exist(receiver):
            if have_sold(self.name, n):

                self.setwallet(str(self.getname()), int(self.getwallet())-int(n))
                file = open("account/" + str(receiver) + ".txt")
                for position, line in enumerate(file):
                    if position in [1]:
                        self.setwallet(str(receiver), int(line)+n)
                text = self.getname()+" a donné "+str(n)+" JungleCoin a "+str(receiver)
                self.trade.append(text+"\n")
                if len(self.trade) >= 10:
                    junglechain.create_block_from_transaction(self.trade)
                    self.trade = []

            else:
                print("vous n'avez pas assez d'argents")
        else:
            print("le compte du receveur n'existe pas!")

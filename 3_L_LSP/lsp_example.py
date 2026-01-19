class Animal:
    def comer(self):
        print("O animal esta comendo")

    def andar(self):
        print("O animal está andando na jaula")

class Felino(Animal):
    def lamber(self):
        print("O felino está lambendo seu pelo")


class Leao(Felino):
    def rugir(self):  
        print("O leao esta rugindo alto")

class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()

animal = Animal()
felino = Felino()
leao = Leao()
pessoa = Pessoa()

animal.comer()
felino.comer()
leao.comer()

pessoa.observa(animal)
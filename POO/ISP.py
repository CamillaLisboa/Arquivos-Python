from abc import ABC, abstractmethod

class TrabalhadorRuim(ABC):
    @abstractmethod
    def trabalhar(self): pass

    @abstractmethod
    def comer(self): pass

    @abstractmethod
    def dormir(self): pass


class RoboRuim(TrabalhadorRuim):
    def trabalhar(self):
        print("Robô trabalhando")
    def comer(self):   # desnecessário para robô
        print("Robô comendo (?)")
    def dormir(self):  # desnecessário para robô
        print("Robô dormindo (?)")


## refatorado

from abc import ABC, abstractmethod

class PodeTrabalhar(ABC):
    @abstractmethod
    def trabalhar(self): pass

class PodeComer(ABC):
    @abstractmethod
    def comer(self): pass

class PodeDormir(ABC):
    @abstractmethod
    def dormir(self): pass


class Humano(PodeTrabalhar, PodeComer, PodeDormir):
    def trabalhar(self):
        print("Humano trabalhando")
    def comer(self):
        print("Humano comendo")
    def dormir(self):
        print("Humano dormindo")


class Robo(PodeTrabalhar):
    def trabalhar(self):
        print("Robô trabalhando")



h = Humano()
h.trabalhar(); h.comer(); h.dormir()

r = Robo()
r.trabalhar()

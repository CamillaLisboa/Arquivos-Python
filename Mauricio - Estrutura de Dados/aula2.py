#Classese e objetos
class Calculadora:
    def __init__(self,a,b): #metodo construtor, executado no momento que o objeto e criad
        self.a = a
        self.b = b
    
    def Soma(self):
        return self.a + self.b
    
    def Subtrai(self):
        return self.a - self.b





x = Calculadora(30,10)

print(x.Soma())
print(x.Subtrai())
class PetTradicional:
    def __init__(self, nome, especie, idade, peso):
        self.__nome = nome
        self.__especie = especie
        self.__idade = idade
        self.__peso = peso

    def get_nome(self):
        return self.__nome
    
    def get_especie(self):
        return self.__especie
    
    def get_idade(self):
        return self.__idade
    
    def get_peso(self):
        return self.__peso
    

    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) > 0:
            self.__nome = nome.strip()
        else:
            raise ValueError("Nome deve ser uma string não vazia")
    
    def set_especie(self, especie):
        if isinstance(especie, str) and len(especie.strip()) > 0:
            self.__especie = especie.strip()
        else:
            raise ValueError("Espécie deve ser uma string não vazia")
    
    def set_idade(self, idade):
        if isinstance(idade, int) and idade >= 0:
            self.__idade = idade
        else:
            raise ValueError("Idade deve ser um número inteiro não negativo")
    
    def set_peso(self, peso):
        if isinstance(peso, (int, float)) and peso > 0:
            self.__peso = float(peso)
        else:
            raise ValueError("Peso deve ser um número positivo")
    
    def __str__(self):
        return f"Pet: {self.__nome}\nEspécie: {self.__especie}\nIdade: {self.__idade} anos\nPeso: {self.__peso} kg"
    

pet1 = PetTradicional("Buddy", "Cão", 3, 15.5)
print(f"Pet criado!\n\n{pet1}")

print(f"Nome: {pet1.get_nome()}")
print(f"Espécie: {pet1.get_especie()}")
print(f"Idade: {pet1.get_idade()}")
print(f"Peso: {pet1.get_peso()}")

pet1.set_nome("Max")
pet1.set_idade(4)
pet1.set_peso(16.2)
    
print(f"Pet atualizado!\n\n {pet1}")
class PetComAnnotations:
    
    def __init__(self, nome, especie, idade, peso):
        self._nome = nome
        self._especie = especie
        self._idade = idade
        self._peso = peso
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) > 0:
            self._nome = nome.strip()
        else:
            raise ValueError("Nome deve ser uma string não vazia")
    
    @property
    def especie(self):
        return self._especie
    
    @especie.setter
    def especie(self, especie):
        if isinstance(especie, str) and len(especie.strip()) > 0:
            self._especie = especie.strip()
        else:
            raise ValueError("Espécie deve ser uma string não vazia")
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int) and idade >= 0:
            self._idade = idade
        else:
            raise ValueError("Idade deve ser um número inteiro não negativo")
    
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, peso):
        if isinstance(peso, (int, float)) and peso > 0:
            self._peso = float(peso)
        else:
            raise ValueError("Peso deve ser um número positivo")
    
    def __str__(self):
        return f"Pet: {self._nome}\nEspécie: {self._especie}\nIdade: {self._idade} anos\nPeso: {self._peso} kg"
    
pet2 = PetComAnnotations("Mimi", "Gato", 2, 4.8)
print(f"Pet criado: {pet2}")


print(f"Nome: {pet2.nome}")
print(f"Espécie: {pet2.especie}")
print(f"Idade: {pet2.idade}")
print(f"Peso: {pet2.peso}")

pet2.nome = "Luna"
pet2.idade = 3
pet2.peso = 5.1
    
print(f"Pet atualizado!\n\n{pet2}")
from abc import ABC, abstractmethod

class Client(ABC):
    def __init__(self, id="", email="", phone="", address=""):
        self._email = email
        self._phone = phone
        self._address = address
        self._id = id

    @abstractmethod
    def valida_faturamento(self, valor=0):
        pass

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        self._address = value

    def __str__(self):
        return (f"--- Dados do Cliente ---\n"
                f"ID: {self._id}\n"
                f"E-mail: {self._email}\n"
                f"Telefone: {self._phone}\n"
                f"Endereço: {self._address}")


class PessoaFisica(Client):
    def __init__(self, id="", cpf="", name="", email="", phone="", address=""):
        super().__init__(id, email, phone, address)
        self._name = name
        self._cpf = cpf

    def valida_faturamento(self, valor=0):
        print('Análise de faturamento não se aplica')

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    def __str__(self):
        return (f"Pessoa Física\n"
                f"Nome: {self._name}\n"
                f"CPF: {self._cpf}\n"
                f"{super().__str__()}")


class PessoaJuridica(Client):
    def __init__(self, id="", cnpj="", razao_social="", tipo="", nome_fantasia="", email="", phone="", address=""):
        super().__init__(id, email, phone, address)
        self._cnpj = cnpj
        self._razao_social = razao_social
        self._tipo = tipo
        self._nome_fantasia = nome_fantasia

    def valida_faturamento(self, valor=0):
        if valor > 300000000:
            self.tipo = 'Grande Empresa'
        elif valor > 4800000:
            self.tipo = 'Média Empresa'
        elif valor > 360000:
            self.tipo = 'Pequena Empresa'
        else:
            self.tipo = 'Micro Empresa'

    @property
    def cnpj(self):
        return self._cnpj
    
    @cnpj.setter
    def cnpj(self, value):
        self._cnpj = value

    @property
    def razao_social(self):
        return self._razao_social
    
    @razao_social.setter
    def razao_social(self, value):
        self._razao_social = value

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def nome_fantasia(self):
        return self._nome_fantasia
    
    @nome_fantasia.setter
    def nome_fantasia(self, value):
        self._nome_fantasia = value

    def __str__(self):
        return (f"Pessoa Jurídica\n"
                f"CNPJ: {self._cnpj}\n"
                f"Razão Social: {self._razao_social}\n"
                f"Nome Fantasia: {self._nome_fantasia}\n"
                f"Tipo: {self._tipo}\n"
                f"{super().__str__()}")


# ====== TESTE ======
pf = PessoaFisica(
    id="1", cpf="137.334.667-13", name="Camilla",
    email="caschemar@gmail.com", phone="(21)98123-5592", address="Garça - SP"
)

pj = PessoaJuridica(
    id="2", cnpj="12.345.678/0001-99", razao_social="Tech Solutions LTDA",
    tipo="Média Empresa", nome_fantasia="TechSol",
    email="contato@techsol.com", phone="(11)99999-8888", address="São Paulo - SP"
)

print(pf)
print("---------------------##########----------------------")
print(pj)

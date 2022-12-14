class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo
        
    def desativar(self):
        self.ativo = False
        print (f"A pessoa '{self.nome}' foi desativada com sucesso.")

if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "123456", True)
    pessoa1.desativar()
    
    if (pessoa1.ativo == True):
        print (f"A pessoa '{pessoa1.nome}' está ativa")
    else:
        print (f"A pessoa '{pessoa1.nome}' não está ativa")



#Crie uma classe Livro que possui os atributos nome, qtdPaginas, autor e preço. 
#–Crie os métodos getPreco para obter o valor do preco e o método setPreco para setar um novo valor do preco. 
#Crie um codigo de teste

class Livro:
    def __init__(self, nome, qtdpaginas, autor, preco):
        self.nome = nome
        self.qtdpaginas = qtdpaginas
        self.autor = autor
        self.preco = preco
        
    def getPreco (self):
        return self.preco
    
    def setPreco (self, novoPreco):
        self.preco = novoPreco
        
livro1 = Livro("aspokaops", 20, "aosas", 50)
print (livro1.getPreco())
livro1.setPreco(30)
print(livro1.getPreco())

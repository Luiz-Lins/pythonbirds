class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é  {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    luiz = Mutante(nome='luiz')
    jose = Homem(luiz, nome='jose')
    print(Pessoa.cumprimentar(jose))
    print(id(jose))
    print(jose.cumprimentar())
    print(jose.nome)
    print(jose.idade)
    for filho in jose.filhos:
        print(filho.nome)
    jose.sobrenome = 'silva'
    del jose.filhos
    jose.olhos = 1
    print(jose.__dict__)
    print(luiz.__dict__)
    print(Pessoa.olhos)
    print(jose.olhos)
    print(luiz.olhos)
    print(id(Pessoa.olhos), id(jose.olhos), id(luiz.olhos))
    print(Pessoa.metodo_estatico(), jose.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), jose.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(luiz, Pessoa))
    print(isinstance(jose, Homem))
    print(luiz.olhos)
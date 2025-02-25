class Aluno:
    def __init__(self, nome, idade, matricula):
        self._nome = nome
        self._idade = idade
        self._matricula = matricula

    def mostrar_dados(self):
        print(f"Nome: {self._nome}, Idade: {self._idade}, Matrícula: {self._matricula}")

    def aniversario(self):
        self._idade += 1
        return self._idade

    def get_nome(self):
        return self._nome
    
    def set_nome(self, novo_nome):
        self._nome = novo_nome
        return self._nome
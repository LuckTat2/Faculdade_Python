class Departamento():
    def __init__(self, nome,):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\nFuncionários do departamento {self.nome}:")
        for funcionario in self.funcionarios:
            print(f"- {funcionario.nome} ({funcionario.cargo})")
    
class Funcionario():
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

def main():
    departamento1 = Departamento("TI")
    funcionario1 = Funcionario("Lucas", "Desenvolvedor")
    funcionario2 = Funcionario("Jorge", "Analista de Sistemas")

    departamento1.adicionar_funcionario(funcionario1)
    departamento1.adicionar_funcionario(funcionario2)

    departamento1.listar_funcionarios()

if __name__ == "__main__":
    main()
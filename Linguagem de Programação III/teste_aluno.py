from aluno import Aluno #Importação da classe

aluno1 = Aluno("Lucas",27,3312)
aluno2 = Aluno("Pedro",35,4432)

aluno1.mostrar_dados()
aluno2.mostrar_dados()

aluno1.aniversario()
aluno1.mostrar_dados()

print(aluno1.get_nome())

aluno1.set_nome("Jorge")
print(aluno1.get_nome())


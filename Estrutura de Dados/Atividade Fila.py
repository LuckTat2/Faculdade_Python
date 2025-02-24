fila_decolagem = []
fila_alternativa = []
ct_decolagem = []
ct_decolagem_alternativa= []




def listar_quantidade_decolagem(fila_decolagem):
   if len(fila_decolagem) == 0:
       print('\033[31mERRO: Fila vazia\033[m')
   else:
       print(len(fila_decolagem))
   return


def decolar_alternativa(fila_alternativa,ct_decolagem_alternativa):
   if len(fila_alternativa) == 0:
       print('\033[31mERRO: Fila vazia\033[m')
   else:
       while True:
           autorizar_alternativa = input("\033[33mAvião enviado para a Fila Alternativa, digite S para autorizar a decolagem: \033[m").lower()
           if autorizar_alternativa == "s":
               ct_decolagem_alternativa.append(fila_alternativa[0])
               fila_alternativa.pop(0)
               print("\033[32mAvião decolou da Fila Alternativa com sucesso!\033[m")
               break
           else:
               print("\033[31mDado inválido, digite S para autorizar o voo:\033[m")
      
def autorizar(fila_decolagem, fila_alternativa, ct_decolagem, ct_decolagem_alternativa):
   if len(fila_decolagem) == 0:
       print('\033[31mERRO: Fila vazia\033[m')
   else:
       autorizado = fila_decolagem[0]
       fila_decolagem.pop(0)
       while True:
           decolou = input("O avião decolou? [S/N]").lower()
           if decolou == "s":
               ct_decolagem.append(fila_decolagem[0])
               print("\033[32mAvião decolou da Fila de Decolagem com sucesso!\033[m")
               break
           elif decolou == "n":
               fila_alternativa.append(autorizado)
               decolar_alternativa(fila_alternativa, ct_decolagem_alternativa)
               break
           else:
               print('\033[31mDado inválido! Digite S ou N\033m[')
              
   return


def adicionar_decolar(fila_decolagem):
   nome = input("Digite o Prefixo Aeronáutico do avião que irá decolar:")
   fila_decolagem.append(nome)
   return


def listar_decolagem(fila_decolagem):
   if len(fila_decolagem) == 0:
       print('\033[31mERRO: Fila vazia\033[m')
   else:
       print(fila_decolagem)
   return


def listar_caracteristica(fila_decolagem):
   if len(fila_decolagem) == 0:
       print('\033[31mERRO: Fila vazia\033[m')
   else:
       primeiro_aviao = fila_decolagem[0]
       print(primeiro_aviao)
   return


def adicionar_alternativa(fila_decolagem , fila_alternativa):
   removido = fila_decolagem[0]
   fila_decolagem.pop(0)
   fila_alternativa.append(removido)
   return
def relatório(ct_decolagem, ct_decolagem_alternativa):
   print(f"Total de aviões que decolaram da pista principal: {len(ct_decolagem)}")
   print(f"Total de aviões que decolaram da pista alternativa: {len(ct_decolagem_alternativa)}")


def menu():
   while True:
       print("-"*30)
       print(f"\tEscolha sua opção:\n")
       print("1: \033[33mListar a quantidade de aviões na fila de decolagem\033[m")
       print("2: \033[33mAutorizar a decolagem do primeiro avião da fila de decolagem\033[m")
       print("3: \033[33mAdicionar um avião à fila de decolagem\033[m")
       print("4: \033[33mListar todos os aviões da fila de decolagem\033[m")
       print("5: \033[33mListar as características do primeiro avião da fila de decolagem\033[m")
       print("6: \033[33mEmitir relatório\033[m")
       print("7: \033[33mSair\033[m")


       opcao = input("Opção: ")
       print("-"*30)


       if opcao == "1":
           listar_quantidade_decolagem(fila_decolagem)
       elif opcao == "2":
           autorizar(fila_decolagem, fila_alternativa, ct_decolagem, ct_decolagem_alternativa)
       elif opcao == "3":
           adicionar_decolar(fila_decolagem)
       elif opcao == "4":
           listar_decolagem(fila_decolagem)
       elif opcao == "5":
           listar_caracteristica(fila_decolagem)
       elif opcao == "6":
           relatório(ct_decolagem, ct_decolagem_alternativa)
       elif opcao == "7":
           print("PROGRAMA ENCERRADO.")
           break
       else:
           print("\033[31mDado Inválido!\033[m")
   return




menu()

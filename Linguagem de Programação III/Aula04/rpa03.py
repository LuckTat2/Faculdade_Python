import pyautogui as p
import os
import time

class AutomacaoRPA:
    def abrir_notepad(self):
        """Abre um novo Bloco de Notas e espera carregar"""
        os.system("notepad")
        time.sleep(2)  # Tempo para garantir que o Notepad abra

    def escrever_texto(self, texto):
        """Garante que o Bloco de Notas esteja em foco e escreve um texto"""
        janela = p.getActiveWindow()  # Obtém a janela ativa (Notepad)
        if janela:
            janela.maximize()  # Maximiza para garantir o foco
            time.sleep(1)
            p.write(texto, interval=0.1)  # Escreve no Notepad
        else:
            print("Erro: Não foi possível identificar a janela do Notepad.")

# Criando um objeto e executando os métodos
rpa = AutomacaoRPA()
rpa.abrir_notepad()
rpa.escrever_texto("Meu robô está vivo com orientação a objetos!")
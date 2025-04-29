import pyautogui  # Importa o módulo pyautogui, que permite controlar o mouse e o teclado.
import time  # Importa o módulo time, que fornece funções de manipulação de tempo, como sleep por um tempo.
import subprocess  # Importa o módulo subprocess, usado para executar programas externos.

# Passo 1: Abrir o Bloco de Notas
subprocess.Popen(['notepad.exe'])  # Executa o programa 'notepad.exe', abrindo o Bloco de Notas.

# Passo 2: Esperar um pouco para garantir que o Bloco de Notas abriu
time.sleep(2)  # Pausa o código por 2 segundos para garantir que o Bloco de Notas tenha tempo de abrir.

# Passo 3: Digitar a mensagem
pyautogui.write('Meu robo está vivo e está fazendo análises de dados', interval=0.1)
# Usa o pyautogui para digitar a mensagem no Bloco de Notas. O parâmetro 'interval' define o tempo entre cada tecla pressionada.

# Passo 4: Aguardar 5 segundos para visualizar
time.sleep(5)  # Pausa o código por 5 segundos para dar tempo de visualizar o que foi digitado.

# Passo 5: Fechar o Bloco de Notas
pyautogui.hotkey('alt', 'f4')  # Simula pressionar as teclas 'Alt' + 'F4' para fechar o Bloco de Notas.

# Passo 6: Confirmar para não salvar, se necessário
time.sleep(1)  # Pausa por 1 segundo para aguardar o pop-up de confirmação.
pyautogui.press('right')  # Simula pressionar a tecla "esquerda" para selecionar a opção "Não salvar".
pyautogui.press('enter')  # Simula pressionar a tecla "Enter" para confirmar a escolha de não salvar.
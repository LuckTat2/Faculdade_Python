import pyautogui as p
import os
import pyperclip


# Função para abrir e escrever no Notepad
def abrir_notepad():
    os.system('start notepad')  # Abrir o Bloco de Notas
    p.sleep(2)  # Espera 2 segundos para garantir que o Bloco de Notas abra

    # Copiar a mensagem para a área de transferência
    pyperclip.copy('MEU ROBÔ ESTÁ VIVO!!!!')

    # Colar a mensagem no Notepad
    p.sleep(1)
    p.hotkey('ctrl', 'v')  # Atalho 'Ctrl + V' para colar a mensagem
    print('Mensagem escrita no Bloco de Notas!')


# Função para abrir e escrever no Word
def abrir_word():
    os.system('start winword')  # Abrir o Word
    p.sleep(3)  # Espera 3 segundos para garantir que o Word abra

    # Escrever uma mensagem no Word
    p.write('Mensagem escrita no Word!')
    print('Mensagem escrita no Word!')


# Função para abrir e escrever no Excel
def abrir_excel():
    os.system('start excel')  # Abrir o Excel
    p.sleep(3)  # Espera 3 segundos para garantir que o Excel abra

    # Escrever uma mensagem no Excel
    p.write('Mensagem escrita no Excel!')
    print('Mensagem escrita no Excel!')


# Opção do usuário para escolher qual programa abrir
option = p.confirm('Olá! Por favor, escolha o programa desejado:', buttons=['EXCEL', 'WORD', 'NOTEPAD'])

# Executar a função com base na escolha do usuário
if option == 'EXCEL':
    abrir_excel()  # Corrigido aqui
elif option == 'WORD':
    abrir_word()
elif option == 'NOTEPAD':
    abrir_notepad()
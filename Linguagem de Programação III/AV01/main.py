import pandas as pd
from datetime import datetime
import os
from reportlab.pdfgen import canvas
import qrcode
import smtplib
from email.message import EmailMessage
import pywhatkit as kit
import time

# 1) Caminhos absolutos
BASE_DIR = r'C:\RPA\AV01'
PLANILHA = os.path.join(BASE_DIR, 'clientes.xlsx')
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'logs.txt')
PASTA_QR = os.path.join(BASE_DIR, 'boletos')
PASTA_PDF = os.path.join(BASE_DIR, 'faturas')

# Função de log
def log(msg):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    linha = f'[{ts}] {msg}'
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(linha + '\n')
    print(linha)

# Geração de QR Code
def gerar_qrcode(pix_str, nome_arquivo):
    img = qrcode.make(pix_str)
    img.save(nome_arquivo)
    log(f"QR Code gerado: {nome_arquivo}")

# Geração da fatura PDF
def gerar_fatura(nome_cliente, valor, vencimento, nome_pdf, qr_code_img):
    c = canvas.Canvas(nome_pdf)
    c.setFont("Helvetica", 14)
    c.drawString(100, 750, f"Fatura para: {nome_cliente}")
    c.drawString(100, 720, f"Valor: R$ {valor}")
    c.drawString(100, 700, f"Vencimento: {vencimento}")
    c.drawImage(qr_code_img, 100, 500, width=100, height=100)
    c.save()
    log(f"Fatura gerada: {nome_pdf}")

# Envio de e-mail
def enviar_email(destinatario, assunto, corpo, anexo_path):
    try:
        msg = EmailMessage()
        msg['Subject'] = assunto
        msg['From'] = 'lucas.desouza@aluno.fmpsc.edu.br'
        msg['To'] = destinatario
        msg.set_content(corpo)

        with open(anexo_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(anexo_path)
            msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('lucas.desouza@aluno.fmpsc.edu.br', 'fwusehwwfbprrgou')
            smtp.send_message(msg)

        log(f"E-mail enviado para {destinatario}")
    except Exception as e:
        log(f"Erro ao enviar e-mail para {destinatario}: {e}")

# WhatsApp
def enviar_whatsapp(numero, mensagem):
    try:
        hora = datetime.now().hour
        minuto = datetime.now().minute + 1
        kit.sendwhatmsg(f"+55{numero}", mensagem, hora, minuto)
        time.sleep(15)
        log(f"WhatsApp enviado para {numero}")
    except Exception as e:
        log(f"Erro ao enviar WhatsApp para {numero}: {e}")

# 2) Leitura da planilha (apenas leitura)
clientes = pd.read_excel(PLANILHA, engine='openpyxl')

# 3) Processamento
for i, row in clientes.iterrows():
    nome = row['Nome']
    email = row['Email']
    telefone = str(int(row['Telefone']))
    valor = row['Valor']

    # Verifica se 'Vencimento' é uma string ou datetime
    if isinstance(row['Vencimento'], str):
        vencimento = pd.to_datetime(row['Vencimento'], errors='coerce')
    else:
        vencimento = row['Vencimento']

    if pd.isna(vencimento):
        vencimento = 'Data inválida'
    else:
        vencimento = vencimento.strftime('%Y-%m-%d')

    status = str(row['Status']).lower()

    log(f"Processando {nome} | Status: {status}")

    if status == 'pago':
        log(f"{nome} já está com status 'pago'. Pulando.")
        continue

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_base = f'{nome.replace(" ", "_")}_{timestamp}'

    nome_qr = os.path.join(PASTA_QR, f'qr_{nome_base}.png')
    nome_pdf = os.path.join(PASTA_PDF, f'fatura_{nome_base}.pdf')

    pix_str = f"pix://pagamento/{nome}/{valor}"
    gerar_qrcode(pix_str, nome_qr)
    gerar_fatura(nome, valor, vencimento, nome_pdf, nome_qr)

    enviar_whatsapp(telefone, f"Olá {nome}, sua fatura vence em {vencimento}. Valor: R$ {valor}.")
    enviar_email(email, "Fatura Pendente", f"Olá {nome}, segue em anexo sua fatura.", nome_pdf)

import os
import smtplib
from email.message import EmailMessage

# Configurar variáveis de ambiente para segurança (adicione essas variáveis no seu sistema)
EMAIL_ADDRESS = os.getenv('EMAIL_USER')  # Exemplo: "seuemail@gmail.com"
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')  # Senha de aplicativo do Gmail


def enviar_email(destinatario, assunto, mensagem):
    """ Envia um e-mail usando a conta configurada """
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = destinatario
    msg.set_content(mensagem)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"OK E-mail enviado com sucesso para {destinatario}")
    except Exception as e:
        print(f"X Erro ao enviar e-mail: {e}")


# Exemplo de uso:
enviar_email("cliente@email.com", "Chegou a encomenda #35",
             "Favor buscar a encomenda #35 que acabou de chegar.")

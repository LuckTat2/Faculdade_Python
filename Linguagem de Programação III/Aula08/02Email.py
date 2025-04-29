import os
import smtplib
from email.message import EmailMessage

# Defina aqui o seu e-mail e a senha do aplicativo do Gmail
EMAIL_ADDRESS = "seuemail@gmail.com"  # Substitua pelo seu e-mail
# Substitua pela senha do aplicativo gerada no Gmail
EMAIL_PASSWORD = "sua_senha_de_app"

# Criando a mensagem do e-mail
msg = EmailMessage()
msg["Subject"] = "Chegou #35 a encomenda"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "destinatario@email.com"  # Substitua pelo e-mail do destinatário
msg.set_content("Favor buscar a encomenda #35 que acabou de chegar.")

# Enviando o e-mail
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print("OK E-mail enviado com sucesso!")
except Exception as e:
    print(f"NO OK Erro ao enviar e-mail: {e}")

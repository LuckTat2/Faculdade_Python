import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Gerar o QR Code com a URL do pagamento
url_pagamento = 'https://exemplo.com/pagamento?codigo=123456'
qr = qrcode.make(url_pagamento)

# Salvar o QR Code como uma imagem
qr.save('qrcode_pagamento.png')

# Criar o PDF com os detalhes da compra
pdf_path = 'compra_com_qrcode.pdf'
c = canvas.Canvas(pdf_path, pagesize=letter)

# Adicionar título e detalhes da compra
c.setFont("Helvetica-Bold", 16)
c.drawString(100, 750, "Compra Realizada com Sucesso!")

# Adicionar informações sobre o produto e pagamento
c.setFont("Helvetica", 12)
c.drawString(100, 730, "Produto: Produto Exemplo")
c.drawString(100, 710, "Preço: R$ 100,00")
c.drawString(100, 690, "Forma de Pagamento: Boleto")

# Inserir o QR Code no PDF
c.drawImage('qrcode_pagamento.png', 100, 550, width=200, height=200)

# Salvar o PDF
c.save()

# Abrir o PDF gerado
os.startfile(pdf_path)
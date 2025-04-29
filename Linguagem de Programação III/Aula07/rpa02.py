from fpdf import FPDF
import datetime as dt

# Ler os dados da compra salvos na Parte 1
with open("compra.txt", "r") as f:
    detalhes_compra = f.read()

# Criar um PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='B', size=16)

# Título do PDF
pdf.cell(200, 10, "Detalhes da Compra", ln=True, align='C')
pdf.ln(10)

# Data da compra
data_compra = dt.datetime.now().strftime("%d/%m/%Y %H:%M")
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Data da compra: {data_compra}", ln=True)
pdf.ln(5)

# Detalhes da compra
pdf.multi_cell(0, 10, detalhes_compra)

# Salvar o PDF
pdf_name = "detalhes_compra.pdf"
pdf.output(pdf_name)

print(f"PDF gerado com sucesso: {pdf_name}")
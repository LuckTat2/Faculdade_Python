import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

arquivo = r'C:\RPA\AV01\clientes.xlsx'
dados = pd.read_excel(arquivo, engine='openpyxl')

driver = webdriver.Chrome()
driver.get("http://localhost/php/RPA_AV01/formulario.html")
time.sleep(2)

for _, row in dados.iterrows():
    nome = row['Nome']
    email = row['Email']
    telefone = str(row['Telefone'])
    valor = str(row['Valor'])

    if isinstance(row['Vencimento'], pd.Timestamp):
        vencimento = row['Vencimento'].strftime('%Y-%m-%d')
    else:
        vencimento = pd.to_datetime(row['Vencimento'], errors='coerce').strftime('%Y-%m-%d')

    status = 'pendente'
    if 'Status' in row and pd.notna(row['Status']):
        status = row['Status'].lower()

    driver.find_element(By.NAME, 'nome').send_keys(nome)
    time.sleep(random.uniform(1.0, 1.5))  # Aumentado o intervalo de tempo

    driver.find_element(By.NAME, 'email').send_keys(email)
    time.sleep(random.uniform(1.0, 1.5))  # Aumentado o intervalo de tempo

    driver.find_element(By.NAME, 'telefone').send_keys(telefone)
    time.sleep(random.uniform(1.0, 1.5))  # Aumentado o intervalo de tempo

    driver.find_element(By.NAME, 'valor').send_keys(valor)
    time.sleep(random.uniform(1.0, 1.5))  # Aumentado o intervalo de tempo

    campo_vencimento = driver.find_element(By.NAME, 'vencimento')
    driver.execute_script("arguments[0].value = arguments[1];", campo_vencimento, vencimento)
    time.sleep(random.uniform(1.0, 1.5))  # Aumentado o intervalo de tempo

    driver.find_element(By.NAME, 'status').send_keys(status)
    time.sleep(random.uniform(1.0, 1.5))  # Aumentado o intervalo de tempo

    driver.find_element(By.TAG_NAME, 'button').click()
    time.sleep(3)  # Aumentado o intervalo após o clique no botão

    driver.get("http://localhost/php/RPA_AV01/formulario.html")
    time.sleep(2)  # Aumentado o intervalo ao recarregar a página

driver.quit()

import rpa as r
import pyautogui as p
import time

r.init(visual_automation=True, chrome_browser=True)
r.url('https://br.investing.com/currencies/usd-brl')
time.sleep(5)  # Espera a página carregar completamente

# Verifica o conteúdo da página manualmente para confirmar o XPath
dolar = r.read('//*[@data-test="instrument-price-last"]')  # Esse XPath pode mudar, confirme no momento da execução
print(f'Dólar hoje: {dolar}')

r.close()

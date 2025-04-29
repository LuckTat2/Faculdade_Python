import rpa as r
import pyautogui as p

# Inicializa o navegador
r.init(visual_automation=True, chrome_browser=True)

# Acessa a página da loja
r.url('https://www.saucedemo.com/')
p.sleep(3)

# Insere login (usuário e senha de teste do site)
r.type('//*[@id="user-name"]', 'standard_user')  # Nome de usuário
r.type('//*[@id="password"]', 'secret_sauce[enter]')  # Senha
p.sleep(3)

# Adiciona um produto ao carrinho
r.click('//*[@id="add-to-cart-sauce-labs-backpack"]')
p.sleep(2)

# Acessa o carrinho
r.click('//*[@id="shopping_cart_container"]/a')
p.sleep(2)

# Avança para o checkout
r.click('//*[@id="checkout"]')
p.sleep(2)

# Preenche os dados de compra
r.type('//*[@id="first-name"]', 'Carlos')
r.type('//*[@id="last-name"]', 'Silva')
r.type('//*[@id="postal-code"]', '12345-678')
r.click('//*[@id="continue"]')
p.sleep(2)

# Finaliza a compra
r.click('//*[@id="finish"]')
p.sleep(2)

# Captura os detalhes da compra
detalhes_compra = r.read('//*[@id="checkout_complete_container"]')

# Salva os detalhes em um arquivo de texto para a próxima etapa
with open("compra.txt", "w") as f:
    f.write(detalhes_compra)

# Captura de tela
p.screenshot("compra_finalizada.png")

# Fecha o navegador
r.close()

print("Compra finalizada e dados salvos!")
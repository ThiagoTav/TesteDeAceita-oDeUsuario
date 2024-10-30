from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

@given('que estou na página de login')
def step_impl(context):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    context.driver = webdriver.Chrome(options=options)  # ou webdriver.Firefox()
    context.driver.get('https://www.saucedemo.com/')

@when('insiro "{usuario_exemplo}" e "{senha123}"')
def step_impl(context, usuario_exemplo, senha123):
    try:
        # Procurando o campo de nome de usuário
        print("Procurando o campo de nome de usuário...")
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, 'user-name')))
        print("Campo de nome de usuário encontrado. Inserindo o usuário:", usuario_exemplo)
        context.driver.find_element(By.ID, 'user-name').send_keys(usuario_exemplo)
        
        # Procurando o campo de senha
        print("Procurando o campo de senha...")
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
        print("Campo de senha encontrado. Inserindo a senha.")
        context.driver.find_element(By.ID, 'password').send_keys(senha123)
        
        # Procurando o botão de login
        print("Procurando o botão de login...")
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, 'login-button')))
        print("Botão de login encontrado. Clicando para fazer login...")
        context.driver.find_element(By.ID, 'login-button').click()

    except Exception as e:
        print("Erro durante a execução do passo de login:", str(e))
        raise

@then('devo ser redirecionado para o painel principal')
def step_impl(context):
    try:
        # Verifica se o URL contém o caminho "/inventory.html" (ou o que corresponder após o login)
        print("Verificando redirecionamento para o painel principal...")
        WebDriverWait(context.driver, 10).until(
            EC.url_contains('/inventory.html')
        )
        current_url = context.driver.current_url
        print("Redirecionamento bem-sucedido para:", current_url)
        assert '/inventory.html' in current_url, f"Redirecionamento incorreto: {current_url}"

    except Exception as e:
        print("Erro ao verificar o redirecionamento:", str(e))
        raise

    finally:
        # Fecha o navegador
        context.driver.quit()
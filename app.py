from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
#import json


def iniciar_driver():
    chrome_options = Options()

    parametros = ['--lang=pt-BR','--window-size=1920x1080','--incognito']

    for parametro in parametros:
        chrome_options.add_argument(parametro)

    chrome_options.add_experimental_option('prefs',{
        #altera o diretório de download
        'download.default_directory' : 'D:\\Projetos Selenium\\Downloads',
        #notifica o GC que o diretorio foi alterado
        'download.directory_upgrade' : True,
        #desabilita confirmação de download
        'download.prompt_for_download': False,
        #desabilita notificações
        'profile.default_content_setting_values.notifications' : 2,
        #permite downloads múltiplos
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    #inicializando o webdriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)

    return driver

driver = iniciar_driver()

#navegar
driver.get('https://www.olx.com.br/estado-rj/rio-de-janeiro-e-regiao?q=playstation%205&sp=2')

while True:
    sleep(5)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(2)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(2)
    driver.execute_script('window.scrollTo(0,document.body.scrollTop);')
    sleep(2)



    #Econtrar os títulos, os preços e os links
    titulos = driver.find_elements(By.XPATH,"//a[@class='olx-ad-card__title-link']//h2")
    precos = driver.find_elements(By.XPATH,"//h3[@data-ds-component='DS-Text']")
    links = driver.find_elements(By.XPATH,"//a[@class='olx-ad-card__title-link']")



    #guardar em um arquivo csv
    for titulo, preco, link in zip(titulos, precos,links):
        
        with open('preços.csv','a',encoding='utf-8',newline='') as arquivo:
            link_extraido = link.get_attribute('href')
            arquivo.write(f'{titulo.text};{preco.text};{link_extraido}{os.linesep}')
    try:
        botao_prox_pagina = driver.find_element(By.XPATH,'//span[text()="Próxima página"]')
        sleep(1)
        botao_prox_pagina.click()
    except:
        print('Chegamos na ultima página')
        break
    


#fazer isso para todas as páginas




input('')
# nome_prod1 = driver.find_element(By.ID,'ds-ad-card-title-3')
# preco1 = driver.find_element(By.XPATH,'//*[@id="main-content"]/div[4]/section/div[2]/div[1]/div[2]/h3')

# nome_prod2 = driver.find_element(By.ID,'ds-ad-card-title-4')
# preco2 = driver.find_element(By.XPATH,'//*[@id="main-content"]/div[5]/section/div[2]/div[1]/div[2]/h3')

# nome_prod3 = driver.find_element(By.ID,'ds-ad-card-title-5')
# preco3 = driver.find_element(By.XPATH,'//*[@id="main-content"]/div[6]/section/div[2]/div[1]/div[2]/h3')

# lista_produtos[nome_prod1.text] = preco1.text
# lista_produtos[nome_prod2.text] = preco2.text
# lista_produtos[nome_prod3.text] = preco3.text

# print(lista_produtos)

# with open('precos.txt','a',encoding='utf-8',newline='') as lista:
#     lista.write(json.dumps(lista_produtos))
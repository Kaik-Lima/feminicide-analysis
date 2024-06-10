from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
url = 'https://www.ssp.sp.gov.br/estatistica/violencia-contra-a-mulher'

# Configurando o navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Scraping
driver.get(url)
sleep(15)
# Todas classes btn
year = driver.find_elements(By.CLASS_NAME, 'btn')
# Ano 2023
year[20].click()
sleep(3)
# Meses do ano
months = driver.find_elements(By.CLASS_NAME, 'accordion-button')

# Criando DataFrame
df = pd.DataFrame()

cont = -1
typeCont = 1
for c in range(len(months)):
    months[c].click()
    sleep(1)
    typeCont += 4
    for i in range(18):
        typeCase = driver.find_elements(By.TAG_NAME, 'th')[typeCont].text
        typeCont += 1
        cont += 4
        cases = driver.find_elements(By.TAG_NAME, 'td')[cont].text
        # Adicionando dados no DataFrame
        new_row = pd.DataFrame({'Titulo': [typeCase], 'Quantidade': [cases]})
        df = pd.concat([df, new_row], ignore_index=True)
        sleep(0.3)
    cont -= 4

# Impressão
df.head()
# Exportando para planilha
df.to_csv('datas_feminicidio.csv')

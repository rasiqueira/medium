import Algorithmia
import wikipedia
from time import sleep
from selenium import webdriver


ask = input('Qual o assunto você quer publicar? (em inglês pq em portugues não tem quase nada): ')


try:
    text = wikipedia.summary(ask)
except:
    ask = input('escreva um termo válido em inglês: ')
    text = wikipedia.summary(ask)

input = {
  "action": "translate",
  "text": text,
  "target_language" : "pt-br"
}

client = Algorithmia.client('simtcMfVcIi2EcFstBQAJlyiiKe1')
algo = client.algo('translation/GoogleTranslate/0.1.1')
algo.set_options(timeout=300) # optional
response = algo.pipe(input).result['translation']
resposta = response.replace("&quot;", "")
print (resposta)

input = {
  "action": "translate",
  "text": ask,
  "target_language" : "pt-br"
}

client = Algorithmia.client('simtcMfVcIi2EcFstBQAJlyiiKe1')
algo = client.algo('translation/GoogleTranslate/0.1.1')
algo.set_options(timeout=300) # optional
pergunta = algo.pipe(input).result['translation']


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://medium.com/')

driver.find_element_by_link_text("Sign in").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Welcome back.'])[1]/following::button[1]").click()

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('rodrigoafons@hotmail.com')
senha = driver.find_element_by_xpath('//*[@id="pass"]')
senha.send_keys('rod@1220')
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

sleep(10)
driver.get('https://medium.com/new-story')
element = driver.find_element_by_xpath('//*[contains(@class, "title")]')
driver.execute_script("arguments[0].innerText = '{0}'".format(pergunta), element)
element = driver.find_element_by_xpath('//*[contains(@class, "trailing")]')
driver.execute_script("arguments[0].innerText = '{0}'".format(resposta), element)
sleep(3)
try:
    driver.find_element_by_xpath('//*[contains(@class, "button")]').click()
    sleep(3)
except:
    driver.find_element_by_xpath('//*[contains(@class, "button")]').click()
    sleep(3)

driver.find_element_by_xpath('//*[contains(@class, "button")]').click()
sleep(3)

driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[4]/div[1]/div/button').click()

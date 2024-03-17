import pyttsx3 
import re
import requests
from bs4 import BeautifulSoup

speaker = pyttsx3.init()
voices = speaker.getProperty('voices') 
speaker.setProperty('voice', voices[0].id) 
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate-25) 

def get_soup(url):
    url = url
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def urlf(pesquisa):
    buscaurl=f'https://pt.wikipedia.org/w/index.php?search={pesquisa}&title=Especial%3APesquisar&profile=advanced&fulltext=1&ns0=1'
    soup=get_soup(buscaurl)
    pesquisa=soup.find_all(class_="mw-search-results")[0]
    link=pesquisa.find('a').get('href')
    return f'https://pt.wikipedia.org{link}'


while True:
    try:
        pesquisa=input('digite sua busca: ').replace(' ','+')
        url=urlf(pesquisa)
        soup=get_soup(url)
        texto=soup.find_all(class_="mw-parser-output")
        break
    except:
        print('Não achei essa pesquisa tente dnv\n')
        continue

for i in range(len(texto)):
    for p in texto[i].find_all('p'):
        print(re.sub(r'\[.*?\]', '', p.text))
        speaker.say(re.sub(r'\[.*?\]', '', p.text)) 
        speaker.runAndWait()
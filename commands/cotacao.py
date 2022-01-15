import urllib.request as request
from bs4 import BeautifulSoup
import json

def cotacao(moeda):
    url = "https://economia.awesomeapi.com.br/json/last/{}".format(moeda)
    
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        data = json.loads(data)

        valor_cotacao = data['USDBRL']['high']
        valor_cotacao = valor_cotacao.replace('.', ',')

        valor = conversao_medidas(valor_cotacao[0:4])

        return valor

def conversao_medidas(valor):
    url = "https://conversor-de-medidas.com/mis/por-extenso/_{}_".format(valor)

    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        soup = BeautifulSoup(data, 'html.parser')

        valor_falado = soup.select(".destacado")[2].decode_contents()

        return valor_falado

import urllib.request as request
import json

def cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    #req = request.Request(url, method='GET')

    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        data = json.loads(data)

        valor_cotacao = data['USDBRL']['high']
        valor_cotacao = valor_cotacao.replace('.', 'i')

        #print(valor_cotacao[0:4])

        return valor_cotacao[0:4]

#cotacao()

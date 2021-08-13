import requests
from bs4 import BeautifulSoup


class Currency():
    def __init__(self):
        self.data = self.send_request('http://dovizgrafik.com/')

    def send_request(self, url):
        return requests.get(url)

    def get_currency(self):
        soup = BeautifulSoup(self.data.content,'html.parser')
        usd_tl = soup.find (id='USDTL').find(id='show').text
        euro_tl = soup.find (id='EURTL').find(id='show').text
        btc_usd = soup.find(id='BTCUSD').find(id='show').text
        xau_usd = soup.find(id='XAUUSD').find(id='show').text
        euro_usd = soup.find(id='EURUSD').find(id='show').text
        gram_altin_tl = soup.find(id='gram-altinTL').find(id='show').text

        response = '<b>Sezer özürlü</b>\n\n'
        response += '<b>Dolar</b>: '+usd_tl+' TL\n'
        response += '<b>Euro</b>: '+euro_tl+' TL\n'
        response += '<b>BTC</b>:  '+btc_usd+' TL\n'
        response += '<b>XAU</b>:  '+xau_usd+' TL\n'
        response += '<b>EUR/USD</b>: '+euro_usd+' TL\n'
        response += '<b>GRAM</b>: '+gram_altin_tl+' TL\n'
        print(response)
        return response


if __name__ == '__main__':
     Currency().get_currency()
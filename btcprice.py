import sched, time
import requests
from bs4 import BeautifulSoup
import csv

s = sched.scheduler(time.time, time.sleep)

def btc_price(sc):
    #Track the index
    source = requests.get('https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch')
    soup = BeautifulSoup(source.content, 'html.parser')
    index = soup.find_all("span", class_ = "Trsdu(0.3s)")[0].text
    print(index)

    #Print data to a csv file
    csv_file = open('btc_p.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([index])
    csv_file.close()

    s.enter(0.5,1, btc_price, (sc,))


s.enter(0.5, 1, btc_price, (s,))
s.run()

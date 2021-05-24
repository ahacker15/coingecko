# coding:UTF-8
import requests
import time
def get_exchange():
    list = []
    list2 = []
    url = "https://api.coingecko.com/api/v3/exchanges"
    http_data = requests.get(url=url).json()
    for data in http_data:
        a = data['name']
        list.append(a)
    for i in range(0, 40):
        list2.append(list[i])
        return list2

def try_exchange():
    while True:
        exchange_01 = get_exchange()
        time.sleep(300)
        exchange_02 = get_exchange()
        if exchange_02 !=exchange_01:
            b = [y for y in exchange_02 if y not in exchange_01]
            if b!=[]:
                server_api = "http://pushplus.hxtrip.com/send?token=xxx&title=排名发生了变化&content=%s&template=html" % b
                requests.get(url=server_api)
def main():
    try_exchange()
if __name__=='__main__':
    main()
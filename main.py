import requests # en çok kullanılan HTTP kütüphanesidir

response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
print(response) # <Response [200]>
'''
1xx bilgilendirici yanıtlar döner
2xx başarılı bir durumda döner
3xx başka bir yere yönlendirir
4xx istemci hataları
5xx sunucu hataları
'''

if response.status_code == 200:
    print(response.text) # gelen cevabu metin olarak yazar
    print(response.json()) #gelen cevabı jsan formatinda yazar json -> java script object notation

    for crypto in response.json():
        print(crypto["currency"]) # listede ki 2000 tane kriptonun isimlerini döndürdü currency -> para birimi

    for crypto in response.json():
        print(crypto["price"]) # listede ki 2000 tane kriptonun tutarını döndürdü

def getCryptoData():
    if response.status_code == 200:
        return response.json()

cryptoResponse = getCryptoData()
userInput = input("Kripto adınızı giriniz: ")
for crypto in cryptoResponse:
    if crypto["currency"] == userInput:
        print(crypto["price"])
        break
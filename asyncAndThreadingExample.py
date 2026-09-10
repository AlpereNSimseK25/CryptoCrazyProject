import threading
import requests
import time

def getDataSync(urls):
    startTime = time.time() # çalışmaya başladığı zamanı alır
    jsonArray = []
    for url in urls:
        jsonArray.append(requests.get(url).json())

    endTime = time.time() # çalışmayı bitirdiği zamanı alır
    elapsedTime = endTime - startTime
    print(f"Çalışma zamanı: {elapsedTime} saniye")

    return jsonArray

urls = ["https://postman-echo.com/delay/3"]*10 # bu sitede 3 saniye gecikme ile çalışır
#getDataSync(urls) Çalışma zamanı: 33.604796171188354 saniye
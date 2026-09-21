import threading
import requests
import time

from main import response


def getDataSync(urls):
    startTime = time.time() # çalışmaya başladığı zamanı alır
    jsonArray = []
    for url in urls:
        jsonArray.append(requests.get(url).json())

    endTime = time.time() # çalışmayı bitirdiği zamanı alır
    elapsedTime = endTime - startTime
    print(f"Çalışma zamanı: {elapsedTime} saniye")

    return jsonArray


class ThreadingDownloader(threading.Thread):

    jsonArray = []
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.jsonArray.append(response.json())
        return self.jsonArray

def getDataThreading(urls):
        startTime = time.time()
        threads = []
        for url in urls:
            thread = ThreadingDownloader(url)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
            print(thread)
        endTime = time.time()
        elapsedTime = endTime - startTime
        print(f"Çalışma zamanı: {elapsedTime} saniye")

urls = ["https://postman-echo.com/delay/3"]*10 # bu sitede 3 saniye gecikme ile çalışır
#getDataSync(urls) Çalışma zamanı: 33.604796171188354 saniye
#getDataThreading(urls) Çalışma zamanı: 3.717952013015747 saniye
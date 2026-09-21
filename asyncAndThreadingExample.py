import threading
import requests
import time
import asyncio
import aiohttp


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


async def getDataAsyncButAsWrapper(urls):
    startTime = time.time()
    jsonArray = []

    # async yapılan bir işlemin sonucu await olarak alınmalı
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as response:
                jsonArray.append(await response.json())

    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"Çalışma zamanı: {elapsedTime} saniye")

async def getData(session, url, jsonArray):
    async with session.get(url) as response:
        jsonArray.append(await response.json())

async def getDataAsyncConcurrently(urls):
    startTime = time.time()
    jsonArray = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for urls in urls:
            tasks.append(asyncio.ensure_future(getData(session, urls, jsonArray)))
        await asyncio.gather(*tasks) # for loop ile içine bilgileri vermek yerine -tasks kullandık

    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"Çalışma zamanı: {elapsedTime} saniye")
    return jsonArray

urls = ["https://postman-echo.com/delay/3"]*10 # bu sitede 3 saniye gecikme ile çalışır
#getDataSync(urls) Çalışma zamanı: 33.604796171188354 saniye
#getDataThreading(urls) Çalışma zamanı: 3.717952013015747 saniye
#asyncio.run(getDataAsyncButAsWrapper(urls)) Çalışma zamanı: 31.960915327072144 saniye
#asyncio.run(getDataAsyncConcurrently(urls)) Çalışma zamanı: 3.563718318939209 saniye
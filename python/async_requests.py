import asyncio
import aiohttp
import time

async def make_request(url):
    async with aiohttp.ClientSession() as session:
        await asyncio.sleep(10)  # Add a 10-second delay
        async with session.get(url) as response:
            return await response.text()

async def main():
    start_time = time.time()

    urls = ["http://www.google.com", "http://www.bing.com", "http://www.youtube.com"]

    tasks = [make_request(url) for url in urls]
    responses = await asyncio.gather(*tasks)

    for url, response in zip(urls, responses):
        print(f"Received response from {url} in {time.time() - start_time:.2f} seconds.")
    
    print("Total time taken with asyncio:", time.time() - start_time)

if __name__ == "__main__":
    asyncio.run(main())

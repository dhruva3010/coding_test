import time
import requests

def make_request(url):
    response = requests.get(url)
    return response.text

start_time = time.time()

urls = ["http://www.google.com", "http://www.bing.com", "http://www.youtube.com"]

for url in urls:
    response = make_request(url)
    print(f"Received response from {url} in {time.time() - start_time:.2f} seconds.")
    time.sleep(10)  # Sleep for 10 seconds

print("Total time taken without asyncio:", time.time() - start_time)

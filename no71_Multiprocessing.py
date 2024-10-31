import multiprocessing
import multiprocessing.process
import requests
def downloadFile(url, name):
    response = requests.get(url)
    open(f"no98_Image{name}.jpg","wb").write(response.content)

url = "https://picsum.photos/200/300"
pros = []
for i in range(1,6):
    # downloadFile(url,i)
    p = multiprocessing.Process(target=downloadFile, args=[url,i])
    p.start()
    pros.append(p)

for p in pros:
    p.join()
import requests
from bs4 import BeautifulSoup

# response = requests.get("https://www.google.com")
# print(response.text)

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "name" : "Tanmoy",
#     "id" : "CSE/21/023",
#     "sem": "7th sem"
# }
# headers = {"conten-type":"type of content"}
# response = requests.post(url, headers=headers, json=data)
# print(response.text)


url = "https://cloneweb.freewebhostmost.com/"
r = requests.get(url)
shup = BeautifulSoup(r.text, "html.parser")
print(shup.prettify())
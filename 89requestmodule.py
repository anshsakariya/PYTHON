import requests
url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":'Harry',
    "Body":'bhai',
    "userId":12,
}
header={
   'Content-type':'application/json;charset=UTF-8',
}
response=requests.post(url,headers=header,json=data)
print(response.text)



import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com/blogpost/djangocheatsheet/"
r=requests.get(url)
#print(text)
soup=BeautifulSoup(r.text,'html.parser')
for heading in soup.find_all("h2"):
    print(heading.text)
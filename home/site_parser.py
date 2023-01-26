import requests
from bs4 import BeautifulSoup
import urllib.request

def parse_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open("test1.txt", "w") as file:
        for link in soup.find_all("a"):
            data = link.get('href')
            if data != None and data.startswith('htt'):
                file.write(data) 
                file.write("\n")
                
def parse_images(url):  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    image_tags = soup.find_all('img')
    links = []
    for image_tag in image_tags:
        links.append(image_tag['src'])
    with open("test2.txt", "w") as file:
        for link in links:
            file.write(url+link) 
            file.write("\n")
    

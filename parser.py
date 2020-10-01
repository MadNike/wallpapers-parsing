import requests
from bs4 import BeautifulSoup as bs


url = 'https://wallpaperscraft.ru/all/1920x1080'
data = requests.get(url)
soup = bs(data.text, 'html.parser')
wallpapers_link = list(map(lambda tag: 'https://wallpaperscraft.ru' + tag['href'], soup.find_all('a', class_="wallpapers__link")))
for link in wallpapers_link:
    with open(f'./images/{link.split("/")[-2]}.jpg', 'wb') as img:
        link_soup = bs(requests.get(link).text, 'html.parser')
        download_link = link_soup.find('img', class_='wallpaper__image')['src']
        img.write(requests.get(download_link).content)

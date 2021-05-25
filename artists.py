import requests
from bs4 import BeautifulSoup as Bs


class Data:
    def __init__(self, rank, name, last_week, peak, weeks_on_list, url):
        self.rank = rank
        self.name = name
        self.last_week = last_week
        self.peak = peak
        self.weeks_on_list = weeks_on_list
        self.url = url


def charlist(url):
    page = requests.get(url)
    src = page.content
    content = Bs(src, 'lxml')
    li = content.find_all('li', class_='chart-list__element')
    data = []
    for element in li:
        rank = element.find('div', class_='chart-list-item__rank ').find('a').text
        name = element.find('div', class_='chart-list-item__title-text').text
        previous_ranks = element.find_all('div', class_='chart-list-item__ministats-cell')
        lw = previous_ranks[0].text
        peak = previous_ranks[1].text
        weeks_on_charts = previous_ranks[2].text
        img = element.find('img', class_='chart-list-item__image')
        image_link = img['src']
        data.append((Data(rank, name, lw, peak, weeks_on_charts, image_link)))
    return data

datas = charlist('https://www.billboard.com/charts/artist-100')

for i in datas:
    print(i.rank)
    print(i.title)
    print(i.artist)
    print(i.last_week)
    print(i.peak)
    print(i.weeks_on_list)
    print(i.url)
    print('------------')

import requests
from bs4 import BeautifulSoup as Bs


class Data:
    def __init__(self, rank, name, last_week, peak, weeks_on_list):
        self.rank = rank
        self.name = name
        self.last_week = last_week
        self.peak = peak
        self.weeks_on_list = weeks_on_list


def charlist(url):
    page = requests.get(url)
    src = page.content
    content = Bs(src, 'lxml')
    div = content.find_all('div', class_='chart-list')
    data = []
    for element in div:
        rank = element.find('div', class_='chart-list-item__rank').text.strip()
        name = element.find('span', class_='chart-list-item__title-text').text.strip()
        previous_ranks = element.find_all('div', class_='chart-list-item__ministats-cell')
        lw = previous_ranks[0].text.strip()
        peak = previous_ranks[1].text.strip()
        weeks_on_charts = previous_ranks[2].text.strip()
        print(rank)
        print(name)
        print(lw)
        print('---------------')
        data.append((Data(rank, name, lw, peak, weeks_on_charts)))
    return data


data = charlist('https://www.billboard.com/charts/artist-100')


# for i in data:
#     print(i.rank)
#     print('--------')
#     print(i.name)
#     print('--------')
#     print(i.last_week)
#     print('--------')
#     print(i.peak)
#     print('--------')
#     print(i.weeks_on_list)
#     print('--------')
#     print('--------')

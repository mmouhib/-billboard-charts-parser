import requests
from bs4 import BeautifulSoup as Bs


class Data:
    def __init__(self, rank, title, artist, last_week, peak, weeks_on_list, url):
        self.rank = rank
        self.title = title
        self.artist = artist
        self.last_week = last_week
        self.peak = peak
        self.weeks_on_list = weeks_on_list
        self.url = url


"""
    songs_url = 'https://www.billboard.com/charts/billboard-global-200'
    albums_url = 'https://www.billboard.com/charts/billboard-200'
    
    Replace the function parameter (url) by one of the upper
    
"""

def charlist(url):
    page = requests.get(url)
    src = page.content
    content = Bs(src, 'lxml')
    li = content.find_all('li', class_='chart-list__element')
    data = []
    for element in li:
        rank = element.find('span', class_='chart-element__rank__number').text
        song = element.find('span', class_='chart-element__information__song').text
        artist = element.find('span', class_='chart-element__information__artist').text
        previous_ranks = element.find_all('span', class_='chart-element__meta')
        lw = previous_ranks[0].text
        peak = previous_ranks[1].text
        weeks_on_charts = previous_ranks[2].text
        img = element.find('span', class_='chart-element__image')
        image = img['style']
        indx = image.find('(')
        image_link = image[indx + 2:-3]
        data.append((Data(rank, song, artist, lw, peak, weeks_on_charts, image_link)))
    return data

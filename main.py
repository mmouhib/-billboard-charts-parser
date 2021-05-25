import songsAndArtists
import json
# todo export results to JSON and Excel files
songs_url = 'https://www.billboard.com/charts/billboard-global-200'
albums_url = 'https://www.billboard.com/charts/billboard-200'
artists_url = 'https://www.billboard.com/charts/artist-100'

while 1:
    choice = input("""
    1) Top 200 Songs
    2) Top 200 Albums
    3) Top 100 Artists
    """)
    if choice.isdigit():
        if 0 < int(choice) < 4:
            break

data = songsAndArtists.charlist(artists_url)

for i in data:
    print(i.rank)
    print(i.title)
    print(i.artist)
    print(i.last_week)
    print(i.peak)
    print(i.weeks_on_list)
    print(i.url)
    print('------------')


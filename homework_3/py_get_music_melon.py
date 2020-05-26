import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
musics = soup.select('#lst50 > td')

# music (tr들) 의 반복문을 돌리기
for music in musics:
    number = music.select_one('div > span.rank')
    if number is not None:
            rank = number.text
#            print (rank)
    a_title = music.select_one('div > div > div.ellipsis.rank01 > span > a')
    if a_title is not None:
            title = a_title.text
#            print (title)
    a_artist = music.select_one('div > div > div.ellipsis.rank02 > a')
    if a_artist is not None:
            artist = a_artist.text
            print (rank, title, '-', artist)


#    print (rank[0:2])
#    a_title = music.select_one('div > div > div.ellipsis.rank02 > a')
#    title = a_title.text.strip()
#    print (title.text.strip())
#    a_artist = music.select_one('div > div > div.ellipsis.rank01 > span > a')
#    artist = a_artist.text.strip()
#    print (artist)

#    print (rank[0:2], title, '-', artist)

#lst50 > td:nth-child(2) > div > span.rank
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a


#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
# 해당 url의 html 코드를 soup에 저장
soup = BeautifulSoup(data.text, 'html.parser')

# select_one method
# 내가 필요한 항목의 selector를 select_one 메서드에 주면 해당 HTML 태그를 가져옴 (title = <a href="/movie/bi/mi/basic.naver?code=186114" title="밥정">밥정</a>)
# title에 넣은 객체의 type은 bs4.element.Tag
title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')

# select method
# 여러 항목을 선택하고 싶을 때 공통되는 selector 까지를 select 메서드에 주면 해당되는 태그들을 싹 모아서 가져옴
# 이때 가져온 객체의 type은 bs4.element.ResultSet 이며 list 형태이다.
movies = soup.select('#old_content > table > tbody > tr')
# 이후 list 각 원소들에 대해 원소.select_one 메서드로 하위 selector를 주면 된다.

# 가져오고 싶은 항목 : 순위, 제목, 별점
# 순위 selector : #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
# 제목 selector : #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# 별점 selector : #old_content > table > tbody > tr:nth-child(2) > td.point

for movie in movies:
    rank = movie.select_one('td:nth-child(1) > img')
    title = movie.select_one('td.title > div > a')
    point = movie.select_one('td.point')
    if rank:
        print(rank['alt'], title.text, point.text)



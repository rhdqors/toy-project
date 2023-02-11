import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@Cluster0.zhropba.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'http://book.interpark.com/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028',
    headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)
books = soup.select('#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li')
# print(books)
num = 0
for i in books:
    name = i.select_one('div > a > div.itemName > strong').text.strip()
    image = i.select_one('div > div.cover > div.coverImage > label > a > img')['src']
    writer = i.select_one('div > a > div.itemMeta > span.author').text
    publishing = i.select_one('div > a > div.itemMeta > span.company').text
    url = i.select_one('div > a')['href']
    num += 1
    # doc = {
    #     'num': num,
    #     'category': '도서',
    #     'name': name,
    #     'writer': writer,
    #     'publisher': publishing,
    #     'image': image,
    #     'url': url
    # }
    # db.books.insert_one(doc)
    # print(num, name, image, writer, publishing)
    # print(url)
# musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# for i in musics:
#     url = i.select_one('td:nth-child(3) > a')
#     print(url)
# doc = {
#         'num': num,
#         'category': '도서',
#         'name': '세이노',
#         'writer': writer,
#         'publisher': publishing,
#         'image': image,
#         'url': url
#     }
# db.books.insert_one(doc)
#인터파크 제목
#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li:nth-child(1) > div > a > div.itemName > strong
#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li:nth-child(2) > div > a > div.itemName > strong
#인터파크 이미지
#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li:nth-child(2) > div > div.cover > div.coverImage > label > a > img
#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li:nth-child(1) > div > div.cover > div.coverImage > label > a > img
#인터파크 저자
#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li:nth-child(1) > div > a > div.itemMeta > span.author
#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li:nth-child(2) > div > a > div.itemMeta > span.author
#인터파크 출판사
#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li:nth-child(1) > div > a > div.itemMeta > span.company
#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li:nth-child(2) > div > a > div.itemMeta > span.company
#인터파크 책 정보
#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li:nth-child(1) > div > a
#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li:nth-child(2) > div > a


#지니뮤직
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > a
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > a

#알라딘 제목
#Myform > div:nth-child(3) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(2) > a > b
#Myform > div:nth-child(4) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(2) > a.bo3 > b

#교보문고 제목
#tabRoot > div.view_type_list.switch_prod_wrap > ol:nth-child(1) > li:nth-child(1) > div.prod_area.horizontal > div.prod_info_box > a > span
#tabRoot > div.view_type_list.switch_prod_wrap > ol:nth-child(1) > li:nth-child(2) > div.prod_area.horizontal > div.prod_info_box > a > span

#예스24 제목
#category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)
#category_layout > tbody > tr:nth-child(3) > td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)
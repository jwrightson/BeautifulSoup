import bs4 as bs
import urllib.request
import pandas as pd
import openpyxl
import html5lib
import lxml
import re
import datetime


sauce_1 = urllib.request.urlopen('https://www.imdb.com/title/tt0141842/episodes?season=1').read()
sauce_2 = urllib.request.urlopen('https://www.imdb.com/title/tt0141842/episodes?season=2').read()
sauce_3 = urllib.request.urlopen('https://www.imdb.com/title/tt0141842/episodes?season=3').read()
sauce_4 = urllib.request.urlopen('https://www.imdb.com/title/tt0141842/episodes?season=4').read()
sauce_5 = urllib.request.urlopen('https://www.imdb.com/title/tt0141842/episodes?season=5').read()
sauce_6 = urllib.request.urlopen('https://www.imdb.com/title/tt0141842/episodes?season=6').read()

soup_1 = bs.BeautifulSoup(sauce_1, 'lxml')
soup_2 = bs.BeautifulSoup(sauce_2, 'lxml')
soup_3 = bs.BeautifulSoup(sauce_3, 'lxml')
soup_4 = bs.BeautifulSoup(sauce_4, 'lxml')
soup_5 = bs.BeautifulSoup(sauce_5, 'lxml')
soup_6 = bs.BeautifulSoup(sauce_6, 'lxml')

get_text_1 = str(soup_1.find_all('span', {"class" : "ipl-rating-star__rating"}))
get_text_2 = str(soup_2.find_all('span', {"class" : "ipl-rating-star__rating"}))
get_text_3 = str(soup_3.find_all('span', {"class" : "ipl-rating-star__rating"}))
get_text_4 = str(soup_4.find_all('span', {"class" : "ipl-rating-star__rating"}))
get_text_5 = str(soup_5.find_all('span', {"class" : "ipl-rating-star__rating"}))
get_text_6 = str(soup_6.find_all('span', {"class" : "ipl-rating-star__rating"}))

my_text_1 = (re.findall("\d+\.?\d*", get_text_1))
my_text_2 = (re.findall("\d+\.?\d*", get_text_2))
my_text_3 = (re.findall("\d+\.?\d*", get_text_3))
my_text_4 = (re.findall("\d+\.?\d*", get_text_4))
my_text_5 = (re.findall("\d+\.?\d*", get_text_5))
my_text_6 = (re.findall("\d+\.?\d*", get_text_6))

number_1 = 0
number_2 = 0
number_3 = 0
number_4 = 0
number_5 = 0
number_6 = 0


list1 = []

for text in my_text_1:
    number_1 += 1
    ##print(text)
    ##print(number)
    if ((number_1-25) % 12 == 0):
        list1.append(text)
for text in my_text_2:
    number_2 += 1
    ##print(text)
    ##print(number)
    if ((number_2-25) % 12 == 0):
        list1.append(text)
for text in my_text_3:
    number_3 += 1
    ##print(text)
    ##print(number)
    if ((number_3-25) % 12 == 0):
        list1.append(text)
for text in my_text_4:
    number_4 += 1
    ##print(text)
    ##print(number)
    if ((number_4-25) % 12 == 0):
        list1.append(text)
for text in my_text_5:
    number_5 += 1
    ##print(text)
    ##print(number)
    if ((number_5-25) % 12 == 0):
        list1.append(text)
for text in my_text_6:
    number_6 += 1
    ##print(text)
    ##print(number)
    if ((number_6-25) % 12 == 0):
        list1.append(text)




df = pd.DataFrame(list1)

df.to_excel('sopranos_ratings.xlsx')



   
    





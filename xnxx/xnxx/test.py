
from bs4 import BeautifulSoup
html='http://http://www.xnxx.com/video-j0mu338/chinese_/'
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
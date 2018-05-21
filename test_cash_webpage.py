from cash_webpage import *

webpage = WebPage("http://www.fest.lviv.ua/uk/projects/uku/")
# print(webpage.content)
f = open('cashed_page.html', 'w')
t = open('cashed_page_txt.txt', 'w')
f.write(str(webpage.content))
t.write(str(webpage.content))
f.close
t.close







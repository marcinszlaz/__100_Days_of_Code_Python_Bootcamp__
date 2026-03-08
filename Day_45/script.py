import html
from bs4 import BeautifulSoup
import lxml # another parser

with open(file='./website.html',mode='r')as f:
  contents = f.read()
  contents.title()
  soup = BeautifulSoup(contents,"lxml")


# print(soup.text.title())
# print(soup.text.title())
# print(soup.text)
# print(soup.a)
# function find_all and getText()

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#   print(tag.getText())
#
# heading = soup.find(name="h1",id="name")
# print(heading)
# section_heading = soup.find(name="h3",class_="heading")
# print(section_heading)
# print(section_heading.get("class"))
# print(section_heading.name)
# a_in_p_soup = soup.select("p a")
# print('nested a in p',a_in_p_soup)
#
# headings = soup.select(".heading")
# print(headings)

#1
ft = soup.find("form")
mx=ft.maxlength
print(mx)
#2
# ft=soup.select("input")
# mx=ft.attr("maxlength")
#3
# ft=soup.find_all("form")[0]
# mx=ft.attrs().maxlength
#4
ft = soup.find("input")
print(ft)
ml = ft.get("maxlength")
print(ml)
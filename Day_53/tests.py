import html
"""
# Znajdź pole (użyj bardzo ogólnego XPATHa, bo Google ma specyficzne nazwy)
login_input = wait.until(ec.presence_of_element_located((By.NAME, "identifier")))
# Wpisz login "siłą" przez JS
driver.execute_script("arguments[0].value = 'twoj_mail@gmail.com';", login_input)
# Poinformuj stronę, że coś się zmieniło (ważne!)
driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", login_input)
driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", login_input)
# Kliknij "Dalej" (często guzik ma nazwę id="identifierNext")
next_btn = driver.find_element(By.ID, "identifierNext")
driver.execute_script("arguments[0].click();", next_btn)

"""

print(chr(21328))
print(ord('卐'))
print(hex(ord('卐')))
print('\U00005350')
print('\u5350')
print('zwykla spacja',ord(' '),'(numer unicode)')
print('encja &nbsp; HTML',ord(html.unescape('&nbsp;')),'(numer unicode)')
_list_ = [1,2,3,4,5]
def print_or_not(list_,print_=False):
  if print_ == True:
    print(list_)

print_or_not(_list_,print_=False)

'''
dobry xpath, od razu wyszukuje atrybutu
$x('((//ul[contains(@class,"List-c")]/li[1]//a[@class="property-card-link"])[1])')[0].href

a ten wyszukuje liste atrybutów
$x('//a[@class="property-card-link"]').map(element => element.href)
map(element => element.href) to coś w stylu list składanych w Python

xpath_offert_url = '//ul[contains(@class,"List-c")]/li[1]//a[@class="property-card-link"]'

'''
slownik = ['Clicking and clicking','Stop clicking me !','maybe you will stop clicking xD', 'And he\'s again doing the same']
def click_me():
  my_label.config(text = f'{random.choice(slownik)}')
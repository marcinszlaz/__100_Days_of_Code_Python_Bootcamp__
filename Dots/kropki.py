import colorgram

def color_list():
  rgb_colors =[]
  colors = colorgram.extract('kropki.jpg', 24)

  '''
  sprawdz = (dir(colors[0]))
  for linia in sprawdz:
    if '_' not in linia:
      print(linia)
  '''

  for color_rgb in colors:
    r = color_rgb.rgb.r
    g = color_rgb.rgb.g
    b = color_rgb.rgb.b
    krotka = (r,g,b)
    rgb_colors.append(krotka)
  it = 1
  testowa_tablica = []
  for _ in range(len(rgb_colors)):
    ch1,ch2,ch3 = rgb_colors[_]
    if (ch1 and ch2 and ch3) < 230:
      testowa_tablica.append(rgb_colors[_])

  rgb_colors = testowa_tablica


    # print(_,':',rgb_colors[_])
    # for __ in range(len(rgb_colors[_])):
    #   print(it,':',rgb_colors[_][__])
    #   it += 1
    #   if rgb_colors[_][__] < 230:
    #
      # if __ < 230:
      #   testowa_tablica.append(rgb_colors[_])
      # else:
      #   print('nope')
  # print(len(rgb_colors))
  # print(rgb_colors)

  """
  selekcja = dir(zmienna)
  for _ in selekcja:
    if '_' not in _:
      print(_,end=',')
  
  # print(help(zmienna))
  """
  return rgb_colors
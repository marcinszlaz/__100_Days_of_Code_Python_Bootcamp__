import csv
#
# with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
#   csv_data = csv.reader(csv_file, delimiter=',')
#   list_of_rows = []
#   for row in csv_data:
#     list_of_rows.append(row)
#   print(list_of_rows)


m_d = {'cafe': 'Maczek', 'location': 'http://zupa.com', 'open': '9:00AM', 'close': '18:00PM', 'coffee': '☕️☕️', 'wifi': '💪💪', 'power': '🔌🔌', 'submit': True, 'csrf_token': 'IjVlMDUwODIxNmFjZGZmNzBiOTQzZDEyMzEyYzg4NTE0MTg3OTBkOGIi.afN_Nw.DUJPecLUW-vph565EkEiVsBEbwc'}

values_list = [v for k,v in m_d.items() if k not in ('submit','csrf_token')]

with open(file='cafe-data.csv',mode='a',encoding='utf-8',newline='') as file:
  csv.writer(file, delimiter=',',lineterminator='\r\n').writerow(values_list)

batch_size = 1000
data = [(f"Produkt {i}",i*10.0) for i in range(1,10001)]
# print('zawartość tablicy krotek',data)
# print('długość tablicy krotek',len(data))
# print('\n\n\n\n')
for i in range(0,len(data),batch_size):
  batch = data[i:i+1000]
  print(batch)
for i in range(0,10000,1000):
  print(data[i],data[i+999])

def multiplying(x,y):
  return x*y

print(multiplying(2,2))

lbd_multiplying = lambda x,y:x*y

print(lbd_multiplying(2,2))

sequence = lambda seq1,seq2: [x for x in seq1 if x in seq2]
print(*sequence([1,2,3],[2,5,6]))
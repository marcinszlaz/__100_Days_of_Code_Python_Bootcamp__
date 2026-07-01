import numpy as np
test_list = [1,2,3,4,5]

print('test_list: ',test_list)
print('test_list reversed: ',test_list[::-1])

maciorka = np.array([

  [[1,2,3],
  [4,5,6],
  [7,8,9]],
  [[1,2,3],
  [4,5,6],
  [7,8,9]],
  [[1,2,3],
  [4,5,6],
  [7,8,9]]

])


print('maciorka\n', maciorka)
print('.ndim', maciorka.ndim)
print('.shape', maciorka.shape)

reverted_maciorka = maciorka[:,::-1,:]
print('reverted maciorka: \n', reverted_maciorka)
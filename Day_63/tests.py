an_egzample_list_of_tuple = [(1,2,3),(4,5,6),(7,8,9)]
yyy =''
for tuple_ in an_egzample_list_of_tuple:
  print(f"{tuple_[0]} - {tuple_[1]} - {tuple_[2]}" )
  result_list_comp = " - ".join([str(t) for t in tuple_])
  result_map = " - ".join(map(str,tuple_))
  print(result_list_comp)
  print(result_map)
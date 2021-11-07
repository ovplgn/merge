lists=[1,2,4], [5,6,7], [0,2,100]
def merge(*lists):
  s= sum(lists, [])
  print(sorted(s))
merge(*lists)
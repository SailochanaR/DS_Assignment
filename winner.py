# Winner problem 
lst=list(map(str,input().split()))
size=len(lst)
def winner(lst):
  count=1
  i=0
  while not len(lst)==1:
    if i==len(lst):
      i=0
    if count==5:
      count=1
    if count<5 and i<len(lst):
      if count==4:
        lst.pop(i)
        count+=1
      else:
        i+=1
        count+=1
  return lst[0]
winner(lst)

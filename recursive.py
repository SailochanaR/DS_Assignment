def no_of_coins(sum,Ele,sol):
  if sum==0:
    return sol
  a=(sum//max(Ele))
  for i in range(a):
    sol.append(max(Ele))
  sum-=a*max(Ele)
  Ele.pop(max(Ele))
  return no_of_coins(sum,Ele,sol)
if __name__=='__main__':
    Ele=[int(x) for x in input().split()]
    sum=int(input('enter the sum'))
    sol=[]
    no_of_coins(sum,Ele,sol)

Ele=[]
size=int(input())
for i in range(size):
     Ele.append(int(input()))
count=0
i=0
for i in range(size+1):
    count+=1
    if(count%4==0 or count%10==4):
        print("the winner is:",Ele.pop(i))
    if(i==size):
      i=0
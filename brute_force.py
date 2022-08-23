#brute force
Ele=sorted([int(x) for x in input().split()])     # 1,2,5
sum=int(input('enter the sum'))                  # 15
sol=[]
count=1
i=0
total=sum
while sum>0:
    if not total >= sorted(Ele)[0]:
      print("Invalid")

      break
    if sum-Ele[i]>0:
        sol.append(Ele[i])
        sum=sum-Ele[i]
        print('sum is',sum)
        i+=1
        count+=1
        if count>len(Ele):
            i=0
            count=1
    elif sum-Ele[i]<0:
        i=0
        count=1
    else:
        sol.append(Ele[i])
        sum-=Ele[i]

    
print(sol)
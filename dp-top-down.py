ele = list(map(int,input("Enter coins -> ").split()))
tar = int(input("Enter target -> "))
size = len(ele)
sol=[]
coins=[]
count=0
while tar>0:
    i=0
    for i in range(size):
        if(tar>=ele[i]):
            sol.append(tar-ele[i])
    print(sol)
    tar1=min(sol)
    coins.append(tar-tar1)
    tar=tar1
    count+=1

    if tar<=0:
      print("No of coins required from array to make the target:",count) 
print("the coins which got used:",coins)
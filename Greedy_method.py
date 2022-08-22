def no_of_coins(V):
	Ele= []
	n = int(input())
	for i in range(n):
	    Ele.append(int(input()))
	print(Ele)
	res = []

	i = 1
	count=0
	while(i >= 0):
		
		while (V >= Ele[i]):
			V -= Ele[i]
			res.append(Ele[i])

		i -= 1
	for i in range(len(res)):
		print(  res[i], end = " ")
		count+=1
	print(count)

if __name__ == '__main__':
	n =int(input())
	print("Sum is", n, ": ", end = "")
	no_of_coins(n)
	
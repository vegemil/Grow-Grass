n = int(input())

for i in range(2*n):
	for j in range(n):
		if (i+j)%2 == 0:
			print("*", end="")
		else:
			print(" ", end="")
	print("")

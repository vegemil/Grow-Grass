arr = []
for _ in range(5):
	arr.append(max(int(input()), 40))
print(sum(arr)//5)

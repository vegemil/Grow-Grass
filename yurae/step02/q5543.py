arr1 = []
arr2 = []
for _ in range(3):
    arr1.append(int(input()))
	for _ in range(2):
	    arr2.append(int(input()))
		print(min(arr1) + min(arr2) - 50)

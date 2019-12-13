n = int(input())
arr = list(map(int, input().split()))
ave = 0
for el in arr:
	ave = ave + el/n
mx = max(arr)
ave = (ave/mx)*100
print(ave)

a = int(input())
b = int(input())
c = int(input())
n = a*b*c
cnt = [0 for _ in range(10)]
while(n > 0):
	cnt[n%10] = cnt[n%10] + 1
	n = n//10

for num in cnt:
	print(num)

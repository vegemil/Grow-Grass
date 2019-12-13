n = int(input())
curr = n
cnt = 0
while(True):
	val = curr%10 + curr//10
	curr = val%10 + (curr%10)*10
	cnt = cnt + 1
	if (curr == n):
		break

print(cnt)

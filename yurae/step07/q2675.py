n = int(input())
for _ in range(n):
	(k, line) = input().split()
	ans = ""
	for ch in line:
		ans = ans + ch * int(k)
	print(ans)

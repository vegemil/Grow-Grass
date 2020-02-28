n, m = map(int, input().split())

k = n-m

cnt_n = [0, 0]
cnt_k = [0, 0]
cnt_m = [0, 0]

curr = n
while (curr > 1):
	cnt_n[0] += curr//5
	curr //= 5
curr = n
while (curr > 1):
	cnt_n[1] += curr//2
	curr //= 2

curr = k
while (curr > 1):
	cnt_k[0] += curr//5
	curr //= 5
curr = k
while (curr > 1):
	cnt_k[1] += curr//2
	curr //= 2

curr = m
while (curr > 1):
	cnt_m[0] += curr//5
	curr //= 5
curr = m
while (curr > 1):
	cnt_m[1] += curr//2
	curr //= 2

print(min([cnt_n[0] - cnt_k[0] - cnt_m[0], cnt_n[1] - cnt_k[1] - cnt_m[1]]))

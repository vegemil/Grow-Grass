(h, m) = map(int, input().split())
if m < 45:
	h = h - 1
if h < 0:
	h = 23
m = (m+15)%60
print(h, m)

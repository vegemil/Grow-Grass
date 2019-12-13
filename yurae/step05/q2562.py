mx = -1
idx = -1
for i in range(1, 10):
	curr = int(input())
	if(curr > mx):
		mx = curr
		idx = i

print(mx)
print(idx)

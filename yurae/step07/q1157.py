line = input()
cnt = [0 for _ in range(26)]

for ch in line:
	idx = -1
	if(ord(ch) < ord('a')):
		idx = ord(ch) - ord('A')
	else:
		idx = ord(ch) - ord('a')
	cnt[idx] = cnt[idx] + 1

dup_max = False
max_idx = 0
for i in range(1, len(cnt)):
	if(cnt[i] > cnt[max_idx]):
		dup_max = False
		max_idx = i
	elif(cnt[i] == cnt[max_idx]):
		dup_max = True

if dup_max:
	print("?")
else:
	print(chr(65 + max_idx))

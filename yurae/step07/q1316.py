import sys

n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
	word = sys.stdin.readline().split()[0]
	arr = [False for _ in range(26)]

	has_dup = False
	idx = 0
	while (idx < len(word)):
		ch = word[idx]
		ch_idx = ord(ch) - ord('a')
		if (arr[ch_idx]):
			has_dup = True
			break
			
		arr[ch_idx] = True
		while (idx < len(word)):
			if (ch != word[idx]):
				break
			idx += 1
	

	if (has_dup == False):
		cnt += 1

print(cnt)

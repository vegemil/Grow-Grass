line = input()
cnt = [-1 for _ in range(26)]

for i in range(len(line)):
	ch = line[i]
	if (cnt[ord(ch)-ord('a')] < 0):
		cnt[ord(ch)-ord('a')] = i

for el in cnt[:-1]:
	print(el, end=" ")

print(cnt[-1])

import sys

word = sys.stdin.readline()
cnt = 0
idx = 0
while (idx < len(word)):
	if (idx == len(word)-1):
		break
	ch = word[idx]
	if (ch == 'c'):
		if (word[idx+1] == '=' or word[idx+1] == '-'):
			idx += 1
	elif (ch == 'd'):
		if (word[idx+1] == '-'):
			idx += 1
		elif ((idx < len(word)-3) and word[idx+1] == 'z' and word[idx+2] == '='):
			idx += 2
	elif (ch == 'l' or ch == 'n'):
		if (word[idx+1] == 'j'):
			idx += 1
	elif (ch == 's' or ch == 'z'):
		if (word[idx+1] == '='):
			idx += 1
	idx += 1
	cnt += 1

print(cnt)

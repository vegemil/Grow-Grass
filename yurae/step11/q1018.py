import sys

str1 = "WBWBWBWB"
str2 = "BWBWBWBW"

def cnt_diff(s1, s2):
	cnt = 0
	for i in range(len(s1)):
		if(s1[i] != s2[i]):
			cnt += 1
	return cnt


def calc1(line, idx):
	global str1, str2
	cnt = 0
	if (idx%2 == 0):
		cnt += cnt_diff(str1, line)
	else:
		cnt += cnt_diff(str2, line)
	return cnt


def calc2(line, idx):
	global str1, str2
	cnt = 0
	if (idx%2 == 0):
		cnt += cnt_diff(str2, line)
	else:
		cnt += cnt_diff(str1, line)
	return cnt


def main():
	n, m = map(int, sys.stdin.readline().split())
	chess = []
	for _ in range(n):
		chess.append(sys.stdin.readline().split()[0])

	res = 64
	for i in range(n-7):
		for j in range(m-7):
			cnt1 = 0
			cnt2 = 0
			for k in range(0, 8):
				line = chess[i+k][j:j+8]
				cnt1 += calc1(line, k)
				cnt2 += calc2(line, k)
			res = min([res, cnt1, cnt2])

	print(res)


main()

import sys

cnt1, cnt2 = 0, 0

def get_cnt(inp, n):
	global cnt1, cnt2
	if (len(inp) == 1):
		return 1 if (inp == "1") else 0

	k = n//2
	div1, div2, div3, div4 = "", "", "", ""
	for i in range(n):
		for j in range(n):
			if (i < k and j < k):
				div1 += inp[i*n + j]
			elif (i < k and j >= k):
				div2 += inp[i*n + j]
			elif (i >= k and j < k):
				div3 += inp[i*n + j]
			else:
				div4 += inp[i*n + j]

	chk = [get_cnt(div1, k), get_cnt(div2, k), get_cnt(div3, k), get_cnt(div4, k)]
	if (chk[0] == 1 and chk[1] == 1 and chk[2] == 1 and chk[3] == 1):
		return 1
	elif (chk[0] == 0 and chk[1] == 0 and chk[2] == 0 and chk[3] == 0):
		return 0
	else:
		for el in chk:
			if el == 1:
				cnt2 += 1
			elif el == 0:
				cnt1 += 1
		return -1
	


def main():
	n = int(sys.stdin.readline())
	inp = ""
	for _ in range(n):
		arr = sys.stdin.readline().split()
		for el in arr:
			inp += el

	get_cnt(inp, n)
	print(cnt1)
	print(cnt2)


if __name__ == "__main__":
	main()

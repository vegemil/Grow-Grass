import sys


def quad(inp, n):
	if (n == 1):
		return "0" if inp == "0" else "1"

	k = n//2
	div1, div2, div3, div4 = "", "", "", ""
	for i in range(n):
		for j in range(n):
			idx = i*n + j
			if (i < k and j < k):
				div1 += inp[idx]
			elif (i < k and j >= k):
				div2 += inp[idx]
			elif (i >= k and j < k):
				div3 += inp[idx]
			else:
				div4 += inp[idx]

	quads = [quad(div1, k), quad(div2, k), quad(div3, k), quad(div4, k)]
	if (quads[0] == "0" and quads[1] == "0" and quads[2] == "0" and quads[3] == "0"):
		return "0"
	elif (quads[0] == "1" and quads[1] == "1" and quads[2] == "1" and quads[3] == "1"):
		return "1"
	else:
		return "(" + quads[0] + quads[1] + quads[2] + quads[3] + ")"


def main():
	n = int(sys.stdin.readline())
	inp = ""
	for _ in range(n):
		inp += sys.stdin.readline().split()[0]
	print(quad(inp, n))


if __name__ == "__main__":
	main()

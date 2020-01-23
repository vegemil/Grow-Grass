import sys

def main():
	n = int(sys.stdin.readline())
	arr = []
	sumn = 0
	for _ in range(n):
		k = int(sys.stdin.readline())
		sumn += k
		arr.append(k)

	arr.sort()

	# cnt, val
	cnt = [[1, arr[0]]]
	for i in range(1, n):
		if (cnt[-1][1] == arr[i]):
			cnt[-1][0] += 1
		else:
			cnt.append([1, arr[i]])

	print(round(sumn/n))
	print(arr[(len(arr)//2)])

	cnt = sorted(cnt, reverse=True, key=lambda x: (x[0], -x[1]))
	if (len(cnt) > 1 and cnt[0][0] == cnt[1][0]):
		print(cnt[1][1])
	else:
		print(cnt[0][1])

	if (len(arr) > 1):
		print(arr[-1] - arr[0])
	else:
		print(0)

if __name__ == "__main__":
	main()

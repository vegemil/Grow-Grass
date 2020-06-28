import sys

def lower_bound(arr, start, end, piv):
	while (start < end):
		mid = (start+end)//2
		if (arr[mid] < piv):
			start = mid+1
		else:
			end = mid
	return end+1


def main():
	n = int(sys.stdin.readline())
	arr = list(map(int, sys.stdin.readline().split()))

	# length, prev, prev-idx
	chk = [[-1, -1] for _ in range(n)]
	chk[0] = [0, arr[0]]
	lis = [10000 for _ in range(n)]
	lis[0] = arr[0]
	idx = 0

	for i in range(0, n):
		if (lis[idx] < arr[i]):
			idx += 1
			lis[idx] = arr[i]
			chk[i] = [idx, arr[i]]
		else:
			nxt = lower_bound(lis, 0, idx, arr[i])
			lis[nxt-1] = arr[i]
			chk[i] = [nxt-1, arr[i]]

	res = []
	print(max(chk)[0]+1)
	for i in range(n-1, -1, -1):
		if (chk[i][0] == idx):
			idx -= 1
			res.append(chk[i][1])

	while(res):
		print(res.pop(), end=" ")
	print("")				


if __name__ == "__main__":
	main()

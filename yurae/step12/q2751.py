import sys


# re-implemented q2750
# works with Pypy3
def quicksort(arr, start, end):
	if (start >= end):
		return

	piv = (start+end)//2
	if (piv != start):
		arr[start], arr[piv] = arr[piv], arr[start]
		piv = start

	curr = start + 1
	while (curr <= end):
		if (arr[curr] < arr[piv]):
			arr[curr], arr[piv+1] = arr[piv+1], arr[curr]
			arr[piv], arr[piv+1] = arr[piv+1], arr[piv]
			piv += 1
		curr += 1

	quicksort(arr, start, piv-1)
	quicksort(arr, piv+1, end)


def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(int(sys.stdin.readline()))

	quicksort(arr, 0, len(arr)-1)

	for el in arr:
		print(el)

if __name__ == "__main__":
	sys.setrecursionlimit(100000)
	main()


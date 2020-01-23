import sys


# quicksort without sort()
def quicksort(arr, start, end):
	if (start >= end):
		return

	# select appropirate pivot
	piv1, piv2, piv3 = start, (start+end)//2, end
	piv = piv1
	if ((arr[piv1] <= arr[piv2] and arr[piv2] <= arr[piv3])
			or (arr[piv1] >= arr[piv2] and arr[piv2] >= arr[piv3])):
		piv = piv2
	elif ((arr[piv1] <= arr[piv3] and arr[piv3] <= arr[piv2])
			or (arr[piv1] >= arr[piv3] and arr[piv3] >= arr[piv2])):
		piv = piv3

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

import sys
from bisect import bisect_left

def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		el = int(sys.stdin.readline())
		arr.insert(bisect_left(arr, el), el)
		idx = len(arr)//2-1 if len(arr)%2 == 0 else len(arr)//2
		print(arr[idx])


if __name__ == "__main__":
	main()

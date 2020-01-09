import sys

def main():
	while (True):
		arr = list(map(int, sys.stdin.readline().split()))
		if (arr[0] == 0):
			return

		arr = sorted(arr)
		if (arr[0]*arr[0] + arr[1]*arr[1] == arr[2]*arr[2]):
			print("right")
		else:
			print("wrong")


main()

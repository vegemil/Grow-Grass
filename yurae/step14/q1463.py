from collections import deque

def main():
	n = int(input())
	arr = [-1 for _ in range(1000001)]
	arr[n] = 0

	deq = deque([])
	deq.append(n)
	while(arr[1] < 0):
		curr = deq.popleft()
		if (curr%3 == 0 and arr[curr//3] < 0):
			arr[curr//3] = arr[curr] + 1
			deq.append(curr//3)
		if (curr%2 == 0 and arr[curr//2] < 0):
			arr[curr//2] = arr[curr] + 1
			deq.append(curr//2)
		if (curr > 0 and arr[curr-1] < 0):
			arr[curr-1] = arr[curr] + 1
			deq.append(curr-1)

	print(arr[1])


if __name__ == "__main__":
	main()

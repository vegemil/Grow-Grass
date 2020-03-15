from collections import deque
import sys

def main():
	queue = deque([])
	for _ in range(int(sys.stdin.readline())):
		line = sys.stdin.readline().split()
		if (line[0] == "push"):
			queue.append(line[1])
		elif (line[0] == "pop"):
			res = -1 if not queue else queue.popleft()
			print(res)
		elif (line[0] == "size"):
			print(len(queue))
		elif (line[0] == "empty"):
			res = 1 if not queue else 0
			print(res)
		elif (line[0] == "front"):
			res = -1 if not queue else queue[0]
			print(res)
		elif (line[0] == "back"):
			res = -1 if not queue else queue[-1]
			print(res)


main()

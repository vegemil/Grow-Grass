import sys

def main():
	m = int(sys.stdin.readline())
	arr = []
	for _ in range(m):
		line = sys.stdin.readline().split()
		if (line[0] == "add"):
			el = int(line[1])
			if not el in arr:
				arr.append(el)
		elif (line[0] == "remove"):
			el = int(line[1])
			if el in arr:
				arr.remove(el)
		elif (line[0] == "check"):
			el = int(line[1])
			if el in arr:
				print(1)
			else:
				print(0)
		elif (line[0] == "toggle"):
			el = int(line[1])
			if el in arr:
				arr.remove(el)
			else:
				arr.append(el)
		elif (line[0] == "all"):
			arr = [i for i in range(1, 21)]
		elif (line[0] == "empty"):
			arr = []


if __name__ == "__main__":
	main()

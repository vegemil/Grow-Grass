import random

def main():
	n = int(input("input numbers of data : "))
	mx = int(input("input max value of numbers : "))
	dup = input("allow duplication? (y/n) : ")

	allow_dup = True
	if (dup == "y"):
		allow_dup = True
	elif (dup == "n"):
		allow_dup = False
	else:
		print("exit")
		return

	if allow_dup:
		f = open("data.txt", 'w')
		f.write(str(n) + "\n")

		for _ in range(n):
			line = str(random.randrange(1, mx+1)) + "\n"
			f.write(line)
		f.close()

	else:
		f = open("data.txt", 'w')
		f.write(str(n) + "\n")
	
		if (n > mx):
			print("max value should be greater than input numbers")
			return

		arr = [i for i in range(1, mx+1)]
		random.shuffle(arr)
		for el in arr[:n]:
			line = str(el) + "\n"
			f.write(line)
		f.close()

	print("generated data")


if __name__ == "__main__":
	main()

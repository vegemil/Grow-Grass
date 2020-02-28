import sys, math

def main():
	n = int(sys.stdin.readline())
	arr = list(map(int, sys.stdin.readline().split()))
	base = arr[0]
	for el in arr[1:]:
		gcd = math.gcd(base, el)
		lcm = (el * base)//gcd
		print("{0}/{1}".format(lcm//el, lcm//base))
		

if __name__ == "__main__":
	main()

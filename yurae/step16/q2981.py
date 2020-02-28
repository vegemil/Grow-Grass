import sys, math

def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(int(sys.stdin.readline()))
	arr = sorted(arr)
	gcd = arr[1]-arr[0]
	for i in range(2, len(arr)):
		gcd = math.gcd(gcd, arr[i]-arr[i-1])

	ans = []
	sqrt = int(math.sqrt(gcd))
	for m in range(2, sqrt+1):
		if (gcd % m == 0):
			ans.append(m)
			if (m != int(gcd/m)):
				ans.append(int(gcd/m))
	ans.append(gcd)

	ans = sorted(ans)
	for el in ans[:-1]:
		print(el, end=" ")
	print(ans[-1])

if __name__ == "__main__":
	main()

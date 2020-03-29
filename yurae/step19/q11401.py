div = 1000000007

# a^b ; divide & conquer
def power(a, b):
	global div
	res = 1
	while (b > 0):
		if (b%2 != 0):
			res *= a
		a *= a
		a %= div
		b //= 2
	return res%div


def main():
	n, k = map(int, input().split())
	global div

	if (n == k or k == 0):
		print(1)
		return
	
	fact = [1 for _ in range(4000001)]
	for i in range(2, 4000001):
		fact[i] = (fact[i-1]*i)%div

	res = (fact[n] * power(fact[n-k], div-2) * power(fact[k], div-2))%div
	print(res)


main()

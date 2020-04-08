import sys

n = int(sys.stdin.readline())
dic = {}
arr = list(map(int, sys.stdin.readline().split()))
for el in arr:
	dic[el] = True
m = int(sys.stdin.readline())
chk = list(map(int, sys.stdin.readline().split()))
for el in chk:
	print(1 if el in dic else 0)

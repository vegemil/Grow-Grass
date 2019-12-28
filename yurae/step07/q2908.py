[a, b] = input().split()
rev_a, rev_b = int(a[::-1]), int(b[::-1])
print(max([rev_a, rev_b]))

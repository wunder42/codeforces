n, k, l, r, sa, sk = map(int, raw_input().split())
i, j, a, b = sk/k, sk%k, 0, 0
if n - k:
	a, b = (sa-sk)/(n-k), (sa-sk)%(n-k)
r = []
map(r.extend, [[i+1]*j, [i]*(k - j), [a+1]*b, [a]*(n-k-b)])
print str(r)[1:-1].replace(',', '')
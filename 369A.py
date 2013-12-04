#! /usr/bin/python

n, a, b = map(int, raw_input().split())
s = map(int, raw_input().split())

for x in s:
	if x == 1: a -= 1
	else: b -= 1

if b < 0:
	b = -b
else:
	b = 0
if a < 0:
	b += -a
else:
	b -= a

print b if b > 0 else 0


# 
# o = lambda : map(int, raw_input().split())
# n, a, b = o()
# k = o().count(1)
# print max(0, k - a + max(0, n - k - b))
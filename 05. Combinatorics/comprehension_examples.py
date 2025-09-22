# [expression
#    for var1 in ...
#    for var2 in ...
#   ...
#   if condition1
#   if condition2
#   ...
# ]

# List comprehension
print([2 ** x for x in range(6)])

# List comprehension
print([c.upper() for c in 'Hello, World!' if c not in ' oe'])

# List comprehension
# Pythagorean Triples
from pprint import pprint
pprint([(a, b, c) for a in range(1, 100)
                  for b in range(1, 100)
                  for c in range(1, 100)
                  if a <= b <= c and a ** 2 + b ** 2 == c ** 2])

# Set comprehension
print({c.upper() for c in 'Hello, World!'})

# Dictionary comprehension
print({ i : i ** 2 for i in range(10)})

# Generator comprehension
g = (2 ** i for i in range(100_000_000))
print(next(g))
print(next(g))
print(next(g))
for i in g:
    print(i)
    if i % 4 == 0:
        break

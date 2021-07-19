import sys
import yaml
from itertools import zip_longest

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
print(list(zipped))
print(list(zip(range(5), range(100))))

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
operators = ['*', '/', '+']
print(list(zip(letters, numbers, operators)))
for l, n, o in zip(letters, numbers, operators):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(f'Operator: {o}')



numbers = []
letters = []
zipped = zip(numbers, letters)
x = list(zipped)
print (x)
#uncomment to see results:
#next(zipped)

numbers = [1, 2, 3]
letters = []
zipped = zip(numbers)
x = list(zipped)
print (x)

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
x = list(zipped)
print (x)
print(type(zipped))
x = dict(zipped)
print (x)


a = dict(zip("key", "val"))
s = yaml.safe_dump(a, sort_keys=False)
b = yaml.safe_load(s)
print(a.keys())
print(list(a.keys()))
assert list(a.keys()) == list(b.keys())
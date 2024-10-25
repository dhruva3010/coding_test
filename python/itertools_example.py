from itertools import count, cycle, repeat, chain, product, combinations, permutations, islice, filterfalse

for i in count(1, 2):
    if i > 20:
        break
    print(i)

colors = cycle(['red', 'green', 'blue'])
for _ in range(5):
    print(next(colors))

for i in repeat('Hello', 3):
    print(i)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = chain(list1, list2)
print(list(combined))

cards = ['A', '2', '3']
suits = ['Hearts', 'Diamonds']
deck = list(product(cards, suits))
print(deck)

colors = ['red', 'green', 'blue']
combs = list(combinations(colors, 2))
print(combs)

digits = [1, 2, 3]
perms = list(permutations(digits, 3))
print(perms)

numbers = range(10)
selected = islice(numbers, 1, 9, 2)
print(list(selected))

numbers = range(10)
evens = filterfalse(lambda x: x % 2 != 0, numbers)
print(list(evens))
    
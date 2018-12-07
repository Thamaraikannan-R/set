engineers = set(['John', 'Jane', 'Jack', 'Janice'])
programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])

print(engineers.union(programmers))        # new set with elements from both s and t
print(engineers.intersection(programmers)) # new set with elements common to s and t
print(engineers.issubset(programmers))  # test whether every element in s is in t
print(engineers.difference(programmers)) # new set with elements in s but not in t
print(engineers.symmetric_difference(programmers)) # new set with elements in either s or t but not both
value = programmers.copy()
print(value)
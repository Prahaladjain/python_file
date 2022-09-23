"""
s=set()
print(type(s))

# l=[2,8,9,476,6]
# print(set(l))

# print(set([2,8,9,476,6]))

s.add(1)
s.add(2)

s.union({1,2,3})
print(s)

s1=s.union({1,2,3})
print(s,s1)

s1=s.intersection({1,2,3})
print(s,s1)

s.remove(2)
print(s)

s1={4,6}
print(s.isdisjoint(s1))
"""












# Sets -> Mutable  unique Heterogenous-> only string, number and tuples are stored   unOrdered-> cannot access through index 
# It is a empty dictionary 
# s={} 

# s={1,2,3,4,5,8,"Hello ",5}
# print(type(s))
# print(s)

# Will give random values 
# for i in s:
#     print(i)
# Index access is not allowed 
# print(s[0])



# Set Methods 
s={1,2,3}
s.add(4)
print(s)
# Remove will throw error if element not present in set 
s.remove(1)
print(s)
#  This will not throw any error
s.discard(1)

# Will remove random elememnt
s.pop()
print(s)

# Will remove all elements 
s.clear()
print(s)


# Set Operations 
a={1,2,3}
b={3,4,5,6}

s=a.union(b)
print(s)
i=a.intersection(b)
print(i)

# elements which is in a but not in b 
d=a.difference(b)
print(d)
# elements which is both in a and b and not common 
sd=a.symmetric_difference(b)
print(sd)
# Type COnversion used to convert data types from one to another 
# Explicit Conversion -> Using Function to explicitly converting from one type to another

a=12
print(type(a))

# 1. str()
a=str(a)
print(a)
print(type(a))

# 2. int()
a=int(a)
print(a)
print(type(a))

# 3.float()
a=float(a)
print(a)
print(type(a))

# 4. bool()
a=bool(a)
print(a)
print(type(a))


# Python  have 7 falsy values 
# "" Empty String 
# ,[]-> Empty List 
# ,{}->Empty Dictionary or set 
# ,0,None,0.0,
# ()->Empty tuple
b=[]

print(bool(b))


# Implicit Conversion -> Python Language doing conversion on its own

print(type(12/3))

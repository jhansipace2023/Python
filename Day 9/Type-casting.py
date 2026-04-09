# IMPLICIT TYPE CASTING

a = 5
b = 4
c = a + b
print(type(c))   # <class 'int'>

a = 98.45
b = 10
c = a * b
print(type(c))   # <class 'float'>


# INTEGER DATATYPE CONVERSION

a = 98
print(float(a))      # 98.0
print(complex(a))    # (98+0j)
print(bool(a))       # True
print(str(a))        # '98'

print(list(a))       # TypeError
print(tuple(a))      # TypeError
print(set(a))        # TypeError
print(dict(a))       # TypeError


# FLOAT DATATYPE CONVERSION

a = 98.56
print(int(a))        # 98
print(complex(a))    # (98.56+0j)
print(bool(a))       # True
print(str(a))        # '98.56'

print(list(a))       # TypeError
print(tuple(a))      # TypeError
print(set(a))        # TypeError
print(dict(a))       # TypeError


# COMPLEX DATATYPE CONVERSION

a = 10+5j
print(bool(a))       # True
print(str(a))        # (10+5j)

print(int(a))        # TypeError
print(float(a))      # TypeError
print(list(a))       # TypeError
print(tuple(a))      # TypeError
print(set(a))        # TypeError
print(dict(a))       # TypeError


# BOOLEAN DATATYPE CONVERSION

a = True
print(int(a))        # 1
print(float(a))      # 1.0
print(complex(a))    # (1+0j)
print(str(a))        # True

print(list(a))       # TypeError
print(tuple(a))      # TypeError
print(set(a))        # TypeError
print(dict(a))       # TypeError


# STRING DATATYPE CONVERSION

s1 = "python"
print(list(s1))
print(tuple(s1))
print(set(s1))
print(bool(s1))

s1 = "education"
print(int(s1))       # ValueError
print(float(s1))     # ValueError
print(complex(s1))   # ValueError
print(dict(s1))      # ValueError


# LIST TYPE CASTING

li = [10,20,30,40,98]
print(str(li))
print(tuple(li))
print(set(li))
print(bool(li))

li = [10,20,30,40,98]
print(int(li))       # TypeError
print(float(li))     # TypeError
print(complex(li))   # TypeError
print(dict(li))      # TypeError


# TUPLE DATATYPE CONVERSION

t1 = (10,20,30,40)
print(str(t1))
print(list(t1))
print(set(t1))
print(bool(t1))

print(int(t1))       # TypeError
print(float(t1))     # TypeError
print(complex(t1))   # TypeError
print(dict(t1))      # TypeError

# SET DATATYPE TYPE CASTING

s1 = {98,45,30,89,17}
print(str(s1))
print(list(s1))
print(tuple(s1))
print(bool(s1))

s1 = {98,45,30,89,17}
print(int(s1))       # TypeError
print(float(s1))     # TypeError
print(complex(s1))   # TypeError
print(dict(s1))      # TypeError


# DICTIONARY DATATYPE TYPE CASTING

d1 = {'ename':'smith','salary':98000}
print(str(d1))
print(list(d1))
print(tuple(d1))
print(bool(d1))

d1 = {'ename':'smith','salary':98000}
print(int(d1))       # TypeError
print(float(d1))     # TypeError
print(complex(d1))   # TypeError
obj = 1
print(type(obj))
print(isinstance(obj,str))
print(2e9)
string = 'hello \n'
space = '\n'
string1 = 'world \r'
print(string +space+ string1)
prac = 'abcd'r'abc\n'
prac1 = 'abcd'r'abc'

print(type(prac))
print(prac)
print(len(prac))
print(len(prac1))
print("%s can speak %d languages"%("CC",600))
print("%s can speak %d languages")

x = '   foo   '
y = x
print(x == y)
print(x is y)
x = x.strip()
print(x)
print(y)
print(x == y)
print(x is y)

z= [1,2,3,4]
w = z
print(w)
z.append(5)
print(z)
print(w)

tu = (23,'abc',4.36,(2,3))
print(type(tu[0]))
print(type(tu[3]))
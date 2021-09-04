lst1 = [('a',1),('b',2),('c','hi')]
lst2 = ['x','a',6]

d = {k:v for k,v in lst1}
s = {x for x in lst2}

print(d)
print(s)

def f(n):
    yield n
    yield n+1
    yield n*n

print([i for i in f(3)])
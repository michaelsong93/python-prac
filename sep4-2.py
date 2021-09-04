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

def merge(l,r):
    llen = len(l)
    rlen = len(r)
    i = 0
    j = 0
    while i < llen or j < rlen:
        if j == rlen or (i < llen and l[i] < r[j]):
            yield l[i]
            i += 1
        else:
            yield r[j]
            j += 1
# g = merge([1,3,5],[2,4,6])
# while True:
#     print(g.__next__())
# print(merge([1,3,5],[2,4,6]))
print([x for x in merge([1,2,5],[3,4,6])])
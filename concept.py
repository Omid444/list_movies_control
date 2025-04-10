y =  {x: x ** 2 for x in range(10)}
print(y)

z = dict([('foo', 100), ('bar', 200)]), dict(foo=100, bar=200)
print(z)

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

print(c)

f = dict({'one': 1, 'three': 3}, two=2)
print(list(f))

iter(f.keys())

print(type(f.keys()))

print(type(range(1,10)))
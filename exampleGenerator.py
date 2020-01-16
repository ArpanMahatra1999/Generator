def ex():
    n = 3
    yield n

    n = n**2
    yield n

v = ex()
print(next(v))
print(next(v))
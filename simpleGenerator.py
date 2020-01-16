def func():
    for i in range(1,3):
        yield i

print(next(func()))
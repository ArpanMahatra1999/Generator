def new(dict):
    for x,y in dict.items():
        yield x,y

a = {1:'Hi',2:'Hello'}
b = new(a)

print(b)
print(next(b))
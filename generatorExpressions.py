a = range(6)

print("Generator Expressions. \r")
c = [x+2 for x in a]
print(c)
print(min(c))

d = (x+2 for x in a)
print(d)
#print(min(d))
for x in d:
    print(x)


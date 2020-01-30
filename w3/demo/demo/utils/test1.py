def f1(a, b=None):
    if b is None:
        b = []
    b.append(a)
    return b


a1 = f1(2)
print(a1)

print('-'*40)

a1 = f1(3)
print(a1)
print('-'*40)


a2 = f1(4)
print(a2)



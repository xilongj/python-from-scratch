# gen = (i*i for i in range(1,11))
# for i in range(1,11):
#     # print(gen.__next__())
#     print(next(gen))


def add(s, x):
    return s + x

def gen():
    for i in range(4):
        yield i

base = gen()

for n in [1, 10]:
    base = (add(i, n) for i in base)

print(list(base))
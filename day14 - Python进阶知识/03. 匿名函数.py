# 匿名函数
def foo(x, y):
    return x + y

ret = foo(2, 3)
print(ret)

# 使用方式一
bar = lambda x, y: x + y
print(bar(4,5))

# 使用方式二
# (lambda x, y: x + y)(3, 1)
print((lambda x, y: x + y)(3, 1))

# 使用方式三
# 配合高阶函数函数, 实现函数式编程

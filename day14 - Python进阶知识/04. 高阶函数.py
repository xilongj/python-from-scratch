# 常用高阶函数 filter, map, reduce
# filter
# lst_a = [1, 2, 3, 4, 5, 6, 7, 8]
# def filterEven(item):
#     if item % 2 == 0:
#         return True
#     else:
#         return False
#
# print(list(filter(filterEven, lst_a)))
# print(list(filter(lambda item:item%2 ==0, lst_a)))

# name_list = ['xilongj', 'satyan', 'markz', 'admin']
# def filterName():
#     for uname in name_list:
#         if len(uname) < 7:
#             print(uname)
# filterName()

name_list = ['xilongj', 'satyan', 'markz', 'admin']
def filterName(uname):
    if len(uname) < 7:
        return True
    else:
        return False

print(list(filter(filterName, name_list)))
# =======================================================



# map
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# def bar(item):
#     return item*item
# def nMap(func, lst):
#     res = []
#     for item in lst:
#         res.append(func(item))
#     return res
#
# print(nMap(bar, lst))


# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# def nMap(func, lst):
#     res = []
#     for item in lst:
#         res.append(func(item))
#     return res
# print(nMap(lambda x:x*x, lst))


def bar(item):
    return item * item

lst_b = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(bar, lst_b)))

# print(list(map(lambda item: item*item, lst_b)))



# =======================================================

# 计算1至100和
# num_of_Sum = 0
# for i in range(1,101):
#     num_of_Sum +=i
# print(num_of_Sum)

# print(sum([i for i in range(1,101)]))

# from functools import reduce
# def func(x, y):
#     return x * y
# print(reduce(func, range(1,11)))
print(reduce(lambda x,y:x*y, range(1,11)))






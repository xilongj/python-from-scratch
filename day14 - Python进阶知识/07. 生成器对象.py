# 普通案例
# def getNum5():
#     lst = []
#     for item in range(1,6):
#         lst.append(item)
#     return lst
#
# print(getNum5())

# 生成器案例
# def getNum():
#     print('running')
#     count = 0
#     while count < 5:
#         count += 1
#         yield count
#
# print(getNum)  # <function getNum at 0x000001ED6A0F8310>
# print(getNum())  # <generator object getNum at 0x000001ED6A666B30>
# Gen = getNum()
# print(Gen.__next__())  # 1
# print(Gen.__next__())  # 2
# print(Gen.__next__())
# print(Gen.__next__())
# print(Gen.__next__())
# print(Gen.__next__())

# 去重
lst = ['xilongj', 'satya', 'markz', 'admin', 'xilongj', 'satyan']
print(list(set(lst)))


# {'name': 'xilongj', 'age': 28, 'gender': 'male'}
dic_info = dict([('name', 'xilongj'), ('age', 28), ('gender', 'male')])
print(dic_info)


# sorted
lst = [2, 4, 3, 23, 45, 82]
lst.sort(reverse=True)
print(lst)

print(sorted([2, 4, 3, 23, 45, 82], reverse=True))


# 按照年龄排序
list_info = [('satya', 35), ('markz', 28), ('xilongj', 26)]
list_info = sorted(list_info, key=lambda item:item[1], reverse=True)
print(list_info)

list_age = [{'age':35}, {'age':28}, {'age':18}]
list_age = sorted(list_age, key=lambda item:item['age'], reverse=False)
print(list_age)

# zip函数
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list(zip(list_a, list_b)))

# 考题 zip+dict
# {'satyan': 28, 'xilongj': 37, 'markz': 16}
names = ['satyan', 'xilongj', 'markz']
ages = [28, 37, 16]

dict_info = zip(names, ages)
print(dict(dict_info))
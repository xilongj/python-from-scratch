# 将字典中键值对调
dic = {'uname':'admin','passwd':'xlnx@2021','job':'IT'}
new_dic = {}
for k,v in dic.items():
    new_dic[v] = k
print(new_dic)

# 字典生成式
dic = {'uname':'admin','passwd':'xlnx@2021','job':'IT'}
new_dic = {v:k for k,v in dic.items()}
print(new_dic)
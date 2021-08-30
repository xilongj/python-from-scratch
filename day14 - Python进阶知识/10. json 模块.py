import json

# 序列化方法: 将本语言支持数据类型转换成一个固定字符串格式

stocks = [
    {'name':'中信证券', 'code':'600030', 'price':'24.73'},
    {'name':'格力电器', 'code':'000651', 'price':'41.27'},
    {'name':'双汇发展', 'code':'000895', 'price':'24.16'},
    {'name':'元组股份', 'code':'603886', 'price':'18.07'},
    {'name':'中国银行', 'code':'601988', 'price':'3.00'},
]

stocks_json = json.dumps(stocks, ensure_ascii=False)
print(type(stocks_json), stocks_json)

print(repr(stocks_json))

stocks_data = json.loads(stocks_json)
print(type(stocks_data), stocks_data)
msg = [
    {"title": "西游记", "price": 100},
    {"title": "红楼梦", "price": 200},
    {"title": "三国传", "price": 300},
    {"title": "水浒转", "price": 400},
]

import json

msg_str = json.dumps(msg, ensure_ascii=False)
print(repr(msg_str))

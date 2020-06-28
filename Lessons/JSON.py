import json

d = {'dic': 'Misha', 'dict': 'Tima'}
s = json.dumps(d)
print(type(s))
print(s)
# with open('test.txt', 'w') as file:
#     json.dump(d, file)

m = json.loads(s)

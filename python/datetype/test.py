i = float("123.4")
print(bool(i))
a = 33

lis1 = [0, 34, 23, 1, 2, 3]
len_lis1 = len(lis1)
print(max(lis1))  # 34
print(min(lis1))  # 0
dic = {'name': 'python', 'likes': 123, 'url': 'www.python.org'}
for key in dic:
    print(key, dic[key])
c = 1 + 5j
print(c, type(c))  # (1+5j) <class 'complex'>

a = 5
if a > 4:
    print("a > 0")
elif 0 < a < 4:
    print("0 < a < 4")
else:
    print("a < 0")
a = "hello world,hello python!"
if "hello" in a:
    print("a contains hello")

x_arr = list()
y_arr = list()
for i in range(3) :
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

x_set = set(x_arr)
y_set = set(y_arr)
while x_set :
    x = x_set.pop()
    if x_arr.count(x) == 1 :
        break

while y_set :
    y = y_set.pop()
    if y_arr.count(y) == 1 :
        break
    
print(x, y)
    
    
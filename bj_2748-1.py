n = int(input())

list = []
list.append(0)
list.append(1)

def function(a):
    temp = len(list)
    if a == temp:
        return list[a-1] + list[a-2]
    else:
        list.append(list[temp-1] + list[temp-2])
        return function(a)
    
print(function(n))

# 런타임에러(RecursionError)
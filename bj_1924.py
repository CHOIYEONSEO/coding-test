x, y = map(int, input().split())

def function(a, b):
    date = b
    if a == 1:
        return date
    else:
        a -= 1
        if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
            date += 31
            return function(a, date)
        elif a == 2:
            date += 28
            return function(a, date)
        else:
            date += 30
            return function(a, date)

date = function(x, y)

if (date % 7) == 1:
    print("MON")
elif date % 7 == 2:
    print("TUE")
elif date % 7 == 3:
    print("WED")
elif date % 7 == 4:
    print("THU")
elif date % 7 == 5:
    print("FRI")
elif date % 7 == 6:
    print("SAT")
elif date % 7 == 0:
    print("SUN")
def isLeap(year):
    if year % 400 == 0:
        return 1
    if year % 4 == 0:
        if year % 100 == 0:
            return 0
        return 1
    return 0
year = 2004
print(isLeap(year))
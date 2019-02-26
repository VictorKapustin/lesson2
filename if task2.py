def func(string, string2):
    if not isinstance(string, str) or not isinstance(string2, str):
        return 0
    elif string == string2:
        return 1
    elif len(string) > len(string2):
        return 2
    elif string != string2 and string2 == 'learn':
        return 3


print(func(2, 2))
print(func('f', 2))
print(func('f', 'f'))
print(func('fff', 'f'))
print(func('f', 'learn'))

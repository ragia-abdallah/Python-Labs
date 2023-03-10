print('Method 1')


def strreverse1(str):
    t = len(str)
    rev = ""
    for i in range(t):
        j = t - i - 1
        rev = rev + str[j]
    return rev


print('Say something:')
sen = input()
nes = strreverse1(sen)
print(nes)

print('Method 2')


def strreverse2(str):
    return str[::-1]


print('Say something:')
sen = input()
nes = strreverse2(sen)

print(nes)

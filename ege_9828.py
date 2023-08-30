def from_base_to_ten(n, base):
    n = str(n)
    res = 0
    for i in range(len(n)):
        res += int(n[::-1][i]) * (base ** i)
    return res

def from_ten_to_base(n, base):
    res = ''
    while n != 0:
        res += str(n % base)
        n //= base
    return int(res[::-1])

def transformations(n):
    res = str(from_ten_to_base(n, 3))

    if n % 3 == 0:
        res = '1' + res + '02'
    else:
        res = res + str(from_ten_to_base(n % 3 * 4, 3))
    return from_base_to_ten(res, 3)

A = []
r = 0
for i in range(1, 21):
    r = transformations(i)
    A.append([i, r])

max = 0
for i in A:
    if i[1] < 199 and i[0] > max:
        max = i[0]
print(max)

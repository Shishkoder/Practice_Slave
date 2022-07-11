from math import pow


n = 1_000_000
p = [True] * (n+1)
i = 2

while pow(i, 2) <= n:
    if p[i]:
        for j in range(i * 2, n + 1, i):
            p[j] = False

    i += 1

p[0] = p[1] = False
count = 0

for i in range(1, n + 1):
    if p[i] == False:
        continue

    st = str(i)
    flag = True

    for _ in st:
        st = st[1:] + st[0]
        num = int(st)
        flag &= p[num]

    if flag:
        count += 1
        print(count, i)

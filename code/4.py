# 1

m = int(input("원하는 숫자 m: "))
array = []
index = 0
for i in range(1, 100):    
    if ('3' in str(i)) or ('6' in str(i)) or ('9' in str(i)):
        array.append(i)

print(m, "번 째 수: ", array[m - 1])


# 2

num = int(input("출력 삼각형의 크기: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        if j <= i:
            print(j, end = '')

    print()


# 3

for i in range(9):
    for j in range(8):
        print((j + 2), "x", (i + 1), " = ", (j + 2) * (i + 1), end = '\t')

    print()

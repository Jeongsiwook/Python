# 1

import time

first = input("엔터를 누르고 속으로 10초를 셉니다.")
real_first = time.time()
second = input("10초를 세고 엔터를 누릅니다.")
real_second = time.time()
gap = abs(real_second - real_first)

print("실제 시간: ", abs(real_second - real_first), "초")
print("내가 센 시간과 실제 시간의 차이: ", 10 - gap) 


# 2

val1 = input("문자열 3자리 이상 자릿수를 입력하시오: ")
val2 = val1.split()
step = val2[1]

for i in range(0, len(step)):
    print(val2[0] * int(step[i]))


# 3

string = input("Enter a word which is consist of 5 characters: ")
for i in range(4, -1, -1):
    print(string[i])



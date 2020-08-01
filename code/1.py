# 시간, 분, 초 순서대로 입력하세요(출력)
# 시간(입력)
# 분(입력)
# 초(입력)
# 당신이 입력한 시간은: 0000 초 입니다(출력)

print("시간, 분, 초 순서대로 입력하세요")

hour = int(input())
minute = int(input())
second = int(input())

res = (hour * 3600) + (minute * 60) + second

print("당신이 입력한 시간은: ", res, " 초 입니다")

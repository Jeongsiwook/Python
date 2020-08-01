# 1. 사용자로부터 초 단위 숫자를 입력 받아 시간, 분, 초 단위로 출력하세요

time = int(input("시간을 초 단위로 입력하세요: "))

hour = time // 3600
minute = (time % 3600) // 60
second = time % 3600 % 60

print(hour, "시간", minute, "분", second, "초 입니다.")


# 2. 본인의 영문 이름과 학번을 입력 받은 후 성과 이름, 학번을 각각 다른 줄에 출력하세요
# (1) print문을 4번 쓴 경우

name1, name2, name3, ID = input("Name and School ID: ").split()
print(name1)
print(name2)
print(name3)
print(ID)

# (2) print문을 한 번 쓴 경우

name1, name2, name3, ID = input("Name and School ID: ").split()
print(name1, name2, name3, ID, sep='\n')


# 3. 비밀번호를 미리 설정하여 놓고, 프로그램 실행 시 비밀번호를 입력하면 맞는 지 아닌 지 판단하는 프로그램을 작성하시오

pw = "0638"
pw_input = input("비밀번호를 입력하세요: ")

if (pw == pw_input):
    print("로그인 되었습니다.")

else:
    print("비밀번호가 틀렸습니다.")




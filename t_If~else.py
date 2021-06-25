# 연습문제 2

# ID= input("아이디 입력 : ")
# PW= input("비밀번호 입력 : ")
#
# if ID=="flower" and PW=="1234" :
#     print("로그인 성공!")
# else :
#     print("로그인 실패!")

# s_id= "flower"
# s_pass= "1234"
#
# u_id= input("아이디 입력 : ")
# u_pass= input("비밀번호 입력 : ")
#
# if((s_id==u_id)and(s_pass==u_pass)) :
#     print("로그인 성공!")
# else:
#     print("로그인 실패!")

# 연습문제 3-------------------------------------------------

# w= eval(input("짐의 무게는 얼마입니까? "))
# if(w>20):
#     print('무게 초과, 수수료 20,000원')
#     print('종료합니다.')
# else:
#     print('수수료 없음')
#     print('종료합니다.')

# 연습문제 4--------------------------------------------

# a= eval(input("정수 입력 : "))
# if a%2==1:
#     print("홀수")
# else:
#     print("짝수")

# 연습문제 5----------------------------------------------

# a= int(input("정수1 입력 : "))
# b= int(input("정수2 입력 : "))
# c= int(input("정수3 입력 : "))
# if a<b and b<c :
#     print("제일 큰 수 : ", c)
# elif a>b and b>c :
#     print("제일 큰 수 : ", a)
# else :
#     print("제일 큰 수", b)

# print(----------------------------------------)

# 연습문제 6

# type= int(input("도형 입력(1: 사각형, 2: 삼각형, 3: 원) : "))
# if type==1:
#     a=int(input("가로 입력 : "))
#     b=int(input("세로 입력 : "))
#     weidh= a*b
#     print("사각형의 면적 = ", "%.2f"%(weidh))
# elif type==2:
#     a=int(input("밑변 입력 : "))
#     b=int(input("높이 입력 : "))
#     print("삼각형의 면적 =", "%.2f"%(a*b/2))
# else:
#     a=int(input("반지름 입력 : "))
#     print("원의 면적 =", "%.2f"%(a**2*3.141592))

# type= input(("도형입력(1: 사각형, 2: 삼각형, 3: 원) : "))
# if type=="1" :
#     a=int(input("가로 입력 : "))
#     b=int(input("세로 입력 : "))
#     weidh= a*b
#     print("사각형의 면적 = ", "%.2f" %(weidh))
# elif type=="2" :
#     a=int(input("밑변 입력 : "))
#     b=int(input("높이 입력 : "))
#     print("삼각형의 면적 =", "%.2f"%(a*b/2))
# else :
#     a=int(input("반지름 입력 : "))
#     print("원의 면적 =", "%.2f"% (3.141592*a**2))
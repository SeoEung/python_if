# 07_If중첩
# 사과 상태가 어떤지 확인해서 신선하면 사과 구입
# 단 사과를 살 경우에 가격이 1000원 미만이면 10개를 사고 아니면 5개만 구입

# 사과 상태 입력 받기
# apple_quality = input("사과 상태 입력 : ") # 신선이 들어오면 사과 구입
#
# # 사과를 살건지 결정
# if apple_quality == "신선":
#     apple_price= int(input("사과 가격 입력 : "))
#     if apple_price < 1000:
#         print("사과 10개 구입")
#     else:
#         print("사과 5개 구입")
# else:
#     print("사과를 구입하지 않는다")



# 중첩 if 예제

# 사용자가 현금이나 카드를 선택하면 할인율에 따라 할인액을 계산해주고
# 그 외를 선택하면 잘못입력했다고 문구 송출 후 종료하는 프로그램 작성
# 현금인 경우 15% 할인
# 카드인 경우 5% 할인
# num=int(input("번호 입력 (1. 현금 2. 카드) : "))
# if num == 1 or num == 2 :
#     if num==1:
#         print("15% 할인")
#     else:
#         print("5% 할인")
# else:
#     print("잘못입력했습니다, 종료합니다")

# 결제수단에 따라 할인율 계산
# pay= int(input("지불액 입력 : "))
# if num==1:
#     print("할인율 : 10%")
#     print("할인액 : %d"%(int(pay * 0.1)) + "원")


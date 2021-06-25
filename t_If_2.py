# t_If_2

print("***********상품 정보***********")
print("1. 노트북 : 1,2000,000 원")
print("2. 디지털 카메라 : 400,000 원")
print("*****************************")

num=int(input("상품번호 입력 : "))
if num==1:
    s= int(input("주문 수량 입력 : "))
    p= 1200000
    if(p*s) > 1000000:
        dis= 0.1
    elif 500000 <= (p*s) < 1000000:
        dis= 0.05
    else:
        dis= 1
    print("*********주문 내용*********")
    print("상품명 :     노트북         ")
    print("가격 :      ",format(p,',') ,"원"  )
    print("주문 수량 :  ",s)
    print("주문액 :     ",    format((p*s),','),"원")
    print("할인액 :     ",    format((p*s)*0.1,','),"원")

elif num==2:
    s= int(input("주문 수량 입력"))
    p= 400000
    if (p * s) > 1000000:
        dis = 0.1
    elif 500000 <= (p * s) < 1000000:
        dis = 0.05
    else:
        dis = 1
    print("*********주문 내용*********")
    print("상품명 :     디지털카메라         ")
    print("가격 :      ", format(p, ','), "원")
    print("주문 수량 :  ", s)
    print("주문액 :     ", format((p * s), ','), "원")
    print("할인액 :     ", format((p * s) * 0.1, ','), "원")

else:
    print("잘못 입력하였습니다. 종료합니다.")
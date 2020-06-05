"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""
num = input("주민등록번호 :")
num_list = num.split('-')
check =list(num_list[1])[0]
if check == '1' or check == '3':
    print("남자")
elif check == '2' or check == '4':
    print("여자")
else:
    print("재입력 필요")

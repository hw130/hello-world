def check_id(num):
    if len(num) > 14: #-포함 14글자 넘어가면 종료
        print("잘못 입력하였습니다.")
        return
    print(num)
    if int(num[0]) == 0: #0으로 시작할 경우 2000년 이후 출생자인지 물어보기
        quest=input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
        if quest == 'x':
            if int(num[7]) == 3 or int(num[7]) == 4:#2000년 이후 출생자인데 성별이 1이나 2인 경우
                print('잘못된 번호입니다.\n올바른 번호를 넣어주세요.') #함수 종료
            else:
                if int(num[7]) == 3:
                    print(num[0:2],"년",num[2:4],"월 남자")
                else:
                    print(num[0:2],"년",num[2:4],"월 여자")
        else:
            if int(num[7]) == 1 or int(num[7]) == 3:
                print(num[0:2],"년",num[2:4],"월 남자")
            else:
                print(num[0:2],"년",num[2:4],"월 여자")
    else:
        if int(num[7]) == 3 or int(num[7]) == 4:
            print('잘못된 번호입니다.\n올바른 번호를 넣어주세요.')
            return
        if int(num[7]) == 2:
            print(num[0:2],"년",num[2:4],"월 여자")
        else:
            print(num[0:2],"년",num[2:4],"월 남자")
a=input("주민번호를 입력해주세요: ")
check_id(a)

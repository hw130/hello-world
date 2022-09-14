def gugudan(num):
    try:
        i = 1
        while True:
            result = num * i
            if(i % 2 != 0 and result <= 50):
                print(num, ' X ' , i ,' = ',result)
            elif result >50:
                break
            i=i+1
    except:
        print("잘못 입력하셨습니다.")

number=int(input("몇 단: "))
gugudan(number)

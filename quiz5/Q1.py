def bs31():
    print("베스킨라빈스 써리원 게임")
    print("------------------")

    import random
    number = 0
    while True:
        #my Turn
         my = input("My turn - 숫자를 입력하세요: ")
         my = my.split()
         if (int(my[0]) != number + 1 or len(my) > 3):
             print('다시 입력해주세요')
             continue
         if len(my) == 2:
            if int(my[1])-int(my[0]) != 1:
                print('연속된 숫자를 입력하세요.')
                continue
         if len(my) == 3:
            if int(my[2])-int(my[1]) != 1 or int(my[1])-int(my[0]):
                print('연속된 숫자를 입력하세요.')
                continue
        number = int(my[-1])
        print('현재 숫자: {}'.format(number))

        if(number >= 31):
            print('패배입니다.')
            break

        #computer
        computer=[]
        computer_turn_num = random.randint(1,3)
        for i in range(computer_turn_num):
            number += 1
            #컴퓨터가 31이 넘는 수를 외치면 31로 되돌리기
            if number > 31:
                number -= 1
                continue
            computer.append(number)
            print(f"컴퓨터: {computer-1}")
        print(f"현재숫자 : {number}")
        if 31 in computer:
            print('패배')
            break
    print('게임종료')

bs31()

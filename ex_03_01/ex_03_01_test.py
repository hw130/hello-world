import random
computer=random.randint(0,2)

def rcp(game):
    if computer == 0:
        com = "가위"
    elif computer == 1:
        com = "바위"
    else:
        com = "보"

    if (game == com):
        re = "비겼습니다."
    elif(game == "가위" and com == "보") or (game == "바위" and com == "가위") or (game == "보" and com == "바위"):
        re = "사용자 승리!"
    elif(game == "가위" and com == "바위") or (game == "바위" and com == "보") or (game == "보" and com == "가위"):
        re = "컴퓨터 승리!"
    else:
        print("잘못 입력하셨습니다.")
        quit()
    print("나: ", game)
    print("컴퓨터: ", com)
    print(re)
my=input("가위 바위 보 중에 하나를 입력하세요: ")
rcp(my)

import random
computer=random.randint(0,2)

def rsp_advanced(ga):
    i = 0
    while i < ga:
        my=input("가위 바위 보: ")
        rcp(my)
def rcp(game):
    if computer == 0:
        com = "가위"
    elif computer == 1:
        com = "바위"
    else:
        com = "보"
    if game == 0:
        user = "가위"
    elif game == 1:
        user = "바위"
    else:
        game = "보"

    uc = 0
    usercount = 0
    comcount = 0

    if (game == com):
        re = "비겼습니다."
        uc = 1
    elif(game == "가위" and com == "보") or (game == "바위" and com == "가위") or (game == "보" and com == "바위"):
        re = "사용자 승리!"
        usercount = 1
    elif(game == "가위" and com == "바위") or (game == "바위" and com == "보") or (game == "보" and com == "가위"):
        re = "컴퓨터 승리!"
        comcount = 1
    else:
        print("잘못 입력하셨습니다.")
        quit()
    print("나: ", game)
    print("컴퓨터: ", com)


games = int(input("몇 판을 진행하시겠습니까? : "))
rsp_advanced(games)

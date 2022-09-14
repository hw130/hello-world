birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
age=int(input("한국 나이를 입력하세요: "))
if birth==0:
    print("미국 나이는",age-1," 입니다.")
else :
    print("미국 나이는 ",age-2," 입니다.")

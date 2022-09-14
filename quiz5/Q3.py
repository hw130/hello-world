import random

numbers=[] #3개의 랜덤 숫자 넣을 리스트
min = 101 #최소값
max = 0 #최대값
middle = 0 #중앙값
temp = 0 #최소,중앙,최대값을 정하기 위한 임시 변수
for i in range(3): #총 3개의 랜덤 숫자 생성
    number = random.randint(0, 100)
    numbers.append(number)
for i in range(3): #3개 랜덤 숫자 리스트에서 최소값,중앙값,최대값 정하기
    if numbers[i] < min:
        temp = min
        min = numbers[i]
        numbers[i] = temp
    if numbers[i] > max:
        temp = max
        max = numbers[i]
        numbers[i] = max
    if numbers[i] >min and numbers[i] < max:
        temp = middle
        middle = numbers[i]
        numbers[i] = temp

def guess_numbers():
    i = 0
    count = 0 #맞춘 개수 변수
    words=[] #사용자가 예측한 숫자 저장해놓는 리스트
    while True:
        print(i+1,"차 시도")
        word=int(input('숫자를 예측해보세요: '))

        if word in words: #이미 예측한 숫자를 다시 입력한 경우
            print('이미 예측에 사용한 숫자입니다.')
            i += 1
            continue
        words.append(word) #사용자가 예측한 숫자 리스트에 저장

        if word == min:
            print(f'숫자를 맞추셨습니다!{word}는 최소값입니다.')
            count += 1
        elif word == max:
            print(f'숫자를 맞추셨습니다!{word}는 최대값입니다.')
            count += 1
        elif word == middle:
            print(f'숫자를 맞추셨습니다!{word}는 중앙값입니다.')
            count += 1
        else:
            print('틀렸습니다. 다시 입력해주세요')

        if count == 3:
            print('게임종료')
            print(i+1,'번 시도만에 예측 성공')
            break

        i += 1 #몇 차인지 알려주는 변수

        if i % 5 == 0:
            if word not in numbers:
                print(word,'는 없습니다.')
        #최소값,최대값에 대한 힌트
            if word > min and word < middle:
                print(f'최소값은 {word}보다 작습니다.')
            elif word < min:
                print(f'최소값은 {word}보다 큽니다.')
            elif max < word and word > middle:
                print(f'최대값은 {word}보다 작습니다.')
            elif max > word:
                print(f'최대값은 {word}보다 큽니다.')

guess_numbers()

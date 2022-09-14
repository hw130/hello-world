def count_prime_number(n1, m1):
    i = n1
    count = 0 #소수개수
    if(n1 == 1): #첫 번째 수가 1이면 2부터 시작
        i = 2
    while i <= m1: #마지막 수까지 반복
        j = 2
        bool = True
        while j < i:
            if i % j == 0:
                bool = False #자신 말고 나눠지는 수 존재 시 false
                break
            j = j + 1
        if bool == True: #소수라고 판정났을 시
            count = count + 1
        i = i + 1
    print("소수 개수: ", count)

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
count_prime_number(n, m)

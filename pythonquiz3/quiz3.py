
def find_even_number(n1, m1):
    numbers = [ i for i in range(n,m+1)] # [1,2,3,4,5,6,7,8,9,10]
    i = 0
    middle = int(len(numbers) / 2 )#중앙값 인덱스
    while i < m1:
        if(numbers[i] % 2 == 0):
            print(numbers[i], "짝수")
            if(i == middle and numbers[i] == numbers[middle]): #중앙값 인덱스와 인덱스에 들어있는 값이 같은 경우
                print(numbers[i], "중앙값")
        i = i + 1
# range(시작 숫자, 끝 숫자 + 1)
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n, m)

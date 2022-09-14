def make_comma(num):
    mylist=list(num) #3자리 마다 ,찍는 함수
    i=3
    while i <len(num):
        mylist[i].append(',')
        i += 3
    print(mylist)

in_number=input("숫자를 입력하세요: ")
make_comma(in_number)

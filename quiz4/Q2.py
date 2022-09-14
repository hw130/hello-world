import sys

def count_word(afile, str):
    count = 0
    k = 0
    j = 0
    sys.stdout = open('test1.txt','w') #test1.txt 파일 생성 후 저장
    print(afile)
    for i in afile: #파일 내 문장 한 줄씩 읽기
        while j < len(i):
            if i[k:k+3] == str:
                count += 1
            j += 1
            k += 1
    return count


a ="""안녕하세요.
반갑습니다. 파이썬 공부는 정말 재밌습니다.
"""

cnt = count_word(a, "습니다")
print(cnt)

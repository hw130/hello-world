def grader(student, correct):
    students=[]
    for i in student:
        words = i.split(',') #이름과 정답 분리 저장
        students.append(words) #students리스트에 추가
    count=[] #각 학생들 점수가 들어갈 리스트
    for i in range(5): #학생 수만큼 반복
        j = 0
        total = 0 #각 학생들 점수 변수
        while j < 10: #답 개수만큼 반복
            if correct[j] == int(students[i][1][j]):
                total += 10 #맞으면 점수 10점씩 추가
            j += 1
        count.insert(i,[students[i][0],total]) #학생들 이름이랑 점수 같이 리스트에 추가
    count.sort(key=lambda x:x[-1], reverse=True ) #학생들 점수를 기준으로 내림차순 정렬
    for i in range(5):
        print('학생: ',count[i][0], '점수: ',count[i][1], '점 ',i+1,'등')


# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

grader(s,a)

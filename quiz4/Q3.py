def solution(numbers):
    answer = 0
    my_bool = True
    for i in range(10):
        for j in numbers:
            if i == j:
                my_bool=False
                break
        if my_bool == True:
            answer += i


    return answer

print(solution([1,2,3,4,5,6,7,8]))

# 약수의 합
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i    
        
    return answer
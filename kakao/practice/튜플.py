def solution(s):
    # '{{'와 '}}'를 제거하고, '},{' 기준으로 문자열을 분리
    tuples = s[2:-2].split("},{")
    
    # 각 튜플을 정수의 리스트로 변환하고, 길이에 따라 정렬
    sorted_tuples = sorted([list(map(int, t.split(','))) for t in tuples], key=len)

    answer = []
    for t in sorted_tuples:
        for num in t:
            if num not in answer:
                answer.append(num)
                break

    return answer
  
  
print(solution(input()))
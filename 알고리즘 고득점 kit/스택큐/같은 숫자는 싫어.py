

# main start!

arr = [1,1,3,3,0,1,1]		#TC no.1
#arr = [4,4,4,3,3]		#TC no.2


# main end!

def solution(arr):
    from collections import deque
    dq = deque(arr)
    answer = list()
    while dq :
      d = dq.popleft()
      if len(answer) != 0 :
        if answer[-1] != d :
          answer.append(d)
      else :
        answer.append(d)
    
    return answer
  
print(solution(arr)) 


# def no_continuous(s):
#     # 함수를 완성하세요
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a
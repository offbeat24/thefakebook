import math

# main start!

# nums = [3,1,2,3]		#TC no.1
# nums = [3,3,3,2,2,4]		#TC no.2
nums = [3,3,3,2,2,2]		#TC no.3


# main end!

def solution(nums):
    answer = 0
    N = len(nums)
    set_num = set(nums)
    if len(set_num) >= (N//2) :
      answer = N//2
    elif len(set_num) < (N//2) :
      answer = len(set_num)
    return answer
  
print(solution(nums)) 


# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))
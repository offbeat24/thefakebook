

# main start!

# progresses = [93, 30, 55]		#TC no.1
# speeds = [1, 30, 5]		#TC no.1
progresses = [95, 90, 99, 99, 80, 99]		#TC no.2
speeds = [1, 1, 1, 1, 1, 1]		#TC no.2


# main end!

def solution(progresses, speeds):
  from collections import deque
  q_pro = deque(progresses)
  q_sp = deque(speeds)
  answer = list()
  while q_pro :
    cnt = 0
    if q_pro[0] >= 100 :
      q_pro.popleft()
      q_sp.popleft()
      cnt += 1
      if len(q_pro) == 0 :
        answer.append(cnt)
        break
      while q_pro[0] >= 100:
        q_pro.popleft()
        q_sp.popleft()
        cnt += 1
        if len(q_pro) == 0 :
          answer.append(cnt)
          break
      else :
        answer.append(cnt)
    q_pro= deque([i+j for i,j in zip(q_pro, q_sp)])
  return answer
  
  
print(solution(progresses, speeds)) 


# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]
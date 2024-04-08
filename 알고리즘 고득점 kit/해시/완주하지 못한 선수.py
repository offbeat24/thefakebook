

# main start!

participant = ["leo", "kiki", "eden"]		#TC no.1
completion = ["eden", "kiki"]		#TC no.1
#participant = ["marina", "josipa", "nikola", "vinko", "filipa"]		#TC no.2
#completion = ["josipa", "filipa", "marina", "nikola"]		#TC no.2
#participant = ["mislav", "stanko", "mislav", "ana"]		#TC no.3
#completion = ["stanko", "ana", "mislav"]		#TC no.3


# main end!

def solution(participant, completion):
  participant.sort()
  completion.sort()
  for i in range(len(completion)) :
    if participant[i] != completion[i] :
      answer = participant[i]
      break
  else : 
    answer = participant[-1]
  return answer
  
print(solution(participant, completion)) 



# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
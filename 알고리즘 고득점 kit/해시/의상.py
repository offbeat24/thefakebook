

# main start!

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]		#TC no.1
#clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]		#TC no.2


# main end!

def solution(clothes):
  clothes_hash = dict()
  for cloth in clothes :
    if cloth[1] in clothes_hash :
      clothes_hash[cloth[1]].append(cloth[0])
    else :
      clothes_hash[cloth[1]] = list()
      clothes_hash[cloth[1]].append(cloth[0])
  answer = 1
  for _, val in clothes_hash.items() :
    answer *= (len(val) + 1)
  return answer - 1
  
print(solution(clothes))



def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
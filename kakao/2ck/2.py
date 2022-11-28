def solution(id_list, k):
    answer = 0
    name_list = list()
    pay = dict()
    for i in id_list :
        name_list += list(set(i.split(' ')))
    names = set(name_list)
    for n in names :
        pay[n] = 0
    for n in name_list :
        if pay[n] < k  :
            pay[n] += 1
    answer = sum(pay.values())
    return answer
  
id_list = ["j", "j e j m", "m e m", "e m", "e e e", "m"]
k = 3

print(solution(id_list, k))
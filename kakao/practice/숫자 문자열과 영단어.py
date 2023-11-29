def solution(s):
    replacer = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx,r in enumerate(replacer):
      s = s.replace(r, str(idx))
    answer = int(s)
    return answer


print(solution(input())) 



n = int(input())

answer = 0
for _ in range(n):
    word = input()
    letter = list()
    tmp = word[0]
    for c in word:
        if c not in letter:
            letter.append(c)
            tmp = c
        elif c in letter and c == tmp:
            continue
        else:
            break
    else:
        answer += 1

print(answer)

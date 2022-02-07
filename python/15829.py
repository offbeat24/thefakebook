l = int(input())

st = list(input())
sum = 0
i = 0


def hashing(a, r):
    answer = a * (31**r)
    return answer


for ch in st:
    sum += hashing(ord(ch)-96, i)
    i += 1

print(sum % 1234567891)

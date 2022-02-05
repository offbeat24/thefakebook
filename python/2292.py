num = int(input())

mov = 1
dist = 1

while num > mov:
    mov += 6 * dist
    dist += 1

print(dist)

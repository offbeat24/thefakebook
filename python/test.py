sub1 = "ACAYKP"
sub2 = "CAPCAK"
lcs = [[0] * (len(sub1) + 1) for _ in range(len(sub2)+1)]

print(*lcs)

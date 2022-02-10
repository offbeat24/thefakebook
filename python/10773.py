k = int(input())

bill = list()
for i in range(k) :
  num = int(input())
  if num :
    bill.append(num)
  else :
    bill.pop()
bill.append(0)

print(sum(bill))
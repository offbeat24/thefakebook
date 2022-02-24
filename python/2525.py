hour_, minute_ = map(int, input().split())
plus_ = int(input())


minute_ += (plus_ % 60)

if minute_ >= 60:
    hour_ += 1
    minute_ %= 60

hour_ += plus_ // 60
hour_ %= 24


print(hour_, minute_)

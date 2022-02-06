num = int(input())

words = [input() for _ in range(num)]

words = list(set(words))
words.sort()        
words.sort(key=len)

for word in words:
    print(word)
                
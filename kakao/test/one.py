from collections import defaultdict

def solution(friends, gifts):
    gift_exchange = defaultdict(lambda: defaultdict(int))
    gift_score = defaultdict(int)
    for gift in gifts:
        giver, receiver = gift.split(" ")
        gift_exchange[giver][receiver] += 1
    for giver, receivers in gift_exchange.items():
        for receiver, count in receivers.items():
            gift_score[giver] += count
            gift_score[receiver] -= count
    next_month_gifts = defaultdict(int)
    for friend in friends:
        for other in friends:
            if friend != other:
                if gift_exchange[friend][other] > gift_exchange[other][friend]:
                    next_month_gifts[friend] += 1
                elif gift_exchange[friend][other] == gift_exchange[other][friend]:
                    if gift_score[friend] > gift_score[other]:
                        next_month_gifts[friend] += 1
                    elif gift_score[friend] == gift_score[other]:
                        continue
    
    answer = max(next_month_gifts.values()) if next_month_gifts else 0
    return answer

# 테스트를 위한 예시 데이터
friends_example = ["muzi", "ryan", "frodo", "neo"]
gifts_example = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

# 함수 실행 및 결과 출력
print(solution(friends_example, gifts_example))

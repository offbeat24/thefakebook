def max_rounds_dp(cards, coin, n):
    # Memoization table, key: (frozenset of hand, remaining coins, index in remaining cards)
    memo = {}

    def dp(hand, coins, index):
        if index >= len(cards) or coins < 0:
            return 0

        # Convert hand to a frozenset for hashing
        hand_set = frozenset(hand)

        # Check if we have already computed this state
        if (hand_set, coins, index) in memo:
            return memo[(hand_set, coins, index)]

        max_round = 0
        # Try to pick none, one, or both of the next two cards
        for i in range(4):
            new_hand = hand.copy()
            new_coins = coins
            if index + 2 < len(cards) and cards[index + 1] not in hand and cards[index + 2] not in hand:
                if i == 1:
                    new_hand.append(cards[index + 1])
                    new_coins -= 1
                elif i == 2:
                    new_hand.append(cards[index + 2])
                    new_coins -= 1
                elif i == 3 :
                    new_hand.append(cards[index + 1])
                    new_hand.append(cards[index + 2])
                    new_coins -= 2

            # Check if there's a pair in new_hand that sums up to n+1
            found_pair = False
            for j in range(len(new_hand)):
                for k in range(j + 1, len(new_hand)):
                    if new_hand[j] + new_hand[k] == n + 1:
                        found_pair = True
                        break
                if found_pair:
                    break

            if found_pair:
                max_round = max(max_round, 1 + dp(new_hand, new_coins, index + 2))

        # Try skipping this round
        max_round = max(max_round, dp(hand, coins, index + 2))

        # Save the result in memo and return
        memo[(hand_set, coins, index)] = max_round
        return max_round

    # Initial hand and start index
    initial_hand = cards[:n // 3]
    return dp(initial_hand, coin, n // 3)

# Given example
n = 12
coin = 4
cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
# Calculate the maximum number of rounds using dynamic programming
print(max_rounds_dp(cards, coin, n))




# Calculate the maximum number of rounds





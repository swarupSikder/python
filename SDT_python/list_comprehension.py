nums = [45, 56, 76, 12, 43, 98, 26, 61, 44, 25]

### method (1)

# odds = []
# for num in nums:
#     if num%2 == 1 and num%5 ==0:
#         odds.append(num)
# print(odds)





### method (2)
# odds = [num for num in nums if num%2 == 1 and num%5 == 0]
# print(odds)










players = ['messi', 'pedri', 'marcelo', 'neymar', 'ronaldo']
points = [36, 23, 38, 35, 40]
playerDetails = []

for player in players:
    # print('player: ', player)
    for point in points:
        # print(f'{player}', point)
        playerDetails.append([player, point])


for p in playerDetails:
    print(p[0], p[1])
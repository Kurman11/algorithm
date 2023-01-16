dice1 ,dice2, dice3 = map(int,input().split())


if dice1 == dice2 == dice3:
    print(10000 + max(dice1,dice2,dice3)*1000)
elif dice1 == dice2 or dice2 == dice3 or dice1 == dice3:
    if dice1 == dice2:
        print(1000 + dice1 * 100)
    elif dice2 == dice3:
        print(1000 + dice2 * 100)
    elif dice1 == dice3:
        print(1000 + dice3 * 100)
elif dice1 != dice2 != dice3:
    print(max(dice1,dice2,dice3)*100)

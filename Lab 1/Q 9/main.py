def remove_odds(lst):
    odds = []
    for i in lst:
        if i % 2 != 0:
            odds.append(i)

    for i in odds:
        lst.remove(i)

    return lst


int_list = [1, 5, 32, 6, 4, 535]

print(remove_odds(int_list))
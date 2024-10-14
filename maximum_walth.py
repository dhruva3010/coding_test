def maximum_wealth(accounts):
    max_wealth = 0
    for account in accounts:
        wealth = sum(account)
        if wealth > max_wealth:
            max_wealth = wealth
    return max_wealth

print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))

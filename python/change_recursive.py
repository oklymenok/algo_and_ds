def make_change(change,coins):

	min_coins = change/min(coins)

	if change in coins:
		return 1
	else:
		for i in [c for c in coins if c < change]:
			res = 1 + make_change(change-i,coins)
			if res < min_coins:
				min_coins = res
		return min_coins

coins = [1,5,10,25]
print make_change(22,coins)

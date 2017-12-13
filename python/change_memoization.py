def make_change(change,coins,cache):

	min_coins = change/min(coins)

	if change in coins:
		return 1
	elif change in cache:
		return cache[change]
	else:
		for i in [c for c in coins if c<change]:
			res = 1 + make_change(change-i,coins,cache)
			if res < min_coins:
				min_coins = res
		cache[change] = min_coins
		return min_coins

coins = [1,5,10,25]
cache = {}
print make_change(72,coins,cache)

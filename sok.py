import operator

bought = [float(x) for x in input().split()]
recipe = [float(x) for x in input().split()]
ratios = map(operator.truediv, bought, recipe)
min_ratio = min(ratios)
left_over = []
for i in range(3):
    left_over.append(bought[i] - (recipe[i] * min_ratio))
print(left_over[0], left_over[1], left_over[2])

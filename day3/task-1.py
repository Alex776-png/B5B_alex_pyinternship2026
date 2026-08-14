prices = [100,200,300,400,500,600,700,800,900,696]

average = sum(prices) / len(prices)

result=[price for price in prices if price>average]
print('Average =',average)
print('Above Average = ',result)
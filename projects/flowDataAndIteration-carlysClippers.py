hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1.
total_price = 0

# 2.
for price in prices:
	total_price += price

# 3.
average_price = total_price / len(prices)

# 4.
print("Average Haircut Price: "+str(average_price))

# 5.
new_prices = [new_price-5 for new_price in prices]

# 6.
print(new_prices)

# 7.
total_revenue = 0

# 8. & 9.
for i in range(len(hairstyles)):
	total_revenue = prices[i] + last_week[i]

# 10.
print("Total Revenue: "+str(total_revenue))

# 11.
average_daily_revenue = total_revenue/7
print(average_daily_revenue)

# 12.
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]

# 13.
print(cuts_under_30)
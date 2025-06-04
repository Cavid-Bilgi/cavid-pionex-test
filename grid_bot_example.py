entry_price = 0.0025
grid_count = 10
grid_spacing = 0.0001

buy_levels = [entry_price - i * grid_spacing for i in range(1, grid_count + 1)]
sell_levels = [entry_price + i * grid_spacing for i in range(1, grid_count + 1)]

print("Buy Levels:", buy_levels)
print("Sell Levels:", sell_levels)

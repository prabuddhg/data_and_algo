"""
daily_price = [2, 5, 1, 3]

cash vs stocks

cash_and_no_stocks (return) = max(stock_sell, stock_hold) ---> understood
cash_with_stocks = max(cash_buy, cash_hold)               ---> understood

cash_buy   = cash_and_no_stocks - daily_price (lost) ---> understood
cash_hold  = cash_with_stocks                        ---> understood

stock_sell = cash_with_stocks + daily_price  (gain)  ---> understood
stock_hold = cash_and_no_stocks                      ---> not understood












start--->cash-----hold---->cash
              \          /
                \buy   /sell
                  \  /
                  / \
                 /    \
        stock  --hold--->stock

cash_hold (strategy_hold)
cash_buy (strategy_buy )
stock_hold (strategy_avoid)
stock_sell (strategy_sell)

max(strategy_hold vs strategy_buy)
max(strategy_avoid vs strategy_sell)

Day1: cash_buy (0) and stock_buy(2) and cash_hold(infinite)
Day2: stock_sell (5) and profit is stock_sell-stock_buy (3)
Day3: cash_buy (0) and stock_buy(1) and cash_hold(infinite)
Day4: stock_sell (3) and profit is stock_sell-stock_buy (2)
Total profit = 3+2 = 5

profit = []
cash_not_owning_share = 0
cash_owning_share = -infinity
for each_price in daily_price:
    strategy_buy = cash_not_owning_share - each_price
    strategy_hold = cash_owning_share
    strategy_avoid = cash_not_owning_share
    strategy_sell = cash_owning_share + each_price
    cash_owning_share = max(stock_sell, stock_hold)
    cash_not_owning_share = max(cash_buy, cash_hold)
"""
daily_price = [2, 5, 1, 3]
def max_profit(daily_price):
    cash_not_owning_share = 0
    cash_owning_share = -1000000
    count = 1
    for each_price in daily_price:
        print(f'\nprice on day {count} is {each_price} and initial net worth without stocks ={cash_not_owning_share} and net worth with stocks ={cash_owning_share}')
        count += 1
        strategy_buy_stock = cash_not_owning_share - each_price
        strategy_hold_cash = cash_owning_share
        strategy_avoid = cash_not_owning_share
        strategy_sell = cash_owning_share + each_price
        print(f'strategy_buy_stock {strategy_buy_stock}')
        print(f'strategy_hold_cash {strategy_hold_cash}')
        print(f'strategy_avoid {strategy_avoid}')
        print(f'strategy_sell {strategy_sell}')
        if strategy_buy_stock > strategy_hold_cash:
            cash_owning_share = strategy_buy_stock
            print(f'|->if bought stock for {each_price}, net worth with stock={cash_owning_share}, bought')
        else:
            cash_owning_share = strategy_hold_cash
            print(f'|->if bought stock for {each_price}, net worth with stock={cash_owning_share}, not bought')
        if strategy_avoid > strategy_sell:
            cash_not_owning_share = strategy_avoid
            print(f'|->if sold stock for {each_price}, net worth without stock={cash_not_owning_share}, not sold stock')
        else:
            cash_not_owning_share = strategy_sell
            print(f'|->if sold stock for {each_price},net worth without stock={cash_not_owning_share}, sold stock')


    return cash_not_owning_share

print(max_profit(daily_price))

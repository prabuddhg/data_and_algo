

'''

day n:
    stock_price
    net_worth_no_stock = 0
    net_worth_with_stock = -inf

    4 variables:
    hold_cash = net_worth_no_stock
    buy_stock = net_worth_no_stock - stock_price

    sell_stock = stock_price
    avoid_sell_stock = net_worth_with_stock

	                   formula                          day 1	    day 2	day 3	day 4	profit
price	                                                    2	        5	    1	    3
net worth without	  =max(avoid sell stock, sell stock)    0	        0	    3	    3	    5
net worth with stocks =max(hold cash, buy stock)        -10000	        -2	   -2	    2	    2

hold cash 	          =net worth with stocks            -10000	        -2	   -2	    2
buy stock	          =net worth without - price            -2	        -5	    2	    0

sell stock	          =net worth with stocks - price   -999998	        3	   -1	    5
avoid sell stock	  =net worth without                     0	        0	    3	    3

'''
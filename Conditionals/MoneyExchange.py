# Calculate how many bills and coins the amount entered equals.

money = int(input('Value (€): '))

exchange, money = divmod(money, 50)

if money > 0:
    exchange, money = divmod(money, 20)
    
    if exchange > 0:
        print(exchange, 'bills of 20€.')
    
    if money > 0:
        exchange, money = divmod(money, 10)
        
        if exchange > 0:
            print(exchange, 'bills of 10€.')
        
        if money > 0:
            exchange, money = divmod(money, 5)
            
            if exchange > 0:
                print(exchange, 'bills of 5€.')
            
            if money > 0:
                exchange, money = divmod(money, 2)
                
                if exchange > 0:
                    print(exchange, 'coins of 2€.')
                
                if money:
                    print(exchange, 'coins of 1€.')
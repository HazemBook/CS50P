def main():
    amount_due = 50
    
    change = calculate(amount_due)

    print("Changed Owed: ", change)


# calculate change owed
def calculate(amount_due):
    while (amount_due > 0):
        print("Amount Due: ", amount_due)
        
        insert_coin = int(input("Insert Coin: "))

        if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
            amount_due -= insert_coin
    
    # make sure to return a positive value
    return abs(amount_due)


# call main
main()
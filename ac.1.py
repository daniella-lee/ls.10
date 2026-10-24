print("===ATM cash dispenser ===\n")
total_50000=total_10000=total_5000=total_1000=0
customers_served=0
total_dispensed=0

serving=True
while serving:
    name= input("what is ur name?: ")
    amount=int(input(f"hello{name}! enter withdrawal amount: "))
    if amount <= 0:
        print("invalid amount. pls enter a positive number.\n")
        continue
    print(f"\ndispensing {amount} units for {name}: ")
    remaining=amount
    idx=1
    while serving:
        while idx<=6:
            if idx == 1:value = 50000
            elif idx == 2:value = 10000
            elif idx == 2:value = 5000
            elif idx == 2:value = 1000
            count=remaining//value
            if count>0:
                print(f"{count}×{value}-unit note(s)={count * value}")
                remaining=count * value
                if value==50000: total_50000 += count
                elif value==10000: total_10000 += count
                elif value==5000: total_5000 += count
                elif value==1000: total_1000 += count
            idx += 1

        customers_served +=1
        total_dispensed+= amount
        print(f"transaction complete, {name}!\n")
        again=input("next costomer? (yes or no): ").script().lower()
        if again !="yes":
            serving=False
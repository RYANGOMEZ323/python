##MATCH CASE

print("WELCOME TO KOMINOS PIZZA SHOP")
print("GOOD MORNING SIR//MADAM")
print("ENTER 1 FOR SMALL(RS.150) \nENTER 2 FOR MEDIUM(RS.350)\nENTER 3 FOR LARGE(RS.550)")
SIZE=int(input("WHAT SIZE OF PIZZA DO U PREFER:"))
SMALL = 150
MEDIUM = 350
LARGE = 550
match SIZE:
    case 1:
        print("U SELECTED SMALL SIZE")
        q = int(input("HOW MANY PIZZAS DO U WANT:"))
        totalAmt = q * SMALL
        print("U R TOTAL AMOUNT IS",totalAmt)
        print("DO U NEED TOPPINGS,\nIF NEEDED PRESS '1'\nELSE PRESS '0'")
        top=int(input("TOPPINGS:"))
        match top:
            case 1 :
                print("U SELECTED TOPPINGS")
                TOP = 10
                t=(int(input("HOW MANY NEEDED:")))
                tot= (TOP * t)+ totalAmt
                print("U R TOTAL AMOUNT IS ",tot)
                cost=int(input("PLS PAY THE ABOVE AMOUNT: "))
                if(cost>=tot):
                    if(cost==tot):
                        print("THANK U PURCHASING OUR ITEM")
                    else:
                        print(cost-tot,"HERE IS U R CHANGE")
                        print("THANK U PURCHASING OUR ITEM")
                        
            case _:
                print("U DIDNT SELECT TOPPINGS")
                print("U R TOTAL IS ",totalAmt)
                if(cost>=totalAmt):
                    if(cost==totalAmt):
                        print("THANK U PURCHASING OUR ITEM")
                        
                    else:
                        print(cost-totalAmt,"HERE IS U R CHANGE")
                        print("THANK U PURCHASING OUR ITEM")
                else:
                    print("PLEASE PAY THE CORRECT AMOUNT")
    case 2 :
        print("U SELECTED MEDIUM SIZE")
        q = int(input("HOW MANY PIZZAS DO U WANT:"))
        totalAmt = q * MEDIUM
        print("U R TOTAL AMOUNT IS",totalAmt)
        print("DO U NEED TOPPINGS,\nIF NEEDED PRESS '1'\nELSE PRESS '0'")
        top=int(input("TOPPINGS:"))
        match top:
            case 1 :
                print("U SELECTED TOPPINGS")
                TOP = 10
                t=(int(input("HOW MANY NEEDED:")))
                tot= (TOP * t)+ totalAmt
                print("U R TOTAL AMOUNT IS ",tot)
                cost=int(input("PLS PAY THE ABOVE AMOUNT: "))
                if(cost>=tot):
                    if(cost==tot):
                        print("THANK U PURCHASING OUR ITEM")
                    else:
                        print(cost-tot,"HERE IS U R CHANGE")
                        print("THANK U PURCHASING OUR ITEM")
            case _:
                print("U DIDNT SELECT TOPPINGS")
                print("U R TOTAL IS ",totalAmt)
                if(cost>=totalAmt):
                    if(cost==totalAmt):
                        print("THANK U PURCHASING OUR ITEM")
                        
                    else:
                        print(cost-totalAmt,"HERE IS U R CHANGE")
                        print("THANK U PURCHASING OUR ITEM")
                else:
                    print("PLEASE PAY THE CORRECT AMOUNT")
    case 3 :
        print("U SELECTED LARGE SIZE")
        q = int(input("HOW MANY PIZZAS DO U WANT:"))
        totalAmt = q * LARGE
        print("U R TOTAL AMOUNT IS",totalAmt)
        print("DO U NEED TOPPINGS,\nIF NEEDED PRESS '1'\nELSE PRESS '0'")
        top=int(input("TOPPINGS:"))
        match top:
            case 1 :
                print("U SELECTED TOPPINGS")
                TOP = 10
                t=(int(input("HOW MANY NEEDED:")))
                tot= (TOP * t)+ totalAmt
                print("U R TOTAL AMOUNT IS ",tot)
                cost=int(input("PLS PAY THE ABOVE AMOUNT: "))
                if(cost>=tot):
                    if(cost==tot):
                        print("THANK U PURCHASING OUR ITEM")
                    else:
                        print(cost-tot,"HERE IS U R CHANGE")
                        print("THANK U PURCHASING OUR ITEM")
            case _:
                print("U DIDNT SELECT TOPPINGS")
                print("U R TOTAL IS ",totalAmt)
                if(cost>=totalAmt):
                    if(cost==totalAmt):
                        print("THANK U PURCHASING OUR ITEM")
                        
                    else:
                        print(cost-totalAmt,"HERE IS U R CHANGE")
                        print("THANK U PURCHASING OUR ITEM")
                else:
                    print("PLEASE PAY THE CORRECT AMOUNT")
    case _ :
        print("INVALID SIZE OF PIZZA")
        


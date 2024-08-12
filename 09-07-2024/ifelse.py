#NESTED IF ELSE(GROCERY SHOP)

print("WELCOME TO RYAN GROCERY SHOP")
print("----------------------------")
greeting = input("GOOD MORNING SIR\\MADAM:")
products = int(input("ENTER0 or 1 0r 2 or 3 \n0:RICE\n1:SUGAR\n2:SALT\n3:WHEAT\nENTER U R PURCHASED PRODUCT:"))
if(products==0):
    ricePrice = 50
    print("U SELECTED RICE")
    quantity= int(input("HOW MUCH REQUIRED(IN KGS):"))
    totalAmount = ricePrice * quantity
    print("the amount of rice is ", totalAmount)
    cost=int(input("please pay the above amount:"))
    if(cost>=totalAmount):
        if(cost == totalAmount):
            print("THANK U FOR PURCHASING OUR PRODUCT")
        else:
            print(cost - totalAmount, "here is your change")
            print("THANK U FOR PURCHASING OUR PRODUCT")
        
    else:
        print("please pay the correct amount")
elif(products ==1):
    sugarPrice = 30
    print("U SELECTED SUGAR")
    quantity= int(input("HOW MUCH REQUIRED(IN KGS):"))
    totalAmount = sugarPrice * quantity
    print("the amount of sugar is ", totalAmount)
    cost=int(input("please pay the above amount:"))
    if(cost>=totalAmount):
        if(cost == totalAmount):
            print("THANK U FOR PURCHASING OUR PRODUCT")
        else:
            print(cost - totalAmount, "here is your change")
            print("THANK U FOR PURCHASING OUR PRODUCT")
        
    else:
        print("please pay the correct amount")
elif(products ==2):
    saltPrice = 20
    print("U SELECTED SALT")
    quantity= int(input("HOW MUCH REQUIRED(IN KGS):"))
    totalAmount = saltPrice * quantity
    print("the amount of salt is ", totalAmount)
    cost=int(input("please pay the above amount:"))
    if(cost>=totalAmount):
        if(cost == totalAmount):
            print("THANK U FOR PURCHASING OUR PRODUCT")
        else:
            print(cost - totalAmount, "here is your change")
            print("THANK U FOR PURCHASING OUR PRODUCT")
        
    else:
        print("please pay the correct amount")
elif(products ==3):
    wheatPrice = 40
    print("U SELECTED WHEAT")
    quantity= int(input("HOW MUCH REQUIRED(IN KGS):"))
    totalAmount = wheatPrice * quantity
    print("the amount of wheat is ",totalAmount)
    cost=int(input("please pay the above amount:"))
    if(cost>=totalAmount):
        if(cost == totalAmount):
            print("THANK U FOR PURCHASING OUR PRODUCT")
        else:
            print(cost - totalAmount, "here is your change")
            print("THANK U FOR PURCHASING OUR PRODUCT")
        
    else:
        print("please pay the correct amount")
else:
    print("sorry invalid product")

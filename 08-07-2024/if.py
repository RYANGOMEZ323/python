#08-07-2024




speed = int(input("ENTER THE SPEED:"))
##print(speed)
##if(speed<=0):
##    print("dsdsdx")
##    
##elif(speed <=40):
##    print("SAFE")
##elif(speed<40 or speed>60):
##    print("SAFE DRIVING")    
##elif(speed >100):
##    print("danger")
##    
##else:
##    print("not safe")
    
if(speed>0 and speed<40):
    print("safe for driving")
elif(speed>40 and speed<60):
    print ("safe driving")
elif(speed>60 and speed<80):
    print (" warning")
elif(speed>=80):
    print("danger")
else:
    print("vehicle is yet to be started")
           

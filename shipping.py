#Asks for user input for the weight of the package
print("Welcome to Sal's Shipping Company!")
weight = float(input("What is the weight of your package, in total pounds?\n"))
cost = 0

print("Calculating......\n")

#Ground Shipping Cost
gship = 0.0
flat_charge = 20.00
if weight <= 2.00:
    cost = 1.50 * weight + flat_charge
elif  2 <= weight <= 6:
     cost = 3.00 * weight + flat_charge
elif 6 <= weight <= 10:
    cost = 4.00 * weight + flat_charge
elif weight >= 10:
    cost = 4.75 * weight + flat_charge
else:
    print ("Error")
gship = cost
print("Ground Shipping Total:$ ", gship, "\n")    

#Ground Shipping Premium Cost
gship_premium = 125.00
print("Ground Shipping Premium: $", gship_premium, "\n")

#Drone Shipping Cost
dship = 0.0
if weight <= 2.00:
    cost = 4.50 * weight 
elif  2 <= weight <= 6:
     cost = 9.00 * weight 
elif 6 <= weight <= 10:
    cost = 12.00 * weight 
elif weight >= 10:
    cost = 14.25 * weight
else:
    print ("Error")
dship = cost
print("Drone Shipping: $", dship, "\n")

#Choses the cheapest option
list = [gship, gship_premium, dship]
if min(list) == gship:
    print("Best Deal is Ground Shipping: $", gship)
elif min(list) == gship_premium:
    print( "Best Deal is Ground Shipping Premium: $", gship_premium)
elif min(list) == dship:
    print("Best Deal is Drone Shipping: $", dship)
else:
    print("Error")





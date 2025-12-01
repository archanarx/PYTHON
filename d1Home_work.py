import random
# Use variables to store the prices and quantities.
ricePrice = 45
sugarPrice = 40
oilprice = 130

riceQuantity = 3.0
sugarQuantity = 2.5
oilQuantity = 1.8

# Calculate and print the total price for each item and the final total bill.
riceTotal = ricePrice * riceQuantity
sugarTotal = sugarPrice * sugarQuantity
oilTotal = oilprice * oilQuantity

finalBill = riceTotal + sugarTotal + oilTotal

print("Total price of rice : " , riceTotal )
print("Total price of sugar : " , sugarTotal )
print("Total price of oil : " , oilTotal)

print ("Final Bill : " , finalBill)

# Show the total bill as an integer and also as a string using explicit conversion.
billAsInt = int(finalBill)
billAsStr = str(finalBill)

print("Final bill as int : " , billAsInt )
print("Final bill as str : " , billAsInt)


# Use random number generation to add a random ?5–?10 delivery charge.
deliveryCharge = random.randrange(5,10)

print("Delivery Charge : " , deliveryCharge)

# Show the final bill amount including delivery charge.
totalWithDelivery = finalBill + deliveryCharge

print("Total Amount with delivery charge : " , totalWithDelivery)


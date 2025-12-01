# Store the volume of each juice in separate variables.
appleJuice = 15.5
orangeJuice = 20
grapeJuice = 10.25

# Calculate the total volume sold and print it.
totalVolume = appleJuice + orangeJuice + grapeJuice
print(totalVolume)

# Convert the total volume to an integer and print it.
totalVolume = int(totalVolume)
print(totalVolume)

# Convert the total volume to a string and print it with a message.
totalVolume = str(totalVolume)
print("Total Volume in string: " + totalVolume)


# Add a random number between 5 and 10 (representing additional bonus liters) and print the final total.
import random
bonusLiters = (random.randrange(5,10))
print(bonusLiters)
totalVolume = int(totalVolume)
finalTotal = bonusLiters + totalVolume
print(finalTotal)








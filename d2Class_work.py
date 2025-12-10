# Multiline receipt header
header = """\n\tBOOKSTORE RECEIPT
"""

#Item details
title1 = "Python Basics"
price1 = 450

title2 = "Data Science Intro"
price2 = 600

#  use a single string with basic {} placeholders and call format() once to fill in the values.
line1 = "\t{} - ₹{}\n" .format(title1, price1)
line2 = "\t{} - ₹{}\n" .format(title2, price2)

# total price
total = price1 + price2
totalLine = "\tTOTAL: ₹{}\n" .format(total)

thankYou = "\n\tTHANK YOU FOR SHOPPING WITH US!"
receipt = header + line1 + line2 + totalLine + thankYou

print(receipt.upper())
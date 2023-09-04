###  You are making a ticketing system. The price of a single ticket is $100. For children undeer 3, it is free.
###  Your program needs to take the ages of 5 passengers as input and output the total price of their tickets.


total = 0
i = 0
while i < 5:
    age = int(input())
    i = i + 1
    if age < 3:
        continue
    total +=100
print(total)

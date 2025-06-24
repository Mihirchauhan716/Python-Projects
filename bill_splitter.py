
bill = float(input("Enter bill amount: "))
people = int(input("People sharing: "))
tip = float(input("Tip %: "))

total = bill + (bill * tip / 100)
print("Each person pays:", round(total / people, 2))

# Total sum of the digits
# This test sums all the digits in the given input
# Note: it accepts only integers

n = int(input("Enter a number:"))
input_digits = n
tot = 0
while ( n > 0 ):
    dig = n % 10
    tot = tot + dig
    n = n // 10

print("The total sum of the digits",input_digits,"is:",tot)


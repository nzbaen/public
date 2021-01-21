# Reverse number
# This test takes the number you enter and reverses it
# Note: it accepts only numbers without decimals
# You can change 'n' into a variable of your choice (i.e. can be filled by system's response)

n = int(input("Enter number: "))
input_number = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

print("The reverse of the number",input_number,"is:",rev)


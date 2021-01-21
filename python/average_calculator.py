# Average calculation
# This test takes the number of elements that you are going to input
# and the elements, and calculates the average between them
# You can change 'n' into a variable of your choice (i.e. can be filled by system's response)
# You can change the 'elem' array 

n = int(input("Enter the number of elements to be inserted: "))
a = []
for i in range(0,n):
    elem = int(input("Enter element: "))
    a.append(elem)
    avg = sum(a)/n

print("Average of elements in the list",round(avg,2))
print("Average of elements in the list removing decimal and rounding the number",round(avg))


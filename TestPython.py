#Sum of Natural Numbers
print("Sum of Natural Numbers")
num = int(input("\nEnter a number: "))

if num < 0:
    print("\nEnter a positive number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("\nThe sum is", sum)
    print("\n**********")
print("\n End of Program")
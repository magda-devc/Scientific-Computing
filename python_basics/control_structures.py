def ifEvenorOdd(a):
    if a%2 == 0:
        return "Even"
    #to return a value while calling the function
    else:
        return "Odd"

a = int(input("Enter an integer: "))
print("The number ", a, " is", ifEvenorOdd(a))

#for loop
for i in range(1, 50):
    if i%2 ==0:
        print(i)


#while loop
a  = 10
while a>0:
    print(a)
    a = a-1
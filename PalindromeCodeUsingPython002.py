

array_size = int(input("Enter the Size of the Array:= "))

first_array = []
reversed_array = []

for i in range(array_size):
    myPrompt = "Please enter the " + str(i) + " Array Element: "
    xVal = input(myPrompt)
    first_array.append(xVal)
    reversed_array.append(xVal)

reversed_array.reverse()

print("Entered Array:" + '\n' + str(first_array))

print("Reversed Array:" + '\n' + str(reversed_array))

if(first_array == reversed_array):
    print("Entered Array is a Palindrome")


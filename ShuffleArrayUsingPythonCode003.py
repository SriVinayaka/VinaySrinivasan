

import random

myPrompt = "Enter the Array Size:= "
array_size = int(input(myPrompt))

myArray = []
arrVal = ""

for i in range(array_size):
    myPrompt = "Enter the Array Value at index: (" + str(i) + ") = "
    arrVal = str(input(myPrompt))
    myArray.append(arrVal)

myRandomArray = myArray

print(myRandomArray)

arrVal = ""
for i in range(array_size):
    for arrVal in myArray:
        random.shuffle(myRandomArray)
        print(myRandomArray)





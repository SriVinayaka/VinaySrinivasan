

array_size = int(input("Enter the x Array Size:="))

print(array_size)

xVal = []
yVal = []

myPromptString = ""
for iX in range(array_size):
    myPromptString = "Enter Value for First Array(xVal) at " + str(iX) + " Index = " 
    nVal = input(myPromptString)
    xVal.append(nVal)

myPromptString = ""
for iX in range(array_size):
    myPromptString = "Enter Value for Second Array (yVal) at " + str(iX) + " Index = " 
    nVal = input(myPromptString)
    yVal.append(nVal)


for i in xVal:
    print(i);

for i in yVal:
    print(i);

#To Check Palindrome
palin = 0
palin_array = []

for iX in range(array_size):
    if(xVal[iX] == yVal[iX]):
        palin += 1
        palin_array.append(xVal[iX])
    else:
        continue

itr = 0
print("Palindrome Count = ", palin)
if(palin != 0):
    for j in palin_array :
        print("palin array at ", itr, " = ", j)
        itr += 1




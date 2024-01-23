# Anthony Rapp
# Github: GitRappOSU
#1/22/24
# Assignment 3a, determines minimum and maximum value for any number of integers >= 1

num = int(input("How many integers would you like to enter?"))
print("Please enter", num, "integers.")
_min = int(input())
_max = _min
for i in range(1,num_1):
    number = int(input())
    if number > _max:
        _max = number
    if number < _min:
        _min = number
print("min:", _min)
print("max:" , _max)

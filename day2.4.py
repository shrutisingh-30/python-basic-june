#count vowels in a string
str= input("enter a string: ")
vowels= "aeiou"
count=0
for char in str:
    if char in vowels:
        count+=1

print("no of vowels:" , count)
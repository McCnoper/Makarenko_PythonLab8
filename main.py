print("Task 1")
import random
line = str(input("Enter a sentence: "))
amount = 0
while True:
    try:
        x = int(input("Modes: 1–Vowels, 2-Consonants, 3-All: "))
        if not (x in [1,2,3]):
            raise ValueError
        y = int(input("Output: 1–Amount, 2-Print: "))
        if not (y in [1,2]):
            raise ValueError
        for i in line:
            if x==1 and (i in "aeiou"):
                if y==2:
                    print(i)
                amount+=1
                
            elif x==2 and not(i in "aeiou"):
                if y==2:
                    print(i)
                amount+=1
            elif x==3:
                if y==2:
                    print(i)
                amount+=1
        if y==1:
            print(amount)
        print("End")
        break
    except ValueError:
        print("Enter only proposed modes")
print("---------------------------")
print("Task 2")
first = [1,4,5,8]
second = [2,3,6,7]
choice = input("Actions: 1-Merge, 2-Remove duplicates, 3-Sort")
if choice == "1":
    result = first + second
elif choice == "2":
    result = list(set(first + second))
elif choice == "3":
    result = sorted(first + second)
elif choice == "4":
    result = first + second
print(result)

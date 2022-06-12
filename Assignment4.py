#Q.1
#Getting input from user
m=int(input("Enter Marks :"))
#assigning grade according to marks
if(m<25):
    print(" Grade F ")
elif(m>=25 and m<45):
    print(" Grade E ")
elif(m>=45 and m<50):
    print(" Grade D ")
elif(m>=50 and m<60):
    print(" Grade C ")
elif(m>=60 and m<80):
    print(" Grade B ")
elif(m>=80):   
    print(" Grade A ")
else:
    print(" No result ")

#Q.2
#Taking an input from the user
year = int(input("Enter a year: "))
#Checking if the given year is leap year
if year % 4 == 0 :
    print("year is a Leap Year")
elif year % 100 == 0 :
    print("year is not a Leap Year")
elif year % 400 == 0 :
    print(" year is a Leap Year")
else :
    print("year is not a Leap Year")

#Q.3
import random
for i in range(10):
    #Generating random number num1
    num1 = random.randint(1,10)
    #Generating random number num2
    num2 = random.randint(1,10)
    print(f"Question {i+1}:",end="")
    #Getting the user answer
    user_output = int(input(f"{num1}X{num2}="))
    #Checking if user answer matchea actual answer
    if user_output == (num1*num2):
    #Printing correct if answer matches
        print("Right!")
    else:
        print(f"Wrong.The right answer is {num1*num2}")
    

#Q.4
x=200

for candies in range(x):
#Conditions For determining number of candies
    if candies % 5 == 2:
       if candies % 6 == 3:
          if candies % 7 == 2:
             print(candies, 'candies are in the bowl!')
             break


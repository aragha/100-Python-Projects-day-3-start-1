# # print("Welcome to the rollercoaster!")
# # height = int(input("What is your height in cm? "))
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
def exercise1():
#Write your code below this line 👇
  x = number % 2
  if x == 0:
      print("This is an even number.")
  else:
      print("This is an odd number.")

def exercise2():
  # 🚨 Don't change the code below 👇
  height = float(input("enter your height in m: "))
  weight = float(input("enter your weight in kg: "))
  # 🚨 Don't change the code above 👆
  
  #Write your code below this line 👇
  bmi = round(weight / (height * height))
  interpretations = ["are underweight.", 
  "have a normal weight.",
  "are slightly overweight",
  "are obese.",
  "are clinically obese."
  ]
  # It should tell them the interpretation of their BMI based on the BMI value.
  
  # Under 18.5 they are underweight
  # Over 18.5 but below 25 they have a normal weight
  # Over 25 but below 30 they are slightly overweight
  # Over 30 but below 35 they are obese
  # Above 35 they are clinically obese.
  if bmi >= 35:
      print(f"Your BMI is {bmi}, you {interpretations[4]}")
  else:
    if bmi >= 30:
      print(f"Your BMI is {bmi}, you {interpretations[3]}")
    elif bmi >= 25:
        print(f"Your BMI is {bmi}, you {interpretations[2]}")
    elif bmi >= 18.5:
        print(f"Your BMI is {bmi}, you {interpretations[1]}")    
    else:
        print(f"Your BMI is {bmi}, you {interpretations[0]}")        

def exercise3():
  # 🚨 Don't change the code below 👇
  year = int(input("Which year do you want to check? "))
  # 🚨 Don't change the code above 👆
  
  #Write your code below this line 👇
  if year % 4 == 0:
    if year % 100 != 0:
      print("Leap year.")
    elif year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
      
  else:
    print("Not leap year.")
      


exercise3()
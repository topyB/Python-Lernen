# Aufgabe 15B - "Forty Below In The Water" 
# https://cscircles.cemc.uwaterloo.ca/15b-python-pushups/
#
# In this exercise, you will create a temperature converter which will convert Fahrenheit values to Celsius and vice-versa. 
# You will need the following two formulas which relate the temperature f in Fahrenheit to the temperature c in Celsius:
#
#Fahrenheit
# f = c*(9/5)+32
# Celsius
# c = (f-32)*(5/9)
#
# The input will be a string consisting of a floating-point number followed immediately by the letter F or C, such as "13.2C". 
#   You should convert to the other temperature scale and print the converted value in the same format. 
#   For example, if the input is "8F" then the output should be (approximately) "-13.333C", and if the input is "12.5C" then the output should be "54.5F".

#Meine Lösung: 

temp = input()

if temp.endswith("F") == True:
   temp = temp.replace("F","")
   Celsius = (float(temp)-32)*(5/9)
   print(str(Celsius)+"C")
   
elif temp.endswith("C") == True:
   temp = temp.replace("C","")
   Fahrenheit = (float(temp))*(9/5)+32
   print(str(Fahrenheit)+"F")

   
   
   
   
   

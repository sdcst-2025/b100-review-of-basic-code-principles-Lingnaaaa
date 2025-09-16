"""
### Name:
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""


def calculate_I(lengthtime): 
  if lengthtime_type == 'year':
    return P*r*lengthtime
  if lengthtime_type == 'month':
    return P*r*(lengthtime / 12)
  if lengthtime_type == 'day':
    return P*r*(lengthtime / 365) 

P=float(input("Enter the principal($):"))
r=float(input("Enter the interest rate per year:"))
lengthtime_type = input("Enter the time unit('year''month''day'):")
lengthtime=float(input(f"Enter the lengthtime in {lengthtime_type}:"))

interest=calculate_I(lengthtime)
print(f"The interest earned is ${interest:.2f}")

'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.
'''


# 🚨 Don't change the code above 👆
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")

#Write your code below this line 👇


n_month = 90*12
n_week = 90*52
n_day =  90*365

a_month = int(age)*12
a_week = int(age)*52
a_day = int(age)*365

r_month = n_month - a_month
r_week = n_week - a_week
r_day = n_day - a_day


print(f"You have {r_day} days, {r_week} weeks, and {r_month} months left")


#Below is the actual solution provided by the lecturer

'''
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)
'''
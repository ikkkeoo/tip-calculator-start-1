#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("welcome to the tip calculator")
bill = float(input("what was the total bill? $"))
num_people = int(input("how mant ppl to split the bill? "))
percent_tip = input("what % would you like to give? 10, 12 or 15? ")

percent_tip = int(percent_tip) / 100

pay_per_ppl = round(bill / num_people * (1+percent_tip),2)
pay_per_ppl = "{:.2f}".format(pay_per_ppl)
print(f"each person shoud pay:$ {pay_per_ppl}")
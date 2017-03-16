# BMR Calculator
# by Chris Huffman 2017


def BMR(weight, height, age, gender):
    if gender == 'f':
        yourBMR = 655 + f_weight + f_height - f_age
        return yourBMR
    if gender == 'm':
        yourBMR = 66 + m_weight + m_height - m_age
        return yourBMR




print ("Please enter your name:  ")
name = input()
print ("Hello " + name + ".  This program will calculate your BMR.\n")
print ("First I need to collect some of your biological information.\n")

print ("Please enter your gender:  (m) or (f)")
gender = input()

print ("Thanks.  Now please enter your weight in pounds:  ")
input_weight = float(input())
m_weight = input_weight * 6.23
f_weight = input_weight * 4.35

print ("Cool.  Could I get your age in years?:  ")
input_age = float(input())
m_age = input_age * 6.8
f_age = input_age * 4.7

print ("Great.  One last thing.\n")
print ("Please enter your height round down to the nearest foot (example - 6'8 = 6:  ")
feet_height = float(input())
print ("Now enter the remaining inches that you rounded down:  ")
inches = float(input())
input_height = (feet_height * 12) + inches
m_height = input_height * 12.7
f_height = input_height * 4.7

print ("Great!  That's everything.\n")
print ("Your BMR is....\n\n")
yourBMR = BMR(input_weight, input_height, input_age, gender)
print ("%.2f" % yourBMR)

print ("This number represents the amount of calories you can consume in a day and not theoretically gain or lose weight.\n")
print ("Keep in mind that exercise and other daily activities can increase this number.")




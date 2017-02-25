

#BMI Calculator in Python
#  by Chris Huffman (2017)


########################################################################################################################
########################################################################################################################
#calculate BMI using height and weight
def BMI(metric_height, weight,):
        yourBMI = (weight / (metric_height * metric_height))
        return yourBMI

#provide feedback according to gender and BMI
def feedback(yourBMI):
    if yourBMI < 18.5:
        print ("Your BMI is insanely low.  You should probably be dead.")
    if 18.50 <= yourBMI <= 24.99:
        print ("You have a normal BMI for your gender.")
    if 25.00 <= yourBMI <= 29.9:
        print ("Your BMI is a bit high.  It's ok, you're working hard to fix that! ")
    if 30.00 <= yourBMI <= 39.99:
        print ("You are obese.")
    if yourBMI >= 40.00:
        print ("You are morbidly obese.  Please seek medical assistance immediately. ")

########################################################################################################################
########################################################################################################################

#gather name and provide greeting
print ("Please enter your name: ")
name = input()
print ("Hello, " + name + ".  This is a BMI calculator." + "\n" + "\n")

#gather gender data
print (name + "," + " please provide your gender." + "\n" + "'f' for female" + "\n" + "'m' for male :  ")
gender = input()

#gather weight data
print ("Thank you.\n" + "Please enter your weight in pounds :  ")
input_weight = int(input())
weight = input_weight * .45

#gather height data
print ("Thanks.  One last thing.\n" + "Please enter your height in feet rounded down to the nearest foot :  ")
feet = int(input())
print ("Ok, now enter the inches that you rounded down [ 0 - 11 ] :  ")
inches = int(input())

#calculate height in inches
height = int(feet * 12) + inches
metric_height = height * .025

#provide BMI to user
print ("Great!  That's everything.\n\n")
print ("Your BMI is...\n")
yourBMI = BMI(metric_height, weight)
print ("%.2f" % yourBMI)

#provide feedback specific to gender and BMI
print (feedback(yourBMI))

########################################################################################################################
########################################################################################################################








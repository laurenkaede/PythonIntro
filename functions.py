#------------------------------------------------------------------------------------------------------------------#

# Activity 1:

# age = 60

# if age < 18:
#     print ("Child ticket price is £8.")

# elif age < 60:
#     print ("Adult ticket price is £10.95.")

# else:
#     print ("Senior ticket price is £7.50.")


#------------------------------------------------------------------------------------------------------------------#

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~                      Functions                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Example:

# def press_grind_beans():
#     print("Grinding for 20 seconds")

# press_grind_beans()

#                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                               #

# Activity 2: Create a function that takes two parameters for a coffee order (size, type of drink) and prints them out in a sentence

# def coffee_order(size, type):     
#     print("I'd like a {} sized {} please.".format (size, type))

# coffee_order("medium","hot chocolate")
# coffee_order("small","tea")
# coffee_order("large","coffee")


#------------------------------------------------------------------------------------------------------------------#

# Activity 3: Here's an example of a function that includes a parameter. Parameters are responsible for functions being able to work on different data inputs. Edit the snippet below to include two parameters.

# def take_order(topping):     
#     print('Pizza with {}'.format(topping)) 

# take_order(“pineapple")


# Mine:

# def take_order(topping1,topping2):     
#     print('Pizza with {} and {}.'.format(topping1,topping2)) 

# take_order("pineapple","ham")
# take_order("pepperoni","peppers")
# take_order("chicken","sweetcorn")


#------------------------------------------------------------------------------------------------------------------#

# Activity 4: Cash machine time. Let’s create one that:
 
# } Takes an input of pin number and amount  
# } Prints dispensing cash if the pin number is correct and there’s enough money to withdraw  
# } Displays the new bank balance 
# Be creative!


# bank_balance = 120
# pin_num_correct = 1234


# def withdraw_cash(pin_num,cash_amount):  

#     new_balance = bank_balance - cash_amount
#     if bank_balance >= cash_amount and pin_num == pin_num_correct: 
#         print("Here's your £{} cash withdrawal from your account. Your new balance is £{}.".format(cash_amount,new_balance))   
#     else:         
#         print("Either your pin number was incorrect, or you do not have enough money for a cash withdrawal.")

# withdraw_cash(1234,60)    
# withdraw_cash(1234,120)
# withdraw_cash(4321,60)   

#------------------------------------------------------------------------------------------------------------------#

# num1 = 8
# num2 = 6

# def multiply(num1,num2):
#     return num1 * num2

# print(multiply(num1,num2))


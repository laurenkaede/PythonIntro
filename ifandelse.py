# Activity 1: Create a variable called age. Write an if statement that logs “Yes I can serve you” if age is greater than 17 and else logs “You aren’t old enough”.

# age = 9
# age_limit = 17
# if age > age_limit:
#     print("Yes I can serve you.")
# else:
#     print("You aren't old enough.")

# age = 17  
# age_limit = 17
# if age > age_limit:
#     print("Yes I can serve you.")
# else:
#     print("You aren't old enough.")

# age = 29
# age_limit = 17
# if age > age_limit:
#     print("Yes I can serve you.")
# else:
#     print("You are not old enough.")

#------------------------------------------------------------------------------------------------------------------#

# Activity 2: Take your if statement and add a variable called country. Now check if age > 17 and country == “UK”

# age = 19
# age_limit = 17
# country = "UK"
# if age > age_limit and country == "UK":
#     print("Yes I can serve you.")
# else:
#     print("You aren't old enough.")

# age = 19
# age_limit = 17
# country = "USA"
# if age > age_limit and country == "UK":
#     print("Yes I can serve you.")
# else:
#     print("You aren't old enough.")

#------------------------------------------------------------------------------------------------------------------#

# Challenge 1: Create a variable called password. Check how many letters are in the password, if there are less than 8 print that the password is too short. Otherwise print the password.


# password = ("codenation")
# password_len = len(password)

# if password_len >= 7:
#     print(password)
# else:
#     print("The password is too short.")

# password = ("code")
# password_len = len(password)

# if password_len >= 7:
#     print(password)
# else:
#     print("The password is too short.")

#------------------------------------------------------------------------------------------------------------------#

# Challenge 2: Create a variable called num. Check if the variable is divisible by 3 or 5. If it is print “This number is divisible by 3 or 5”. Otherwise print “This number is not divisible by 3 or 5”.


# number = 15
# div_number_3 = number / 3
# div_number_5 = number / 5

# if (div_number_3).is_integer() or (div_number_5).is_integer():
#     print("This number is divisible by 3 or 5.")
# else:
#     print("This number is not divisible by 3 or 5.")


# number = 8
# div_number_3 = number / 3
# div_number_5 = number / 5

# if (div_number_3).is_integer() or (div_number_5).is_integer():
#     print("This number is divisible by 3 or 5.")
# else:
#     print("This number is not divisible by 3 or 5.")

#------------------------------------------------------------------------------------------------------------------#

# Challenge 3: Create a variable called num. If num is divisible by 3 print “fizz”, if it’s divisible by 5 print “buzz”, if it’s divisible by both 3 and 5 print “fizz buzz”. Otherwise print num.

# num = 7
# div_number_3 = num / 3
# div_number_5 = num / 5

# if (div_number_3).is_integer() and (div_number_5).is_integer():
#     print("fizz buzz")
# elif (div_number_5).is_integer():
#     print("buzz")
# elif (div_number_3).is_integer():
#     print("fizz")
# else:
#     print("This number is not divisible by 3 or 5.")

#------------------------------------------------------------------------------------------------------------------#

# Challenge 4: Create a variable called num. Check if the number is a palindrome (looks the same forward as it does backwards e.g. 1001 or 20202).

# num = ("202")
# val = int(num)
# if num == str(num)[::-1]:
#     print('This number is a palindrome.')
# else:
#     print('This number is not a palindrome.')


#------------------------------------------------------------------------------------------------------------------#

# Challenge 5: Create a variable called time, a variable called place_of_work and a variable called town_of_home. Create an if statement that prints where someone is at times of the day. E.g. if the time is 7 I’m at home, at 8 I’m commuting, at 9 I’m at work.

 
# time = 19
# travelling = ("commuting for work")
# place_of_work = ("Codenation")
# place_of_home = ("Urmston")
 
# if time >= 9 and time < 17.30:
#     print("I am at {}.".format(place_of_work))
 
# elif time >= 7 and time < 9:
#     print("I am {}.".format(travelling))
 
# elif time >= 17.30 and time < 19:
#     print("I am at {}.".format(travelling))
 
# elif time >= 19 and time <= 23:
#     print("I am at {}.".format(place_of_home))
 
# elif time >= 00 and time < 7:
#     print("I am at {}.".format(place_of_home))


#-------------------------------------------------------------------------------------------------------------#
 
# Challenge 6: Create two variables called num1 and num2. Create an if statement that checks if the result of the sum is even. If it is return a success message.
 
# num1 = 5
# num2 = 5
# num_sum = num1 + num2
# if num_sum % 2 == 0:
#     print("{0} is an Even number.".format(num_sum)) 
# else:
#     print("{0} is an Odd number.".format(num_sum)) 


#------------------------------------------------------------------------------------------------------------------#

# Challenge 7: Take the string “jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuh gtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi”. Find the index of a last vowel in the string.
 
# test_string = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"
# last_vowel = 0
# this_vowel = 0
# this_vowel = test_string.rfind("a")
# if this_vowel > last_vowel:
#     last_vowel = this_vowel
# this_vowel = test_string.rfind("e")
# if this_vowel > last_vowel:
#     last_vowel = this_vowel
# this_vowel = test_string.rfind("i")
# if this_vowel > last_vowel:
#     last_vowel = this_vowel
# this_vowel = test_string.rfind("o")
# if this_vowel > last_vowel:
#     last_vowel = this_vowel
# this_vowel = test_string.rfind("u")
# if this_vowel > last_vowel:
#     last_vowel = this_vowel
# print(last_vowel)
 

#------------------------------------------------------------------------------------------------------------------#

# Challenge 8: Create a variable called word that takes a string. Create an if statement that checks if the last letter is the same as the first. If it is return true, otherwise return false.
 
word = "eligible"
if word[0] == word[-1]:
    print("True.")
else:
    print("False.")


#------------------------------------------------------------------------------------------------------------------#


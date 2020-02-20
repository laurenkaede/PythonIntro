#~~~~~~~~~~~                                       Dot Notation                                         ~~~~~~~~~~~#
            #-------------------------------------------------------------------------------------------#


# Learning Objectives • To understand dot notation • To understand different data types • To use VS code to create simple programs


            #-------------------------------------------------------------------------------------------#

#~~~# To print a string #~~~#

# print("Hello world.")

            #-------------------------------------------------------------------------------------------#

#~~~# To print the number of characters in a string #~~~#

# print(len("Hello World."))

            #-------------------------------------------------------------------------------------------#

#~~~# To print the string text in all uppercase #~~~#

# print("Hello World.".upper())

            #-------------------------------------------------------------------------------------------#

#~~~# To print and convert the first character of a string to a capital letter #~~~#

# print("hello world.".capitalize())

            #-------------------------------------------------------------------------------------------#

#~~~# To print the number of occurences of a substring in the given string. #~~~#

# print("hello world".count("Hello"))

            #-------------------------------------------------------------------------------------------#

#~~~# To print (and) .find() method returns the lowest index of the substring if it's found in a given string. If it's not found then it returns -1. E.G. Hello - lowest index is 'H' and so returns a value of '0'. world - lowest index is 'w' and so returns a value of '6'.

# print("hello world".find("hello"))
# print("hello world".find("world"))

            #-------------------------------------------------------------------------------------------#

#~~~# To print (and) .replace() method returns a copy of the string where all occurances of a substring is replaced with another substring.

# print("Hello World.".replace("World.", "Lauren."))

            #-------------------------------------------------------------------------------------------#

#~~~# Prints the index position. Index position starts from '0'.

# print("Hello"[2]) - # This will print the letter 'L'
# print("Hello"[4]) - # This will print the letter 'O'

            #-------------------------------------------------------------------------------------------#

#~~~# Prints and creates a random number between the two given parameters. Second value must always be higher than the first value.

# import random   # <--- Important to include at top of code.
# print(random.randint(1,10))

            #-------------------------------------------------------------------------------------------#

#~~~# Prints the 7th character (with a count starting from 0).

# print('All Around the World'[7].upper())

            #-------------------------------------------------------------------------------------------#

#} random is a library in python } randint is a method in random } randint takes two parameters an upper and a lower bound

# print(random.randint(1,10))  # <--- This is dot notation.





            #-------------------------------------------------------------------------------------------#
#~~~~~~~~~~~                                        Variables                                           ~~~~~~~~~~~#
            #-------------------------------------------------------------------------------------------#

# Learning Objectives • To understand how variable works in Python • To understand and use operators to store values and do calculations • To use snake_case when naming variables • To understand how to access data in variable

            #-------------------------------------------------------------------------------------------#

# 1) allow us to store data inside them
# 2) access them via a name 
# 3) then place new data in them whenever we want

            #-------------------------------------------------------------------------------------------#

# my_name = "Lauren"  # <--- This is a variable, named using snake_case.


# favourite_drink = "Coke Zero"
# drink_adjective = "awesome"

# print("My favourite drink is " + favourite_drink + " because it is " + drink_adjective +".")
# print("My favourite drink is {} because it is {}.".format(favourite_drink, drink_adjective))

            #-------------------------------------------------------------------------------------------#

# Assignment Operators:

# = (assign a variable), *= (assign and multiply), += (assign and addition), /= (assign and divide), -= (assign and subtract), == (equals), != (doesn't equal).




            #-------------------------------------------------------------------------------------------#
#~~~~~~~~~~~                                         If Else                                            ~~~~~~~~~~~#
            #-------------------------------------------------------------------------------------------#

# Learning Objectives • To understand if/else and switch syntax • To understand and use comparison operators • To write programs with single condition • To write programs with multiple conditions

            #-------------------------------------------------------------------------------------------#

# if condition1:     
#   #do this 
# elif condition2:     
#   #do this 
# else:    
#   #if nothing else matched do this

#^^^ an if/else statement.

            #-------------------------------------------------------------------------------------------#

# Example 1:

# age = 19
# age_limit = 17
# country = "USA"
# if age > age_limit and country == "UK":
#     print("Yes I can serve you.")
# else:
#     print("You aren't old enough.")

            #-------------------------------------------------------------------------------------------#

# Example 2:

# Create a variable called word that takes a string. Create an if statement that checks if the last letter is the same as the first. If it is return true, otherwise return false.
 
# word = "eligible"
# if word[0] == word[-1]:
#     print("True.")
# else:
#     print("False.")


## 0 = 1st character  and  -1 = last character



            #-------------------------------------------------------------------------------------------#
#~~~~~~~~~~~                                        Functions                                           ~~~~~~~~~~~#
            #-------------------------------------------------------------------------------------------#

# Learning Objectives • To understand how functions work • To write programs with functions • To write programs with all three types of functions

            #-------------------------------------------------------------------------------------------#

#Functions are written to perform a task. Functions take data, perform a set of tasks on the data, and then return the result.  We can define parameters to be used when calling the function. When calling a function, we can pass in arguments, which will set the function's parameters. We can use return to return the result of a function which allows us to call functions anywhere, even inside other functions.

            #-------------------------------------------------------------------------------------------#

# Example 1:

# def press_grind_beans():
#     print("Grinding for 20 seconds")

# press_grind_beans()


            #-------------------------------------------------------------------------------------------#

# Example 2:

# coffee_is_grinding = False 

# def press_grind_beans():     
#   if coffee_is_grinding:         
#       print(‘The coffee is grinding’)     
#   else:         
#       print(‘The coffee is not grinding’) 

# press_grind_beans()

            #-------------------------------------------------------------------------------------------#

# Example 3:

# def take_order(topping1,topping2):     
#     print('Pizza with {} and {}.'.format(topping1,topping2)) 

# take_order("pineapple","ham")
# take_order("pepperoni","peppers")
# take_order("chicken","sweetcorn")

            #-------------------------------------------------------------------------------------------#

# Example 4: Cash machine time. Let’s create one that:
 
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




            #-------------------------------------------------------------------------------------------#
#~~~~~~~~~~~                                          Lists                                             ~~~~~~~~~~~#
            #-------------------------------------------------------------------------------------------#

# Learning Objectives • To understand the uses of lists • To understand the syntax of creating an lists • To use a variety of methods to work with lists.


             #-------------------------------------------------------------------------------------------#

# Examples of various methods - Find an item on a list using index position, swap item on list, number of items on list, add item to list, and remove last item on list.


# favourite_songs = [
#     "Here Comes The Sun",
#     "The Voice Within'",
#     "Numb"
# ]

# print(favourite_songs)

# print(favourite_songs[2]) # Prints the 3rd song on the list as Python starts with 0 to count index position.

# favourite_songs[1] ="Warrior" # Swaps an item on your list to a new item.

# print(len(favourite_songs)) # Prints the number of songs on the list.

# favourite_songs.append("Bohemian Rhapsody")
# print(favourite_songs) # .append allows you to add another item to your list.

# favourite_songs.pop()
# print(favourite_songs) # .pop allows you to remove the last item on your list.

            #-------------------------------------------------------------------------------------------#

# The following methods include: remove(), reverse(), sort(), count(), extend(), clear()


# favourite_songs = [
#     "Here Comes The Sun",
#     "The Voice Within'",
#     "Numb",
#     "Comfortably Numb"
# ]

# print(favourite_songs)

# .remove() - Removes a given item from the list. Can omly remove one item from the list at a time. 

# favourite_songs.remove("The Voice Within'")
# print(favourite_songs)



# .reverse() - The reverse() function doesn't return any value. It only reverses the elements and updates the list.

# favourite_songs.reverse()
# print(favourite_songs)



# .sort() - The sort() method sorts the elements of a given list in a specific order - Ascending or Descending. Alphabetical or numerical. If both string and integers used, then integers are sorted first.

# favourite_songs.sort()
# print(favourite_songs)



# .count() - In simple terms, count() method counts how many times an element has occurred in a list and returns it.

# favourite_songs.count("Numb")
# print(favourite_songs.count("Numb"))

# favourite_songs.count("Comfortably Numb")
# print(favourite_songs.count("Comfortably Numb"))




# .extend() - The extend() extends the list by adding all items of a list (passed as an argument) to the end.

# favourite_songs1 = [
#     "La La",
#     "Hold Back The River"
# ]

# favourite_songs.extend(favourite_songs1)
# print(favourite_songs)



# .clear() - The clear() method removes all items from the list.

# favourite_songs.clear()
# print(favourite_songs)


            #-------------------------------------------------------------------------------------------#
#~~~~~~~~~~~                                          Loops                                             ~~~~~~~~~~~#
            #-------------------------------------------------------------------------------------------#

# Learning Objectives • To understand the uses of a for loop • To write programs using for loops

            #-------------------------------------------------------------------------------------------#


# Example:

# favorite_drinks = ["Wine", "Gin", "Water"] 

# for drink in favorite_drinks:     
#    print(drink)

                 #-------------------------------------------------------------------------------------------#


# Activity 2. Create a list with 3 values and then add another to the start of the list using a method.

# favourite_songs = [
#     "Here Comes The Sun",
#     "The Voice Within'",
#     "Numb"
# ]
# print(favourite_songs)

# favourite_songs.insert(0, "Roar")  

# .insert (inserts an item to a list) '0' is the position in which the item is added to the list. So '0' would be the start of the list.

# print(favourite_songs)

# for soundtrack in favourite_songs:   
#     print(soundtrack)

#------------------------------------------------------------------------------------------------------------------#

# Activity 3 - Generate 6 random numbers between 1-50.

# import random 
# for i in range(6):     
#     print(random.randint(1,50))


#------------------------------------------------------------------------------------------------------------------#

# Actvity 4 - If we can create a loop to put 0-9 on the screen, how can we count from 9 to 0?

# for i in range(9, -1, -1):     
#     print(i)


#------------------------------------------------------------------------------------------------------------------#

# Activity 5 - Create an array that lists your favourite films, up to 5 elements. Add 2 more using a method. Use a loop to cycle through the array.

# favourite_films = [
#     "Infinity Wars",
#     "Inception",
#     "The Greatest Showman",
#     "The Lucky Ones",
#     "Ready Player One"
# ]
# print(favourite_films)

# favourite_films.append("Cinderella")
# favourite_films.append("Shutter Island")

# print(favourite_films)

# for movies in favourite_films:   # a for loop will loop through our list and extract everything individually.
#     print(movies)


#------------------------------------------------------------------------------------------------------------------#

# Activity 6 - Displays 4 films stored in an array. Use a loop to show each film in the array. Create a function called film_check() that checks if the 3rd film in the array is Ghostbusters. If it is, it should return “yey it’s ghostbusters”. If it isn’t, it should return “booo, we want ghostbusters."


# favourite_films = [
#     "Infinity Wars",
#     "Inception",
#     "Ghostbusters",
#     "Ready Player One"
# ]

# for movies in favourite_films:   
#      print(movies)


# def film_check(movies):
#     if favourite_films[2] == "Ghostbusters":
#         print("Yey, it's Ghostbusters!")
#     else:
#         print("Booo, we want Ghostbusters!")

# film_check("Ghostbusters") 

#------------------------------------------------------------------------------------------------------------------#
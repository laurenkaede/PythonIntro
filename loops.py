#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    Loops    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Activity 1. Create a function for a sub sandwich order: 5 toppings.

# def sandwich_order(topping1,topping2,topping3,topping4,topping5):     
#     print('Sub sandwich with {}, {}, {}, {} and {} please.'.format(topping1,topping2,topping3,topping4,topping5)) 

# sandwich_order("chicken","bacon","lettuce","tomato","sweetcorn")
# sandwich_order("cheese","ham","peppers","cucumber","onion")
# sandwich_order("chicken","sweetcorn","meatballs","tomato","pulled pork")


#------------------------------------------------------------------------------------------------------------------#

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


favourite_films = [
    "Infinity Wars",
    "Inception",
    "Ghostbusters",
    "Ready Player One"
]

for movies in favourite_films:   
     print(movies)


# def film_check(movies):
#     if favourite_films[2] == "Ghostbusters":
#         print("Yey, it's Ghostbusters!")
#     else:
#         print("Booo, we want Ghostbusters!")

# film_check("Ghostbusters") 

#------------------------------------------------------------------------------------------------------------------#
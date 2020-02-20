# Activity 1: Create a list of your favourite songs. Include 3 songs.

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

#---------------------------------------------------------------------------------------------------------------#

# Activity 2: Create a list of your favourite website (3 of them), and then add another two once you’ve created the list. Then remove the last website.

# favourite_websites = [
#     "www.netflix.com",
#     "www.youtube.com",
#     "www.amazon.co.uk"
# ]

# print(favourite_websites)

# favourite_websites.append("www.goodreads.com")
# print(favourite_websites) 

# favourite_websites.append("www.google.com")
# print(favourite_websites)

# favourite_websites.pop()
# print(favourite_websites) 


#------------------------------------------------------------------------------------------------------------------#

# Activity 3: Research on the following methods: remove(), reverse(), sort(), count(), extend() (and many more). Create a program to demonstrate the uses of each method, some of these you may need more than one example. (Pay attention: not all methods would permanently updates/make changes to the arrays themselves.)


favourite_songs = [
    "Here Comes The Sun",
    "The Voice Within'",
    "Numb",
    "Comfortably Numb"
]

# print(favourite_songs)

# .remove() - Removes a given item from the list. Can omly remove one item from the list at a time. 

# favourite_songs.remove("The Voice Within'")
# print(favourite_songs)



# .reverse() - The reverse() function doesn't return any value. It only reverses the elements and updates the list.

# favourite_songs.reverse()
# print(favourite_songs)



# .sort() - The sort() method sorts the elements of a given list in a specific order - Ascending or Descending. Alphabetical or numerical.

# favourite_songs.sort()
# print(favourite_songs)



# .count() - In simple terms, count() method counts how many times an element has occurred in a list and returns it.

# favourite_songs.count("Numb")
# print(favourite_songs.count("Numb"))

# favourite_songs.count("Comfortably Numb")
# print(favourite_songs.count("Comfortably Numb"))




# .extend() - The extend() extends the list by adding all items of a list (passed as an argument) to the end.

favourite_songs1 = [
    "La La",
    "Hold Back The River"
]

favourite_songs.extend(favourite_songs1)
print(favourite_songs)



# .clear() - The clear() method removes all items from the list.

# favourite_songs.clear()
# print(favourite_songs)


#------------------------------------------------------------------------------------------------------------------#
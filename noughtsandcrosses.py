space_one = "X"
space_two = "O"
space_three = " "
space_four = "X"
space_five = "X"
space_six = " "
space_seven = "O"
space_eight = " "
space_nine = " "
crosses = "X"
noughts = "O"

# print("        |         |        ")
# print("   {}    |    {}    |   {}   ".format(space_one, space_two, space_three))
# print("        |         |        ")
# print("- - - - - - - - - - - - - - ")
# print("        |         |        ")
# print("   {}    |    {}    |   {}   ".format(space_four, space_five, space_six))
# print("        |         |        ")
# print("- - - - - - - - - - - - - - ")
# print("        |         |        ")
# print("   {}    |    {}    |   {}   ".format(space_seven, space_eight, space_nine))
# print("        |         |        ")

# Activity 1 - Write an if statement that checks if the items on the top row meet a winning condition.So the top rows are all 'x's or 'o's.

if space_one == crosses and space_two == crosses and space_three == crosses:
    print("Congratulations Crosses, you've won!")

elif space_one == noughts and space_two == noughts and space_three == noughts:
    print("Congratulations Noughts, you've won!")

elif space_one == noughts and space_two == noughts and space_three == crosses:
    print("You've lost!")

elif space_one == noughts and space_two == crosses and space_three == crosses:
    print("You've lost!")

elif space_one == noughts and space_two == crosses and space_three == noughts:
    print("You've lost!")

elif space_one == crosses and space_two == noughts and space_three == crosses:
    print("You've lost!")

elif space_one == crosses and space_two == crosses and space_three == noughts:
    print("You've lost!")

elif space_one == crosses and space_two == noughts and space_three == noughts:
    print("You've lost!")

else:
    print("Try again!")
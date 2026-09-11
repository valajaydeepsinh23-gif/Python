# 1. string

movie = "The Bad Guys"

main_character = "Mr. Wolf"

print("movie name data type", type(movie))

print("main character", main_character)

print("main character data type", type(main_character))


# 2. integer

whole_number = 10

print("number", whole_number)

print("number data type", type(whole_number))


# 3. float

decimal_number = 10.5

print("number", decimal_number)

print("number data type", type(decimal_number))


# 4. boolean

islogged_in = True

print("is user logged in", islogged_in)

print("is user logged data type", type(islogged_in))

verified = False

print("is user account verified", verified)

print("verified data type", type(verified))



# 5. list => mutable => can be changed

fruits = ["apple", "banana", "orange"]

print("fruits items", fruits)

print("fruits data type", type(fruits))

fruits[0] = "dragon fruit"

print("fruits items after", fruits)

print("fruits data type", type(fruits))


# 6. tuple => immutable => cannot be changed

vegetables = ("cucumber", "red chili", "tomato")

print("vegetables before", vegetables)

# vegetables[0] = "corn"

print("vegetables after", vegetables)

print("vegetables data type", type(vegetables))


# 7. list => mutable => can be changed

colors = ["red", "green", "blue"]

print("colors items", colors)

print("colors data type", type(colors))

colors[0] = "yellow"

print("colors items after", colors)

print("colors data type", type(colors))
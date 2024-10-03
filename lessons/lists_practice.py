"""Playing around with lists"""

my_numbers: list[float] = []  # literal version
my_numbers: list[float] = list()  # constructor version

print(my_numbers)

my_numbers.append(1.5)

print(my_numbers)

game_points: list[int] = [102, 86, 94]

print(game_points[1])
print(
    game_points[len(game_points) - 1]
)  # another way if u want to get the last point of a list

game_points[1] = 72
print(game_points[1])
print(len(game_points))
print(game_points)
game_points.pop(1)
print(game_points)

# can we change individual chars in strings this way?
my_name: str = "Izzi"
print(my_name)
# my_name[3] = "y" # didn't work! Converting to list instead

name_as_list: list[str] = list(my_name)
print(name_as_list)
name_as_list[3] = "y"
print(name_as_list)
name_as_list.append("i")
print(name_as_list)

name_as_list.insert(2, "h")
print(name_as_list)
name_as_list.pop(2)
print(name_as_list)

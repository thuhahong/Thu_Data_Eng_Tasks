def direction():
    forwards_backwards = input("Which direction do you want to go? (FORWARDS/BACKWARDS)").lower()
    direction_counter = 0
    if forwards_backwards == "forwards":
        direction_counter += 1
    elif forwards_backwards == "backwards":
        direction_counter -= 1
    return direction_counter


print(direction())


def turn():
    left_right = input("Which way? (LEFT/RIGHT)").lower()
    turn_counter = 0
    if left_right == "right":
        turn_counter += 1
    elif left_right == "left":
        turn_counter -= 1
    return turn_counter


print(turn())


def speed():
    mph = input("How many mph? Choose a number from 1 - 100.")
    return mph


print(speed() + 'mph')

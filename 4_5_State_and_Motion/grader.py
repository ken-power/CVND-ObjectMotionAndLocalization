import numpy as np

import car
import color


def check_vals(value1, value2):
    return value1 == value2


def test_two_colors(c1, c2):
    '''
    Feed in the rgb values of color one,
    then the rgb values of color two (as lists).
    Adds these two together.
    '''
    color1 = color.Color(c1[0], c1[1], c1[2])
    color2 = color.Color(c2[0], c2[1], c2[2])
    new_color = color1 + color2

    return (check_vals(new_color.r, (color1.r + color2.r) / 2) and
            check_vals(new_color.g, (color1.g + color2.g) / 2) and
            check_vals(new_color.b, (color1.b + color2.b) / 2))


def test_add_colors():
    if (test_two_colors([250, 0, 0], [0, 50, 200]) and
            test_two_colors([180, 70, 30], [10, 20, 250])):
        print('Nice work! Your colors add as expected.')
    else:
        print('Oops! Something went wrong. Make sure you are averaging the colors.')


def test_one():
    '''
    Simple test case with little movement.
    '''
    # Create a 2D world of 0's
    height = 4
    width = 6
    world = np.zeros((height, width))

    # Define the initial car state
    initial_position = [0, 0]  # [y, x] (top-left corner)
    velocity = [0, 1]  # [vy, vx] (moving to the right)

    # Create a car with initial params
    carla = car.Car(initial_position, velocity, world)

    carla.move()
    carla.move()
    carla.turn_right()
    carla.move()

    if carla.state == [[1, 2], [1, 0]]:
        return True
    else:
        return False


def test_two():
    '''
    More advanced case going off of the map.
    '''
    # Create a 2D world of 0's
    height = 4
    width = 6
    world = np.zeros((height, width))

    # Define the initial car state
    initial_position = [0, 0]  # [y, x] (top-left corner)
    velocity = [0, 1]  # [vy, vx] (moving to the right)

    # Create a car with initial params
    carla = car.Car(initial_position, velocity, world)

    carla.move()
    carla.move()
    carla.turn_right()
    carla.move()
    carla.move()
    carla.turn_left()
    for i in range(4):
        carla.move()

    if carla.state == [[2, 0], [0, 1]]:
        return True
    else:
        return False


def test_three():
    '''
    Check when using a different initial position, velocity and world.
    '''
    # Create a 2D world of 0's
    height = 6
    width = 8
    world = np.zeros((height, width))

    # Define the initial car state
    initial_position = [4, 5]  # [y, x]
    velocity = [1, 0]  # [vy, vx]

    # Create a car with initial params
    carla = car.Car(initial_position, velocity, world)

    carla.turn_right()
    carla.move()
    carla.move()
    carla.turn_right()
    for i in range(10):
        carla.move()

    if carla.state == [[0, 3], [-1, 0]]:
        return True
    else:
        return False


def test_turn_right():
    if test_one() == True and test_two() == True and test_three() == True:
        print("Nice work! Your turn_right() function behaves as expected.")
    else:
        print("Oops! Something went wrong. Double-check your implementation.")

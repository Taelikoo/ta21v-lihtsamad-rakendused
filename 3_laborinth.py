import random


map = [
    [12, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 24],
]

start_pos_x = 0 
start_pos_y = 0

y_rows = 5
x_columns = 5

def get_next_free_position(current_position_y, current_position_x):
    random_number = random.random()

    can_go_right = current_position_x+1 < x_columns and map[current_position_y][current_position_x+1] == 1
    can_go_left = current_position_x-1 > 0 and map[current_position_y][current_position_x-1] == 1
    can_go_bottom = current_position_y+1 < y_rows and map[current_position_y+1][current_position_x] == 1
    can_go_top = current_position_y-1 > 0 and map[current_position_y-1][current_position_x] == 1

    finish_on_right = current_position_x+1 < x_columns and map[current_position_y][current_position_x+1] == 24
    inish_on_right = current_position_x-1 > 0 and map[current_position_y][current_position_x-1] == 24
    finish_on_bottom = current_position_y+1 < y_rows and map[current_position_y+1][current_position_x] == 24
    finish_on_top = current_position_y-1 > 0 and map[current_position_y-1][current_position_x] == 24

    avaiabel_next_positions = []

    if can_go_right:
        print("can go right")
        position_on_right [current_position_y, current_position_x+1]
        available_next_positions.append(position_on_right)

    if can_go_left:
        print("can go left")
        position_on_left [current_position_y, current_position_x-1]
        available_next_positions.append(position_on_left)

    if can_go_bottom:
        print("can go bottom")
        position_on_bottom [current_position_y+1, current_position_x]
        available_next_positions.append(position_on_bottom)

    if can_go_top:
        print("can go top")
        position_on_top [current_position_y-1, current_position_x]
        available_next_positions.append(position_on_top)

next_free_position = get_next_free_position(start_pos_y, start_pos_x)
print("Next free position is: ", next_free_position)

while next_free_position:
    print("Next free position is: ", next_free_position)
    next_free_position = get_next_free_position(next_free_position[0], next_free_position[1])

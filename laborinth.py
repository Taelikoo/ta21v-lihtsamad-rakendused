map = [
    [12, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [24, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
]

start_pos_x = 0
start_pos_y = 0

y_rows = 5
x_columns = 5

def get_next_free_position(current_position_y, current_position_x):
    if current_position_x + 1 < x_columns and map[current_position_y][current_position_x + 1] == 1:
        print("can go right")
        return [current_position_y, current_position_x + 1]

def get_next_free_position(current_position_y, current_position_x):
    if current_position_x + 1 < x_columns and map[current_position_y][current_position_x - 1] == 1:
        print("can go left")
        return [current_position_y, current_position_x - 1]

    if current_position_y + 1 < y_rows and map[current_position_y + 1][current_position_x] == 1:
        print("can go bottom")
        return [current_position_y + 1, current_position_x]

    if current_position_y - 1 > 0 and map[current_position_y - 1][current_position_x] == 1:
        print("can go top")
        return [current_position_y - 1, current_position_x]
        
print("Next position is: ", next_pos)

while next_pos:
    print("Next position is: ", next_pos)
    next_pos = next_position(next_pos[0], next_pos[1])
    
import numpy as np
instructions = []
with open ('day12.txt') as input:
    lines = input.readlines()
    for line in lines:
        line = line.strip()
        instructions.append(line)


class angle:
    def __init__(self, angle_val):
        self.angle_val = angle_val
    def add_to_angle(self, value):
        angle_sum = self.angle_val + value
        if angle_sum >= 360:
            angle_sum = angle_sum - 360
        elif angle_sum < 0:
            angle_sum = angle_sum + 360
        self.angle_val = angle_sum
    def get_direction(self):
        angle_dict = {0:'W', 90:'N', 180:'E', 270:'S'}
        return angle_dict[self.angle_val]


def move_ship(instructions):
    init_coords = [0, 0]
    ship_angle = angle(180)
    cur_face = ship_angle.get_direction()
    for line in instructions:
        command = line[0]
        command_val = int(line[1:])
        if command in ['N', 'S', 'W', 'E']:
            init_coords = move_in_direction(command, command_val, init_coords)
        elif command == 'R':
            # pretty sure the rule maker mixed up left and right
            ship_angle.add_to_angle(command_val)
            cur_face = ship_angle.get_direction()
        elif command == 'L':
            ship_angle.add_to_angle(-command_val)
            cur_face = ship_angle.get_direction()
        elif command == 'F':
            init_coords = move_in_direction(cur_face, command_val, init_coords)
    return init_coords

def move_in_direction(direction, value, init_coords):
    if direction == 'N':
        init_coords[1] += value
    elif direction == 'S':
        init_coords[1] -= value
    elif direction == 'W':
        init_coords[0] += value
    elif direction == 'E':
        init_coords[0] -= value
    return init_coords

out_coords = move_ship(instructions)
manhattan = sum([abs(i) for i in out_coords])
print('manhattan distance part 1: ',manhattan)

### part 2 ###

def turn_waypoint(waypoint_coords, turn_angle, direction):
    coords_relative = waypoint_coords.copy()
    N_90s = int(turn_angle/90)
    for i in range(N_90s):
        a = coords_relative[0]
        b = coords_relative[1]
        if direction == 'R':
            coords_relative = np.array([-b, a])
        elif direction == 'L':
            coords_relative = np.array([b, -a])
    return coords_relative


def move_along_waypoint(instructions):
    waypoint_coords = np.array([-10, 1])
    ship_coords = np.array([0, 0])
    for line in instructions:
        command = line[0]
        command_val = int(line[1:])
        if command in ['N', 'S', 'W', 'E']:
            waypoint_coords = move_in_direction(command, command_val, waypoint_coords)
        elif command == 'R' or command == 'L':
            waypoint_coords = turn_waypoint(waypoint_coords, command_val, command)
        elif command == 'F':
            ship_coords += waypoint_coords * command_val
    return ship_coords

out_coords = move_along_waypoint(instructions)
manhattan = sum([abs(i) for i in out_coords])
print('manhattan distance with waypoint: ',manhattan)
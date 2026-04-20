def get_pos():
    return (get_pos_x(), get_pos_y())
    
def odd_pos():
    (x,y) = get_pos()
    if x % 2 != 0 and y % 2 != 0:
        return True
    else:
        return False

def is_odd(axis):
    if axis == "x":
        return get_pos_x() % 2 != 0
    elif axis == "y":
        return get_pos_y() % 2 != 0
    return False
    
def move_to(x, y):
    current_x, current_y = get_pos()
    dist_y = abs(current_y - y)
    dist_x = abs(current_x - x)
    if current_x > x:
        for x in range(dist_x):
            move(West)
    elif current_x < x:
        for x in range(dist_x):
            move(East)

    if current_y > y:
        for y in range(dist_y):
            move(South)
    elif current_y < y:
        for y in range(dist_y):
            move(North) 

def all(l) -> Bool:
    for i in l:
        if not i:
            return False
    return True

def pumpkin_ready(field):
    return all(field)
    
def coords_to_list(coords):
    pass
    
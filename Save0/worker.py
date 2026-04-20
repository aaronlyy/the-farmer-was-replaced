import util

def default(coords, func):
    for c in coords:
        for x in range(c["start"][0], c["stop"][0] + 1):
            for y in range(c["start"][1], c["stop"][1] + 1):
                
                util.move_to(x,y)
                func()
                
            util.move_to(x,y)
    
def columns(world_size, cols, func):
    util.move_to(cols["start"], 0)
    for x in range(cols["start"], cols["stop"] + 1):
        for y in range(world_size):
            func()
            move(North)
        move(East)
        
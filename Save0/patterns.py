import util

def default(coords, f):
    for c in coords:
        for x in range(c["start"][0], c["stop"][0] + 1):
            for y in range(c["start"][1], c["stop"][1] + 1):
                
                util.move_to(x,y)
                f()
                
            util.move_to(x,y)
            
def pumpkin(coords, f):
    for c in coords:
        for x in range(c["start"][0], c["stop"][0] + 1):
            for y in range(c["start"][1], c["stop"][1] + 1):
                
                util.move_to(x,y)
                
                f()
                
            util.move_to(x,y)
    return dead

def chessboard(coords, f1, f2):
    for c in coords:
        for x in range(c["start"][0], c["stop"][0] + 1):
            for y in range(c["start"][1], c["stop"][1] + 1):
                
                util.move_to(x,y)
                
                if util.is_odd("x") and not util.is_odd("y"):
                    f1()
                elif not util.is_odd("x") and util.is_odd("y"):
                    f1()
                else:
                    f2()
                
            util.move_to(x,y)
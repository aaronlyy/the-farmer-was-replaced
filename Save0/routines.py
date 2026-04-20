import util
import tasks

def default():
    if get_pos_x() < 4 and (util.is_odd("x") and not util.is_odd("y") or util.is_odd("y") and not util.is_odd("x")):
        tasks.tree()
        return
                
    if get_pos_x() < 4:
        tasks.carrot()
            
    if get_pos_x() >= 4:
        tasks.pumpkin()


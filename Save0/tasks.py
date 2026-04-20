def tree():
    if can_harvest():
        harvest()
        if get_water() <= 0.2:
            use_item(Items.Water)
        plant(Entities.Tree)

def carrot():
    if can_harvest():
        harvest()
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Carrot)
    
def pumpkin():
    if can_harvest():
        harvest()
    if get_ground_type() != Grounds.Soil:
        till()
    if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
        plant(Entities.Pumpkin)

def _harvest():
    harvest()

    
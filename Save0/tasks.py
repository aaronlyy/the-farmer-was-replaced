import patterns
import util


def _pumpkin():
    if get_ground_type() != Grounds.Soil:
        till()
    if get_entity_type() == Entities.Dead_Pumpkin or get_ground_type() == Grounds.Soil:
        plant(Entities.Pumpkin)

def _tree():
    if can_harvest():
        harvest()
        if get_water() <= 0.2:
            use_item(Items.Water)
        plant(Entities.Tree)

# how to plant a carrot
def _carrot():
    if can_harvest():
        harvest()
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Carrot)
        
         
def _harvest(coords):
    patterns.default(coords, harvest)
    
def carrots(coords):
    patterns.default(coords, _carrot)
    
def trees_and_carrots(coords):
    patterns.chessboard(coords, _tree, _carrot)
    
def big_pumpkin(coords):
    patterns.pumpkin(coords, _pumpkin)
        
    util.move_to(coords[0]["start"][0], coords[0]["start"][1])
    harvest()
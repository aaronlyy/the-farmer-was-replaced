import patterns
import util

def _hay():
    if can_harvest():
        harvest()
        
    if get_ground_type() == Grounds.Soil:
        till()


# returns True if pumpkin is ready to harvest
def _pumpkin() -> Bool:
    
    if get_ground_type() != Grounds.Soil:
        till()
    
    if get_entity_type() == Entities.Dead_Pumpkin or get_ground_type() == Grounds.Soil:
        plant(Entities.Pumpkin)
        
    return can_harvest()

def _tree():
    if can_harvest():
        harvest()
        
    if get_ground_type() == Grounds.Soil:
        till()
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

def _sunflower():
    if can_harvest():
        harvest()
    if get_ground_type() != Grounds.Soil:
        till()
    plant(Entities.Sunflower)
        

def hay(coords):
    patterns.default(coords, _hay)

def sunflower(coords):
    patterns.default(coords, _sunflower)

def full_harvest(coords):
    patterns.default(coords, harvest)
    
def carrots(coords):
    patterns.default(coords, _carrot)
    
def trees_and_carrots(coords):
    patterns.chessboard(coords, _tree, _carrot)
    
def big_pumpkin(coords):
    done = False
    field = []
    while not done:
        field = patterns.pumpkin(coords, _pumpkin, field)
        if len(field) == 0:
            done = True
    harvest()
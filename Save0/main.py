import util
import tasks
import worker

world_size = get_world_size()

clear()

tasks_columns = [
    {
        "func": tasks._harvest,
        "cols": {
            "start": 0,
            "stop": 3
        }
    },
    
    {    
        "func": tasks.pumpkin,
        "cols": {
            "start": 4,
            "stop": 7
        }
    }
]

tasks_coords = [
    {
        "func": tasks._harvest,
        "coords": [
            {
                "start": (0,0),
                "stop": (3,3)
            }
        ]
    },
    
    {    
        "func": tasks.pumpkin,
        "coords": [
            {
                "start": (0,4),
                "stop": (3,7)
            }
        ]
    },
    
    {
        "func": tasks.tree,
        "coords": [
            {
                "start": (4,0),
                "stop": (7,3)
            }
        ]
    },
    
    {
        "func": tasks.carrot,
        "coords": [
            {
                "start": (4,4),
                "stop": (7,7)
            }
        ]
    }
]


clear()


while True:
    for task in tasks_coords:
        worker.default(task["coords"], task["func"])
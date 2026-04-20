import tasks

default = [
    {
        "func": tasks.carrots,
        "coords": [
            {
                "start": (1,1),
                "stop": (2,2)
            }
        ]
    },
    {
        "func": tasks.trees_and_carrots,
        "coords": [
            {
                "start": (3,3),
                "stop": (4,4)
            }
        ]
    },
    {
        "func": tasks.big_pumpkin,
        "coords": [
            {
                "start": (8,0),
                "stop": (15,7)
            }
        ]
    }
]
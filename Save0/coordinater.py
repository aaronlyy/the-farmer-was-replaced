import util

def run(routines):
    while True:
        for routine in routines:
            for task in routine:
                task["func"](task["coords"])
        
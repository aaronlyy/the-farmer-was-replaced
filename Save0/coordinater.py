import util

def run(tasks):
    while True:
        for task in tasks:
            task["func"](task["coords"])
        
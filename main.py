import random

import system
import display
import inputs
from consts import *


def main():
    file = system.get_file()
    data = system.load_data(file)

    system.clear()
    
    while True:
        weightings = [(6-data.get(tech[0], 6)) + 2*tech[3] for tech in TECH]
        chosen_tech = random.choices(TECH, weightings, k=1)[0]
        
        score = data.get(chosen_tech[0], None)
        display.display_tech(chosen_tech, score)
        
        inp = inputs.option(">>>: ", VALID_INPUTS)

        system.clear()

        if inp in EXIT_STRINGS:
            break

        elif inp in SCORE:
            display.display_scores(weightings)
        
        elif inp in LIST_COMMANDS:
            display.display_data(data)

        elif inp in ASK_ALL:
            inputs.ask_all(data)
        
        elif inp != "":
            data[chosen_tech[0]] = int(inp)

    save_data(file, data)
        

if __name__ == "__main__":
    main()



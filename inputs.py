from consts import *
import system

def option(prompt: str, valid_inputs: list[str | None], lower_case_input=True) -> str | None:
    while True:
        try:
            inp = input(prompt)
            if lower_case_input:
                inp = inp.lower()
            
        except KeyboardInterrupt:
            inp = None
        
        if inp in valid_inputs:
            break
        
        print("Invalid input")
    
    return inp


def ask_all(data: dict[int]):
    for tech in TECH:
        system.clear()
        print("-" if tech[0] not in data else data[tech[0]], tech[0])
        inp = option("[0->5]: ", VALID_INPUTS)
        if inp not in NUMBERS:
            break

        data[tech[0]] = int(inp)
    system.clear()
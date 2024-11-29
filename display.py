from consts import *

def stars(n_stars: int) -> str:
    fill_star = "★"
    star = "☆"
    
    return "\t" + (fill_star*n_stars) + (star*(5 - n_stars)) + "\t" + str(n_stars)


def display_tech(tech: tuple[str, str, int, int, list[str]], score: int):
    print("Tech:\t\t\t" + tech[0])
    print()
    print("Difficulty:\t", stars(tech[2]))
    print("Usefulness:\t", stars(tech[3]))
    print("My Current Score:", None if score is None else stars(score))
    print("Links:")
    print(*tech[-1], sep="\n", end="\n\n")

def display_scores(weightings):
    for datum in sorted([(i, weightings[i]) for i in range(len(TECH))], reverse=True, key=lambda v: v[1]):
        print("{0: <3}".format(datum[1]), TECH[datum[0]][0])
    print()

def display_data(data: dict[int]):
    if len(data) == 0:
        print("No data to print")
    
    for name in data:
        print("{0: <64}".format(name), stars(data[name]))

    print()
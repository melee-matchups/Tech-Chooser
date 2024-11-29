# Marth Tech Chooser
A simple app to help with solo-practice with Marth
The app will choose a random tech, weighted by a number you give it, and by how useful it is.
Run `main.py` in a directory where files can be created

# Inputs:
- `list`, `lst`, `ls`, `l`
    > List the tech and your current level at them

- `exit`, `quit`, `q`, `e`, `[ctrl-c]`
    > Exit and saves data

- `ask`, `all`, `ask all`, `a`
    > Ask all levels for all tech, good for initially setting the tech levels

- `score`, `s`
    > Show current scores for each tech

- `0`
    > Rate the current chosen tech `I cannot do it`

- `1`
    > Rate the current chosen tech `I'm aware of the tech inputs, but can only do it once or twice`

- `2`
    > Rate the current chosen tech `I can do it, but not often`

- `3`
    > Rate the current chosen tech `I can often do it, but not consistently`

- `4`
    > Rate the current chosen tech `I can do it if I think about it`

- `5`
    > Rate the current chosen tech `I've mastered it`

- ` `
    > Leaving the input blank will clear the screen and choose another tech

# Command line arguments
The first command line argument is an option filename to the json file with the data in it
If this file is not specified, data is saved in `./data.json`

# Tech
To add/change tech, modify the variable `TECH` in `consts.py`

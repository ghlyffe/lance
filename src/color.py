BLACK = 0
MAGENTA = 1
PURPLE = 2
BLUE = 3
AZURE = 4
TURQUOISE = 5
GREEN = 6
YELLOW = 7
ORANGE = 8
RED = 9
WHITE = 10
UNKNOWN = -1

def col_to_string(col):
    if col == 0:
        return "Black"
    elif col == 1:
        return "Magenta"
    elif col == 2:
        return "Purple"
    elif col == 3:
        return "Blue"
    elif col == 4:
        return "Azure"
    elif col == 5:
        return "Turquoise"
    elif col == 6:
        return "Green"
    elif col == 7:
        return "Yellow"
    elif col == 8:
        return "Orange"
    elif col == 9:
        return "Red"
    elif col == 10:
        return "White"
    elif col == -1:
        return "Unknown"

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    manual = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            manual.append(f'{i * 5 + j} | {major} | {minor}')
    #return len(major_colors) * len(minor_colors)
    return manual


result = print_color_map()
assert(result[24] == '25 | Violet | Slate')
print("All is well (maybe!)\n")

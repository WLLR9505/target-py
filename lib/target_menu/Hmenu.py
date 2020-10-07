from lib.target_menu.colors import palette

def update(menu, control, cl):
    i = 0
    for i in range(len(menu)):
        if control["pos1"] == i:
            print(f"{cl[2]}{menu[i]}   {palette.colors[15][1]}")
        else:
            print(f"{menu[i]}")
    print("\n")
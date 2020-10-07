from lib.target_menu.colors import palette

def showFlex(menu, submenu, control, i, i2, cl):
    if i2 == control.getPos2():
        if i == control.getPos1(): # selecionados na mesma linha
            print(f"{cl[2]}{menu[i][0]}{palette.colors[15][1]}".ljust(27, ' '), end='')
            print(f"{cl[2]}{submenu[i2]}{palette.colors[15][1]}")
        else:
            print(f"{cl[2]}{menu[i][0] or ''}{palette.colors[15][1]}".ljust(19, ' '), end='')
            print(f"{cl[2]}{submenu[i2]}{palette.colors[15][1]}")
    elif i == control.getPos1():
        print(f"{cl[2]}{menu[i][0]}{palette.colors[15][1]}".ljust(27, ' '), end='')
        print(f"{cl[2]}{submenu[i2]}{palette.colors[15][1]}")
    else:
        print(f"{cl[2]}{menu[i][0] or ''}{palette.colors[15][1]}".ljust(15, ' '), end='')
        print(f"{cl[2]}{submenu[i2]}{palette.colors[15][1]}")

def showCommon(menu, submenu, control, i, i2, cl):
    if i2 == control.getPos2():
        if i == control.getPos1(): # selecionados na mesma linha
            print(f"{cl[2]}{menu[i]}{palette.colors[15][1]}".ljust(27, ' '), end='')
            print(f"{cl[2]}{submenu[i2]}{palette.colors[15][1]}")
        else:
            try:
                if not isinstance(menu[i], str):
                    raise Exception('is not a flexmenu')
                else:
                    print(f"{palette.colors[15][1]}{menu[i]}".ljust(19, ' '), end='')
            except:
                print(f"".ljust(15, ' '), end='')
            print(f"{cl[2]}{submenu[i2]}{palette.colors[15][1]}")



    elif i == control.getPos1():
        print(f"{cl[2]}{menu[i]}{palette.colors[15][1]}".ljust(27, ' '), end='')
        print(f"{submenu[i2]}")
    else:
        try:
            if not isinstance(menu[i], str):
                raise Exception('is not a flexmenu')
            else:
                print(f"{menu[i]}".ljust(15, ' '), end='')
        except:
            print(f"".ljust(15, ' '), end='')
        print(f"{submenu[i2]}")

def update(menu, submenu, control, cl):
    print("\x1b[2J\x1b[H") # clear

    mTam = 0
    subTam = 0
    i = 0
    i2 = 0
    meiosub = int(len(submenu) / 2) - 1
    mTam = len(menu)
    subTam = len(submenu)

    menuBaixo = int(mTam - control.getPos1())
    menuCima = int(control.getPos1())
    subBaixo = int(subTam - meiosub)
    subCima = int(meiosub - 1)

    if subCima > menuCima:
        #Se faltar espaço a cima
        while subCima > menuCima:
            #Move o SubMenu para baixo
            subBaixo += 1
            subCima += 1
            meiosub += 1
    elif subBaixo > menuBaixo:
        #Se faltar espaço a baixo
        while subBaixo > menuBaixo:
            #Move o SubMenu para cima
            subCima += 1
            subBaixo -= 1
            meiosub += 1

    nAselecionado = control.getPos1()
    nAmeio = meiosub
    inicioSubmenu = nAselecionado - nAmeio


    while i < mTam:
        if i == inicioSubmenu or (i > inicioSubmenu and i < (subTam + inicioSubmenu)):
            while i2 < subTam:
                try:
                    if not isinstance(menu[i], list):
                        raise Exception('is not a flexmenu')
                    else:
                        showFlex(menu, submenu, control, i, i2, cl)
                except:
                    showCommon(menu, submenu,control,i,i2, cl)
                i = i + 1
                i2 = i2 + 1
        if i < mTam:
            print(f"{menu[i]}")
        i = i + 1
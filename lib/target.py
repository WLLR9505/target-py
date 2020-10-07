from lib.target_menu import Vmenu
from lib.target_menu import Hmenu
from lib.target_menu import VsubMenu
from lib.target_menu import showMenu
from lib.target_menu.colors import palette
from msvcrt import getch


def simpleMenu(menu, control, color, submenu):
    input = ''
    control.resetPos()

    cl = palette.selectColor(color)

    Vmenu.update(menu, control, cl)

    while True:
        showMenu.menuV(control, cl, input, menu)
        input = getch().decode('ASCII')

        if input == control.getBack():
            control.setPos1(-1)
            return control

        print("\x1b[2J\x1b[H") # clear
        if input == control.getElect():
            break
    
    if submenu is not None:
        VsubMenu.update(menu, submenu, control, cl)
        while True:
            showMenu.subMenuV(control, cl, input, menu, submenu)
            input = getch().decode('ASCII')
    
            if input == control.getBack():
                control.setPos2(-1)
                return control

            print("\x1b[2J\x1b[H") # clear
            if input == control.getElect():
                break

from lib.target_menu import Vmenu
from lib.target_menu.colors import palette
from lib.target_menu import VsubMenu

def menuV(control, cl, input, menu, submenu=None):
    if input == control.getUp():
        control.setPos1(control.getPos1() - 1)
    elif input == control.getDown():
        control.setPos1(control.getPos1() + 1)


    if control.getPos1() == len(menu):
        control.setPos1(0)
    elif control.getPos1() < 0:
        control.setPos1(len(menu) - 1)
    
    print("\x1b[2J\x1b[H")
    Vmenu.update(menu, control, cl)

def subMenuV(control, cl, input, menu, submenu=None):
    if input == control.getUp():
        control.setPos2(control.getPos2() - 1)
    elif input == control.getDown():
        control.setPos2(control.getPos2() + 1)
    

    if control.getPos2() == len(submenu):
        control.setPos2(0)
    elif control.getPos2() < 0:
        control.setPos2(len(submenu) - 1)
    
    print("\x1b[2J\x1b[H")
    VsubMenu.update(menu, submenu, control, cl)
    
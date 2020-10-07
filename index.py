from lib.target_menu.colors import palette
from lib.target_menu import Hmenu
from lib.target_menu.controls import Controls
from lib import target
from msvcrt import getch

testMenu = ["item 1", "item 2", "item 3"]
testSubmenu = ["sub1", "sub2", "sub3", "sub4"]

def run():
    control = Controls()


    while control.getPos1() >= 0:
        target.simpleMenu(testMenu, control, 'red', testSubmenu)

        if control.getPos1() == -1:
            print("\x1b[2J\x1b[H") # clear
            return 0
        
        if control.getPos1() == 0:
            test(testMenu[control.getPos1()])
        elif control.getPos1() == 1:
            test(testMenu[control.getPos1()])
        elif control.getPos1() == 2:
            test(testMenu[control.getPos1()])


def test(txt):
    print(txt)
    getch()

run()
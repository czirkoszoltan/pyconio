import econio

econio.clrscr()
print("Use cursor keys to control the asterisk")

x = 40
y = 12
econio.rawmode()
while True:
    econio.gotoxy(x, y)
    econio.textcolor(econio.LIGHTGREEN)
    econio.write("*")
    econio.gotoxy(80, 24)
    
    key = econio.getch()
    econio.gotoxy(x, y)
    econio.textcolor(econio.BLUE)
    econio.write(".")

    if key == econio.UP:
        y = max(y-1, 2)
    elif key == econio.DOWN:
        y = min(y+1, 24)
    elif key == econio.LEFT:
        x = max(x-1, 1)
    elif key == econio.RIGHT:
        x = min(x+1, 80)
    elif key == econio.ESCAPE:
        break
econio.normalmode()

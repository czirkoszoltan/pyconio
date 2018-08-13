import econio
import time

# Init
econio.set_title("python-econio test")

# Positioning
econio.clrscr()
econio.gotoxy(0, 0)
econio.textcolor(econio.LIGHTGREEN)
econio.write("Hello")
econio.gotoxy(10, 0)
econio.textbackground(econio.LIGHTBLUE)
econio.write("world!")
print()

# Printing color codes
print(econio.backgroundcolors[econio.RESET], end="")
print("{}Hello {}world!".format(econio.textcolors[econio.RED], econio.textcolors[econio.GREEN]))

# Color combinations
for b in range(0, 16):
    econio.gotoxy(5, 5+b)
    for t in range(0, 16):
        econio.textcolor(t)
        econio.textbackground(b)
        econio.write(" X ")
    econio.write("\n")
print()

# Raw input
econio.textbackground(econio.RESET)
econio.textcolor(econio.RESET)
print("Raw input test, press keys and then Enter:")
econio.rawmode()
while True:
    ch = econio.getch()
    if ch == econio.ENTER:
        break
    print(ch, end=" ")
print()
econio.normalmode()

# Raw input buffering
print("Raw input buffering test, 3s delay, press any keys")
econio.rawmode()
time.sleep(3)
if not econio.kbhit():
    print("No keys pressed.")
else:
    while econio.kbhit():
        print(econio.getch(), end=" ")
    print()
print()
econio.normalmode()

# Normal input
name = input("Enter your name: ")
print("Hello,", name)

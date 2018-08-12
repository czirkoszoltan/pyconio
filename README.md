# Python econio library

Colored output and raw keyboard handling for Linux and Windows console.

This package is created for educational purposes. Uses Jonathan Hartley's [colorama](https://github.com/tartley/colorama) library 
for color output, which is included for convenience.


## Screen and cursor positioning

See the functions in `printer.py`:

```python
import econio

econio.clrscr()
econio.gotoxy(10, 1)
print("Hello world!")
```


## Colored output

See the constants in `colors.py`:

```python
import econio

econio.textcolor(econio.LIGHTGREEN)
econio.textbackground(econio.BLUE)
print("Hello world!")
```

Color codes can be embedded into strings:

```python
print("{}Hello {}world!".format(econio.textcolors[econio.RED], econio.textcolors[econio.GREEN]))
```


## Buffered output

The function `econio.write()` works exactly like `print()`, but does not
flush the output by default. This can be used to draw an entire scene.
Then you can use `econio.flush()` – but econio tries to handle that
the same way Python does, by flushing the output when input is requested.


## Line-oriented input

Just use `input()` as usual.


## Raw keyboard input

Switch to raw mode using `econio.rawmode()`. Then use `econio.kbhit()` to check
if a key is pressed. `econio.getch()` returns an ASCII code or a key code
(see `keys.py`). Finally call `econio.normalmode()`.

```python
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
    econio.gotoxy(80, 24, flush=True)
    
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
```

You can use `with econio.rawkeys()` as well.

## License

MIT license. For the license of the colorama package, see [https://github.com/tartley/colorama/](https://github.com/tartley/colorama/).

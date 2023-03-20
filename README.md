# A Game of HangMan
## Discription
- This is a program that I wrote awhile back. I've modified it a bit so that it can run with CLI. I just thought it'd be fun to add a little extra to [BrainHack School Taiwan's "Writing scripts in python" module](https://brainhackschool-taiwan.github.io/docs/assignments/Writing_scripts_in_python.html).
- There's nothing fancy about this toy Python program. I just thout I could demonstrate that the code within the conditional
```
if __name__ == "__main__"
```
will be executed if the `.py` file is run as a script, but not when it is imprted as in `exe.py` in which the only line of code is `import hangman`.
- If `python exe.py -t abunchofwords` is run in the terminal, the entire part of the HangMan game will be ommited as I have it under the `if` loop.

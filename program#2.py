class fg:
    MAGENTA = '\033[35m'
    BLUE    = '\033[34m'
    RESET   = '\033[39m'
    RED     = '\033[31m'
    CYAN    = '\033[36m'

class bg:
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'
    MAGENTA = '\033[45m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'

name = input("\033[31mEnter your name: ")

age = int(input("\033[34mEnter your age: "))

address = input("\033[35mEnter your address: ")

print(fg.CYAN, "Hi my name is", fg.CYAN, bg.BLUE, style.BRIGHT,{name}, style.RESET_ALL)
print(fg.CYAN, "I'm", fg.BLUE, bg.MAGENTA, style.BRIGHT,{age},"years old", style.RESET_ALL)
print(fg.CYAN, "Currently residing at", fg.MAGENTA, bg.GREEN, style.BRIGHT,{address},style.RESET_ALL)


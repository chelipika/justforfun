import time, os, random
fireworks = [
    "    *    ",
    "   ***   ",
    "  *****  ",
    " ******* ",
    "*********",
    " ******* ",
    "  *****  ",
    "   ***   ",
    "    *    "
]
def display_firework(color_code):
    for frame in fireworks:
        print(f"\033[{color_code}m{frame}")
        time.sleep(0.1)
def display_message():
    print(f"\033[{random.randint(30, 38)}mAlhamdulillah, I wish you protection from laziness and poorness, and everything that is good for you!")
    time.sleep(0.5)
while True:
    display_firework(random.randint(30, 38))  # Firework effect with random colors
    display_message()  # Main "Happy New Year" message

from operator import length_hint
from re import I
from time import sleep
from Game1 import *
from Game2 import *
from game3 import *

def print_load(dot_amount: int, load_time: float):
    for _ in range(dot_amount):
        print(".", end="", flush=True)
        sleep(load_time)


def print_slow(line_to_slow: list, slow_time: float):
    print()
    for _ in line_to_slow:
        sleep(slow_time)
        print(_, end="", flush=True)
        sleep(slow_time - (slow_time * 0.50))


def print_natural(input: str, slow_time: float):
    for char in input:
        print(char, end="", flush=True)
        sleep(slow_time)


def main():
    print_natural("\n\nHello", 0.05)
    sleep(0.05)
    print_natural("\nPlease enter your name: ", 0.05)
    name = input()
    sleep(0.3)
    print_load(3, 0.75)
    print_natural("\nHello " + name, 0.05)
    sleep(1)
    print_natural("\nWelcome to the game.", 0.05)
    sleep(0.75)
    print_natural("\nLet's begin.\n", 0.05)
    sleep(0.5)

    runGame1()

    print_load(3, 0.50)

    print_natural("\nThat was just a basic showcase,\n", 0.05)
    sleep(0.5)
    print_natural("let's continue\n", 0.05)
    
    runGame2()
    
    print_load(3, 0.50)
    print_natural("\nI hope you had fun with that one.\nNow, let's move on to the cursor.\n", 0.05)
    sleep(0.5)
    
    runGame3()
    
    print_load(3, 0.50)
    print_natural("\nI hope you enjoyed the games.\n", 0.05)
    sleep(0.5)


if __name__ == "__main__":
    main()
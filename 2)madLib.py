import random


def chickfight():
    adj = input("Adjective: ")
    s = f"If you're going to challenge a couple to a chicken fight during spring break, make sure they're more {adj} than you!"
    print(s)


def vaccum():
    adj = input("Noun: ")
    s = f"Be careful not to vacuum the {adj} when you clean under your bed."
    print(s)


def basketball():
    adj = input("Body Part: ")
    s = f"Basketball is the best {adj} in the world"
    print(s)


def chicken():
    adj = input("Noun: ")
    s = f"What came first, the chicken or the {adj}?"
    print(s)


def cactus():
    adj = input("Verb: ")
    s = f"I like my donuts with extra {adj} on them."
    print(s)


i = 1
while i == 1:
    m = random.choice([0, 1, 2, 3, 4])
    if m == 0:
        cactus()
    if m == 1:
        chicken()
    if m == 2:
        chickfight()
    if m == 3:
        vaccum()
    if m == 4:
        basketball()
    k = input("To Stop Playing Enter 0:")
    try:
        if int(k) == 0:
            i = 0
    except ValueError:
        continue

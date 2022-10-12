# -*- coding: utf-8 -*-
import random
import re
from reflection import reflect
from text_patterns import psychobabble


def dailiza_answer(user_input):
    """Diese Funktion generiert die Antwort des DAILIZA-Bot.
    """
    user_input = user_input.strip(",.?!")

    # Test input string for all known text patter in pychobabble
    for pattern, responses in psychobabble:
        match = re.search(pattern, str(user_input.lower()))
        if match:
            rspns = random.choice(responses)
            return rspns.format(*[reflect(g) for g in match.groups()])    


def run_dailiza_bot():
    """Diese Funktion startet den DAILIZA-Bot.
    """
    print("Hey Hallo! Ich bin Dailiza. Womit kann ich dir helfen?")
    user_input = ""
    while "exit" not in user_input:
        user_input = raw_input(">> ")
        print(dailiza_answer(user_input))


if __name__ == '__main__':
    run_dailiza_bot()

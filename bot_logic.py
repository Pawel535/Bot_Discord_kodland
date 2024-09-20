import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def coin_toss():
    return random.choice(["Heads", "Tails"])

print(coin_toss())
def random_emoji():
    emojis = ['😀', '😂', '😍', '😎', '🤔']
    return random.choice(emojis)

print(random_emoji())
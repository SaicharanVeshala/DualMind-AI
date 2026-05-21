blocked_words = [
    "hack",
    "malware",
    "bomb",
    "kill",
    "attack"
]


def is_safe(prompt):

    prompt = prompt.lower()

    for word in blocked_words:

        if word in prompt:
            return False

    return True
from functools import lru_cache

# expand character set for more gradients, ordered from darkest to lightest
CHARACTERS = ['@', '#', '8', '&', '%', 'X', '+', '=', '-', ':', '.']  # More detailed gradients
CHAR_RANGE = int(255 / len(CHARACTERS))


@lru_cache
def get_char(val):
    if val > 240:  # green screen detection
        return ' '
    val = 255 - val
    return CHARACTERS[min(int(val/CHAR_RANGE), len(CHARACTERS)-1)]

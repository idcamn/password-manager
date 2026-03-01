import secrets
from .constants import (SAFE_UPPERCASE, SAFE_LOWERCASE, SAFE_DIGITS, SAFE_SYMBOLS, SAFE_ALPHABET)


def generate_password(length: int = 12) -> str:
    if length < 4:
        raise ValueError("Password length must be >= 4")

    # Guarantee every symbol at least once
    guaranteed = [
        secrets.choice(SAFE_UPPERCASE),
        secrets.choice(SAFE_LOWERCASE),
        secrets.choice(SAFE_DIGITS),
        secrets.choice(SAFE_SYMBOLS)
    ]

    res = [secrets.choice(SAFE_ALPHABET) for _ in range(length - 4)] + guaranteed
    secrets.SystemRandom().shuffle(res)
    return ''.join(res)
import string


# Characters excluded to avoid visual ambiguity (O/0, I/l/1)
SAFE_UPPERCASE = ''.join(c for c in string.ascii_uppercase if c not in 'IO')
SAFE_LOWERCASE = ''.join(c for c in string.ascii_lowercase if c not in 'ilo')
SAFE_LETTERS = SAFE_UPPERCASE + SAFE_LOWERCASE

SAFE_DIGITS = ''.join(c for c in string.digits if c not in '01')

SAFE_SYMBOLS = '()[]!@#$^&_?+*/={}:;-'

SAFE_ALPHABET = SAFE_LETTERS + SAFE_DIGITS + SAFE_SYMBOLS
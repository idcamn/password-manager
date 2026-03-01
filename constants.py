import string


SAFE_UPPERCASE = ''.join(c for c in string.ascii_uppercase if c not in 'IO')
SAFE_LOWERCASE = ''.join(c for c in string.ascii_lowercase if c not in 'ilo')
SAFE_DIGITS = ''.join(c for c in string.digits if c not in '01')
SAFE_SYMBOLS = '()[]!@#$^&_?+*/={}:;-'
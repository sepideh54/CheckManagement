import re

def is_persian_text(text):
    pattern = r'^[\u0600-\u06FF\s]+$'
    return bool(re.match(pattern, text))
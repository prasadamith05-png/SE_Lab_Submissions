"""
Spam Scoring Filter - Lab 7 (Fuzz Testing Target & Hardened Implementation)
PES University - Software Engineering Lab 7
"""

# -------------------------------------------------------------
# Hardened, Production-Grade Functions with Guard Clauses
# -------------------------------------------------------------

def sender_domain(email):
    """
    Extract the domain part from an email address.
    Robust against None, empty strings, missing '@', and trailing '@'.
    """
    if not isinstance(email, str):
        return ""
    parts = email.rsplit('@', 1)
    if len(parts) < 2 or not parts[1]:
        return ""
    return parts[1].strip().lower()


def first_link(text):
    """
    Extract the first URL starting with http from a text string.
    Robust against None, missing links, and edge delimiters.
    """
    if not isinstance(text, str):
        return None
    start = text.find('http')
    if start == -1:
        return None
    end = text.find(' ', start)
    if end == -1:
        end = len(text)
    return text[start:end]


def shout_ratio(text):
    """
    Compute ratio of uppercase letters to total alphabetic letters.
    Returns float in range [0.0, 1.0]. Robust against empty strings, numbers, None.
    """
    if not isinstance(text, str):
        return 0.0
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return 0.0
    upper = [c for c in letters if c.isupper()]
    return len(upper) / len(letters)

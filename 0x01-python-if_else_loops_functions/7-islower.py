#!/usr/bin/python3
def islower(arg):
    """Check if characters a upper or lower."""
    if ord(arg) >= 97 and ord(arg) <= 122:
        return True
    else:
        return False

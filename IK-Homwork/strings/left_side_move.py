"""
given a string with random letters and numbers move the letters to left side by maintaining original order
and minimum writes.
Move all letters to left side with minimum memory writes



"""

def leftmove(given):
    ascii_arr = [ord(c) for c in given]
    # create a boundary array with characters and integers
    # characters are from [65-90]A-Z ,[97-122]a-z, [48-57]0-9
    # since we only only characters are given we can safely assume [65-122] ascii character range


    print ascii_arr


leftmove("a2b8z9n9c8x1")

def valid_parant(s):
    """
    s = "({}()[] { ([])})"
    :param s:
    :return:
    """
    d = {'}':'{',']':'[',')':'('}
    s=[]
    for ch in s:
        if ch in ('(','{','['):
            s.append(ch)
        elif ch in (')','}',']'):
            if len(s) == 0 or s.pop() != d[ch]:
                return False
    if len(s) == 0:
        return True
    else:
        return False
"""
Reverse a string by preserving spaces
"""
def revString(str):
    a = str.split()
    rs = [a[i][::-1] for i in range(len(a)-1,-1,-1)]
    return ' '.join(rs)

print revString("Kavitha is very smart.")

"""
http://www.cs.cmu.edu/~cburch/survey/recurse/hanoiimpl.html
"""

def tower_of_hanoi(st,end,helper,disks):
    """
    Prints steps for moving disks from Tower A to Tower B.
    Restriction: bigger disk can't be on the top of the smaller disk

    :param A:  Tower A
    :param B:  Tower B
    :param C:  Tower C
    : disks : number of disks at Tower A
    :return:
    """
    if disks == 0:
        return
    else:
        tower_of_hanoi(st,helper,end,disks-1)
        print "move disc %d from %s to %s"%(disks,st,end)
        tower_of_hanoi(helper,end,st,disks - 1)


tower_of_hanoi('A','B','C',1)
tower_of_hanoi('A','B','C',2)
print "n = 3"
tower_of_hanoi('A','B','C',3)
#print tower_of_hanoi('A','B','C',5)


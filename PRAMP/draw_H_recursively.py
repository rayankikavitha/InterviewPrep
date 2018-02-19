import math
import Graphics

def drawLine(x1, y1, x2, y2):
    # draws line, assume implementation available
    point1 = Graphics.point
    Graphics.Line(point1, point2)


def drawHTree(x, y, length, depth):
    # recursion base case
    if depth == 0:
        return

    x0 = x - length / 2
    x1 = x + length / 2
    y0 = y - length / 2
    y1 = y + length / 2

    # draw the 3 line segments of the H-Tree
    drawLine(x0, y0, x0, y1)  # left segment
    drawLine(x1, y0, x1, y1)  # right segment
    drawLine(x0, y, x1, y)  # connecting segment

    # at each stage, the length of segments decreases by a factor of √2
    newLength = length /math.sqrt(2)

    # decrement depth by 1 and draw an H-tree
    # at each of the tips of the current ‘H’
    drawHTree(x0, y0, newLength, depth - 1)  # lower left  H-tree
    drawHTree(x0, y1, newLength, depth - 1)  # upper left  H-tree
    drawHTree(x1, y0, newLength, depth - 1)  # lower right H-tree
    drawHTree(x1, y1, newLength, depth - 1)  # upper right H-tree

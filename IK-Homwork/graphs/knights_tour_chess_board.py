"""
Question:
---------
Assume you're given a normal chessboard and a knight that
moves like in normal chess. You are then given two inputs:
starting location and ending location in the form of x,y co-
ordinates. The goal is to calculate the shortest number of
moves that the knight can take to get to the target location.
(All the coordinates start with 0 and end with (rows-1) or (cols -1)).
For a 8x8 board the first cell will be (0,0) and the corresponding
opposite corner cell will be (7,7)
Input:
rows
cols
startx
starty
endx
endy
Output:
-1 if there is no solution
OR
num (num = 0 or num > 0)

Solution:
---------
There are two ways to think about a problem like this
1. Start from the starting cell and explore recursively (brute force / DFS)
-OR-
2. Each cell is a vertex in a graph and cells reachable by a knight move are
     adjacent vertices to each vertex.
   "Least number of steps" gives away that we are looking for the shortest path
     and therefore we can do a BFS
Key is to implement the 'get_neighbors' method for this implicitly graphs
question.
For this problem, we don't have to build a graph since get_neighbors can be
done in constant time (there are only 8 possible neighbors).



"""
import Queue

def get_neighbors(rows,cols,i,j):
    """
    Returns a list of cells reachable from the cell(i,j)
    :param rows: total number of rows
    :param cols: total number of columns
    :param i: current x position
    :param j: current y position
    :return:
    """
    # There are 8 potential neighbors
    potential_neighbors=[(i+2, j+1), (i+2, j-1),
                    (i-2, j+1), (i-2, j-1),
                    (i+1, j+2), (i+1, j-2),
                    (i-1, j+2), (i-1, j-2)]
    # All potential neighbors that are inside the board bounds
    # are valid neighbors
    neighbors = []
    for p_i, p_j in potential_neighbors:
        if 0 <= p_i < rows and 0 <= p_j < cols:
            neighbors.append((p_i, p_j))

    return neighbors

def shortest_path(rows, cols, startx, starty, endx, endy):
    #intialize the queue with the starting point
    #q = Queue()
    #q.enqueue((startx,starty))
    q=[]
    q.append((startx,starty))

    # we can keep track of back reference if we want actual paths
    back_references={(startx,starty):None}

    # or we can keep track of distances we care about
    distances ={(startx,starty): 0}

    while q:
        #x,y = q.dequeue()
        x,y = q.pop(0)

        # if we are at the end of cell, we can stop
        if x == endx and y == endy:
            break

        # continue visiting neighbors
        for neighbor_x, neighbor_y in get_neighbors(rows,cols,x,y):
            # If the neighbor has already been visited, we can skip
            # We can use either back_ref or distances here
            # since we add every new vertex we visit to both of them
            if (neighbor_x,neighbor_y) in distances:
                continue

            # if not visited, the distance from start for this neightbor would be distance
            # of the current vertex + 1
            distances[(neighbor_x,neighbor_y)] = distances[(x,y)] + 1

            # The back reference for this neighbor is the current vertex
            back_references[(neighbor_x, neighbor_y)] = (x,y)

            #q.enqueue((neighbor_x, neighbor_y))
            q.append((neighbor_x, neighbor_y))

    if (endx, endy) not in distances:
        # We have not found the end cell in our breadth first search
        return -1
    return distances[(endx, endy)]


def main():
    """
    rows = int(raw_input())
    cols = int(raw_input())
    startx = int(raw_input())
    starty = int(raw_input())
    endx = int(raw_input())
    endy = int(raw_input())
    """

    print shortest_path(5, 5, 0, 0, 4,1)

if __name__ == '__main__':
    main()




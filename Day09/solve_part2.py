import numpy as np

#We solve by just keeping a set of all positions visited
#This way we don't need to consider non visited places ever!

moveDict = {'U':np.array([0,1]),
            'L':np.array([-1,0]),
            'D':np.array([0,-1]),
            'R':np.array([1,0])}


def update_tail(head,tail):
    #Make the head move and tail follow
    #Mpw get the difference in the tail to head pos
    delta = head-tail
    #Tail can only be either within 1 block, 2 blocks or diagonally smaller.
    #Thus if two blocks we simply move in that dir. check
    magnitude = np.linalg.norm(delta)
    if magnitude >= 2:
        #tail += (delta/2)
        tail += np.array([np.sign(delta[0]),np.sign(delta[1])])
    return tail

#Set up initial conditions
positions = [np.array([0,0]) for i in range(10)]

visitedGridPositions = set([(0,0),])
with open("input.txt","r") as f:
    for line in f:
        tokens = line.split()
        for i in range(int(tokens[1])):
            positions[0] += moveDict[tokens[0]]
            for j in range(9):
                positions[j+1] = update_tail(positions[j],positions[j+1])
            visitedGridPositions.add((positions[9][0],positions[9][1]))
print(len(visitedGridPositions))
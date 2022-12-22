import numpy as np

#We solve by just keeping a set of all positions visited
#This way we don't need to consider non visited places ever!

moveDict = {'U':np.array([0,1]),
            'L':np.array([-1,0]),
            'D':np.array([0,-1]),
            'R':np.array([1,0])}


def make_move(head,tail,move):
    #Make the head move and tail follow
    head += moveDict[move]
    #Mpw get the difference in the tail to head pos
    delta = head-tail
    #Tail can only be either within 1 block, 2 blocks or diagonally smaller.
    #Thus if two blocks we simply move in that dir. check
    magnitude = np.linalg.norm(delta)
    if magnitude >= 2:
        #tail += (delta/2)
        tail += np.array([np.sign(delta[0]),np.sign(delta[1])])
    return head,tail

#Set up initial conditions
posHead = np.array([0,0])
posTail = np.array([0,0])

visitedGridPositions = set([(0,0),])
with open("input.txt","r") as f:
    for line in f:
        tokens = line.split()
        for i in range(int(tokens[1])):
            posHead,posTail = make_move(posHead,posTail,tokens[0])
            visitedGridPositions.add((posTail[0],posTail[1]))
print(len(visitedGridPositions))
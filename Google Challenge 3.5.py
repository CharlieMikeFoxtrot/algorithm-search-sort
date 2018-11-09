"""
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, 
but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via 
the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and 
dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge 
of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. 
Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can 
remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing 
Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. 
The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. 
The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod,
 where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of
 nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always
 passable (0). The map will always be solvable, though you may or may not need to remove a wall. 
 The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal 
 moves are allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
Output:
    (int) 7

Inputs:
    (int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
Output:
    (int) 11
"""

"""
def answer(maze):
    # your code here
"""

def answer(maze):
    
    
    l1=[]
    l2=[]
    maze, l1= solve(maze,0,0,l1)
    best = maze[len(maze)-1][len(maze[len(maze)-1])-1] -1
    

    if best == -1:
        best = 9999999

    maze, l2= solve(maze,len(maze)-1,len(maze[len(maze)-1])-1,l1)
    
    l1 += [[0,0]]
    if [len(maze)-1,len(maze[len(maze)-1])-1] in l1:
        l1.remove([len(maze)-1,len(maze[len(maze)-1])-1])
    l2 += [[len(maze)-1,len(maze[len(maze)-1])-1]]


    best = checker(maze,l1,l2,best)


    return(best)
    
def checker(m,l1,l2,b):
    for pair in l1:

        if [pair[0],pair[1]+2] in l2:

            if m[pair[0]][pair[1]] + m[pair[0]][pair[1]+2] -1 < b:

                b = m[pair[0]][pair[1]] + m[pair[0]][pair[1]+2] -1
            
        if [pair[0]+2,pair[1]] in l2:
            if m[pair[0]][pair[1]] + m[pair[0]+2][pair[1]] -1 < b:  

                b = m[pair[0]][pair[1]] + m[pair[0]+2][pair[1]] -1
            
        if [pair[0],pair[1]-2] in l2:
            
            if m[pair[0]][pair[1]] + m[pair[0]][pair[1]-2] -1 < b:

                b = m[pair[0]][pair[1]] + m[pair[0]][pair[1]-2] -1          
        
        if [pair[0]-2,pair[1]] in l2:
            if m[pair[0]][pair[1]] + m[pair[0]-2][pair[1]] -1 < b:

                b = m[pair[0]][pair[1]] + m[pair[0]-2][pair[1]] -1
    return b
        

def solve(m,x,y,lx):
    i=2
    m[x][y] = 2
    l=[]


    newPositions = [] 

    
    while True:
        positions = []


        for pos in newPositions:
            if pos in lx:
                lx.remove(pos)
            positions += check(m,pos[0],pos[1],i)

        positions += check(m,x,y,i)
        l+= positions


        newPositions = positions 

        if len(newPositions) == 0:
            return m,l
        i+=1

def check(maze,down,right,i):

    options = []
    if down +1 < len(maze):
        if  maze[down+1][right] == 0 or maze[down+1][right] > i+1:
            options.append([down+1,right])
            maze[down+1][right] = i+1
        
        
    if down -1 >= 0:
        if maze[down-1][right] == 0 or maze[down-1][right] > i+1:
            options.append([down-1,right])
            maze[down-1][right] = i+1
        
        
    if right -1 >= 0 :
        if maze[down][right-1] == 0 or maze[down][right-1] > i+1:
            options.append([down, right-1])
            maze[down][right-1] = i+1
        
        
    if right + 1 < len(maze[down]):
        if maze[down][right+1] == 0 or maze[down][right+1] > i+1:
            options.append([down, right+1])
            maze[down][right+1] = i+1
            
    return(options)
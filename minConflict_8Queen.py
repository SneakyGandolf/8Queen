# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 20:11:33 2022

@author: caeli
"""

import numpy as np
import random
import math



def minConflict(tries):
    #np.random.seed(5)
    
    rows = np.random.randint(0, 8, 8)
    print('The initial puzzle:', rows)
    iterations, restartCnt, success, fails = 0, 0, 0, 0
    didweS = True
    
    for num in range(tries):
        iterations += 1
        #Identify queens with conflicts in the array
        #Randomly choose a queen w/ >0 conflicts
        check = True
        infiniteLoopTest = 0
        while check:
            choice = random.choice(rows) #equals the index not element
            #print('COL:',choice, '<-->', 'ROW:',rows[choice])
            conflicts = 0
            for i in range(8):
                #for j in range(i+1,8):
                if i != choice: #Passing over current Q location
                    if rows[choice] == rows[i] or abs(choice - i) == abs(rows[choice] - rows[i]):
                        conflicts += 1
                        #print('Conflict:', choice, i)
            infiniteLoopTest += 1
        
            if conflicts > 0 or infiniteLoopTest > 7:
                #print(conflicts, '<--')
                check = False;
        
        
        #Find row w/ lowest num conflicts in that column(Compare other arr elements then check diag)
            #Put queen in that row(Change val in row)
        
        #def lowestConflicts(board):
        rowsCopy = rows.copy()
        options = []
        for j in range(8): #Iterate through all rows
            if j != rows[choice]: #Passing over the choosen row location
                rowsCopy[choice] = j #Set new row value to choosen column in copy
                cnt = 0
                for i in range(8): # Iterate through all columns to make checks
                    if i != choice: #Avoid situation when column(i) equals the choosen column
                        #Make checks on adjacent rows and diags
                        if rowsCopy[choice] == rowsCopy[i] or abs(choice - i) == abs(rowsCopy[choice] - rowsCopy[i]):
                            cnt += 1               
                options.append([j, cnt]) #Add in order to determine best row location in the choose column
    
        
        max = conflicts
        for option in options:
            if option[1] < max:
                max = option[1]
                newRow = option[0]
                rows[choice] = newRow
        
    
        #This segment makes such there are no total remaining intersects
        intersects = 0
        for i in range(0, 8):
            for j in range(i+1, 8):
                if rows[i] == rows[j] or abs(i - j) == abs(rows[i] - rows[j]):
                    intersects += 1
                    
        
        if max == 0 and intersects == 0:
            success += 1
            #print('Solution found!')
            break
        if max == conflicts: #Random restart
            #Find random column
            findCol = random.choice(rows)
            ranRow = random.randint(0,7)
            rows[findCol] = ranRow
            restartCnt += 1
    
    if success < 1:
        fails += 1
        didweS = False
        
    return rows, iterations, restartCnt, success, fails, didweS
    
    


#if not solution then repeat process(choose ran queen) while statement?
#random restart - Can't find successor w/ fewer successors so move random queen then start again(else statement?)

def main():
    
    numOfSuccess, numOfFails, avgRestarts, avgPerRuns = 0, 0, 0, 0
    userInput = int(input("How puzzles would you like to solve?\n"))
    
    print('The corrected puzzles are displayed below:\n\n')
    for numPuz in range(userInput):
        results = minConflict(500)
        avgPerRuns += results[1]
        avgRestarts += results[2]
        numOfSuccess += results[3]
        numOfFails += results[4]

        if results[5] == True:
            print('Puzzle solved', '-->', results[0],'\n')
        else:
            print('Not Quite!', '-->', results[0],'\n')
    
    print('For', userInput, 'puzzles my min-conflict solved', numOfSuccess,'for a success percent of', math.ceil((numOfSuccess / userInput)*100),'%')
    print('On average it took about', round(avgPerRuns / userInput), 'iterations to find a solution.')
    print('This min-conflict program got stuck on average', math.floor((numOfFails / userInput)*100),'% for this run.')
    print('Average random restarts per run:', round(avgRestarts/userInput))
    
if __name__ == "__main__":
    main()

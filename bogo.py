"""
Author: Dara Dimoff
Language: Python3
Program: bogo.py
Description: Implementation of the bogo sorting algorithm and prints out the
    amount of time it took as well as number of iterations it went through.
    Time Complexity: O(N + 1!)
"""

from random import *
from time import *

mergeCounter = 0

def inorder(lst):
    """
    Checks to see if a list is sorted or not

    Parameters:
        lst (list) - The list to check
    Returns:
        Boolean stating whether or not the list is sorted
    """
    i = 0
    j = len(lst)
    while i + 1 < j:
        if lst[i] > lst[i + 1]:
            return False
        i += 1
    return True
 
def bogo(lst):
    """
    Runs the bogo sorting algorithm

    Parameters:
        lst (list) - The list that will be scrambled using the bogo sorting
            algorithm
    Returns:
        The number of iterations it took for the algorithm to be successful
    """
    iterations = 0
    while not inorder(lst):
        iterations += 1
        shuffle(lst)
    return iterations

def merge(lst):
    """
    Runs the merge sort algorithm

    Parameters:
        lst (list) - The list to be sorted

    Returns:
        The number of iterations it took for the algorithm to be successful
    """
    
    if len(lst)>1:
        global mergeCounter

        # split the list and save the midpoint
        mid = len(lst)//2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        # divide and conquer
        merge(lefthalf)
        merge(righthalf)

        i=0
        j=0
        k=0

        # merge
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k]=lefthalf[i]
                i += 1
            else:
                lst[k]=righthalf[j]
                j += 1
            k=k+1

        while i < len(lefthalf):
            lst[k]=lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            lst[k]=righthalf[j]
            j += 1
            k += 1
            
        # update the number of iterations
        mergeCounter += 1
 
def main():
    """
    The main function that runs the program. Takes input from the user and runs
        the sorting algorithm based off of that. Prints out the results for each
        case requested by the user.
    """
    height = int(input("What is the highest number of elements in the list? "))
    print()
    global mergeCounter
    
    for i in range(2, height + 1):
        lst = []
        for i in range(0, i + 1):
            lst.append(randint(0, 100))
        print("----------------------------------------------")

        # run and print results of bogo sort
        print("Bogo sort:")
        print(i, "elements went through...")
        start = time()
        iterations = bogo(lst)
        
        print(iterations, "iterations and took " "%.2f seconds" % (time() - start))

        # run and print results of merge sort
        shuffle(lst)
        print("\nMerge Sort:")
        print(i, "elements went through...")
        start = time()
        merge(lst)
        print(mergeCounter, "iterations and took " "%.2f seconds" % (time() - start))

        # compare the results
        percent = iterations/mergeCounter
        print("\nBogo sort took %.4f%% as many iterations than merge sort" % (percent * 100))

    input("----------------------------------------------\nPress enter to quit")

main()

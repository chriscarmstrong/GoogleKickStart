import sys
import math

def read_a_b_values():
    '''Returns a, b (high and low values) in list'''
    ab = input()
    a = int(ab.split()[0])
    b = int(ab.split()[1])
    return [a, b]

def guess(ab):
    '''Returns midpoint between a and b rounded up'''
    midpoint = (ab[1]+ab[0]) / 2
    return math.ceil(midpoint)

#T is the number of rounds
T = int(input())

#Loop over number of rounds
for _ in range(T):
    #Read initial ab values for the round and N
    ab = read_a_b_values()
    N = int(input())

    #Loop over number of guesses exceeded or until gussed
    for _ in range(N):
        #output a guess
        guess_ = guess(ab)
        print(guess_)
        sys.stdout.flush()
        #check answer
        answer = input()
        if (answer == "CORRECT"):
            break
        if (answer == "TOO_SMALL"):
            ab[0] = guess_
        if (answer == "TOO_BIG"):
            ab[1] = guess_

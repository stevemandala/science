import sys

from random import *

NUM_BANDITS = 5
NUM_ITERATIONS = 1000
PAYOFF = 1

def get_action(p):
    if random() <= p:
        return PAYOFF
    return 0

def construct_bandit(p):
    return (lambda : get_action(p))

def construct_bandits():	
    # Constructs the bandits
    parameters = [random() for _ in range(0, NUM_BANDITS)]
    print("Parameters: {}".format(parameters))
    bandits = [construct_bandit(p) for p in parameters]
    return bandits


def choose_bandit_v1(payoffs, q):
    # With some probability, we choose a random bandit
    if random() < q:
        return randrange(NUM_BANDITS)
    # Otherwise, go with our most generous
    max_bandit = -1
    max_payoff = -1
    for i in range(0, NUM_BANDITS):
        if max_payoff < payoffs[i]:
            max_bandit = i
            max_payoff = payoffs[i]
    if max_bandit == -1:
        return randrange(NUM_BANDITS)
    return max_bandit


def choose_bandit_v2(payoffs, iter):
    # With some probability, we choose a random bandit
    q = float(NUM_ITERATIONS-iter)/float(NUM_ITERATIONS)
    if random() < q:
        return randrange(NUM_BANDITS)
    # Otherwise, go with our most generous
    max_bandit = -1
    max_payoff = -1
    for i in range(0, NUM_BANDITS):
        if max_payoff < payoffs[i]:
            max_bandit = i
            max_payoff = payoffs[i]
    if max_bandit == -1:
        return randrange(NUM_BANDITS)
    return max_bandit

def main():
    bandits = construct_bandits()
    payoffs = [0 for _ in range(0, NUM_BANDITS)]
    for i in range(0, int(NUM_ITERATIONS/2)):
        curr_bandit = choose_bandit_v1(payoffs, 1)
        curr_payoff = bandits[curr_bandit]()
        payoffs[curr_bandit] += curr_payoff
    for i in range(0, int(NUM_ITERATIONS/2)):
        curr_bandit = choose_bandit_v1(payoffs, 0)
        curr_payoff = bandits[curr_bandit]()
        payoffs[curr_bandit] += curr_payoff
    print("Final payoffs: {}".format(payoffs))
        

main()

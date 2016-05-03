# Coin toss
# Guy Whorley
# Simulate a coin toss. Display how many times the headtail appears.
# 0/02/2016 - gcw - created
import random

# init
trials = 5000

# def
def tossCoin(iter):
    coin = ( "head", "tail" )
    heads = 0
    tails = 0
    for i in range(1, 5001):
        singleToss = random.choice(coin)
        if singleToss == "head":
            heads += 1
        else:
            tails += 1
        print "Trial #{}: It's a {}!... So far: {} Head(s) and {} tail(s)".format(str(i), singleToss, str(heads), str(tails))
    #end for
#end def

# TOSS THE COINS
tossCoin(trials)

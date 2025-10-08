import numpy as np

def FizzBuzz(start, finish):
    
    numvec = np.arange(start,finish + 1)
    objvec = np.array(numvec,dtype = object)
    
    fizzbuzz_ = (numvec % 15 == 0)
    buzz_ = (numvec % 5 == 0) & (numvec % 15 != 0)
    fizz_ = (numvec % 3 == 0) & (numvec % 15 != 0)

    objvec[fizzbuzz_] = 'fizzbuzz'
    objvec[buzz_] = 'buzz'
    objvec[fizz_] = 'fizz'
    
    return(objvec)


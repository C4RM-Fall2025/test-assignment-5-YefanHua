import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):

    msum = m * ppy
    
    discount_factors = (1 + y / ppy) ** (-np.arange(1, msum + 1))
    
    couponpv = face * couponRate / ppy * discount_factors
    facepv = face * discount_factors[-1]
    
    wsum = np.sum(couponpv) + facepv
    wtsum = np.sum(couponpv * np.arange(1, msum + 1)) + facepv * (msum)
        
    x = wtsum / wsum / ppy
    return(x)


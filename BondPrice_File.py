import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    
        
    msum = m * ppy
    
    discount_factors = (1 + y / ppy) ** (-np.arange(1, msum + 1))
    
    couponspv = np.sum(discount_factors) * (couponRate * face / ppy)
    
    facepv = face * discount_factors[-1]
    
    x = couponspv + facepv
    
    return x

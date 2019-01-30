### 1 - 1
import math 
import numpy as np

S0 = 100.
K = 105.
T = 1.0
r = 0.05 
sigma = 0.2

I = 100000

np.random.seed(1000)
z = np.random.standard_normal(I)
ST = S0 * np.exp((r - sigma ** 2 / 2) * T + sigma * math.sqrt(T) * z)

hT = np.maximum(ST - K, 0)

C0 = math.exp(-r * T) * np.mean(hT)

print("Value of the European call option:{:5.3f}".format(C0))

### 1 - 2
# Monte Carlo valuation of European call option
# in Black-Scholes-Merton model
# bsm_mcs_euro.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
import math
import numpy as np

# Parameter Values
S0 = 100.  # initial index level

K = 105.  # strike price
T = 1.0  # time-to-maturity
r = 0.05  # riskless short rate
sigma = 0.2  # volatility

I = 100000  # number of simulations

# Valuation Algorithm
z = np.random.standard_normal(I)  # pseudo-random numbers
# index values at maturity
ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * math.sqrt(T) * z)
hT = np.maximum(ST - K, 0)  # payoff at maturity
C0 = math.exp(-r * T) * np.mean(hT)  # Monte Carlo estimator

# Result Output
print('Value of the European call option %5.3f.' % C0)


### 1 - 3
import numpy as np
import pandas as pd
from pylab import plt, mpl

plt.style.use("seaborn")
mpl.rcParams["font.family"] = "serif"

data = pd.read.csv("/Users/zhaochenlian/Downloads/Python/AAPL.csv", index_col = 0,parse_dates = True )

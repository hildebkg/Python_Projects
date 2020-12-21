#Coin flip data collector

r = int(input('Enter the number of times to flip the coin: '))

heads = 0
tails = 0

import random

for k in range(r):
    flip = random.randint(0,1)
    if flip == 1:
        heads = heads + 1
    else:
        tails = tails + 1
    
print('There were {0} heads\n'.format(heads))
print('There were {0} tails\n'.format(tails))

percent_heads = (heads/(heads + tails))*100
print('The percentage of flips that were heads was {0:.2f}%\n'.format(percent_heads))

percent_tails = (tails/(heads + tails))*100
print('The percentage of flips that were tails was {0:.2f}%\n'.format(percent_tails))


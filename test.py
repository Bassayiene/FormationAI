import numpy as np
p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]   # normal

sequence = np.random.choice(6, size=10, p=p1) + 1 
for roll in sequence:
        print("rolled %d" % roll)
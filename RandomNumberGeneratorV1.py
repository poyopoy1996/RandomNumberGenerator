import numpy as np 

seed = np.random.default_rng().integers(0, 2**32 - 1) 
rng = np.random.default_rng(seed) 
sample = rng.choice(int(input("Please Input Range:")), size=int(input("Please put the Sample Size:")), replace=False) 
print("\nSeed:", seed) 
print("Samples:", sample)

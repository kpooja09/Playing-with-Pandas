import numpy as np
import pandas as pd 
eps = np.finfo(float).eps

print(eps)

filename = "seed_dataset.csv"

f = open(filename,'r')
data = pd.read_csv(filename, delimiter = ',')
df = pd.DataFrame(data)
print(df)
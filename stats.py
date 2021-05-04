# %%
import pandas as pd
import numpy as np
import os
from pathlib import Path

# %%
rounds = pd.DataFrame()

pathlist = Path('data').rglob('*.csv')

for path in pathlist:
    rounds = rounds.append(pd.read_csv(str(path)))

print(rounds.shape)
# %%
neg_count = len(rounds[rounds.Result == 'Neg'])
print(f'Neg Bias: {round(neg_count*100/len(rounds) - 50, 2)}%')
# %%

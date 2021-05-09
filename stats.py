# %%
import pandas as pd
import numpy as np
import os
import trueskill as ts
from pathlib import Path
from matplotlib import pyplot as plt

# %%
ts_env = ts.TrueSkill(mu=25, sigma=25/3, beta=5, tau=0.3)
ts_env.make_as_global()

# %% read round CSVs
rounds = pd.DataFrame()
pathlist = Path('data').rglob('*.csv')
for path in pathlist:
    rounds = rounds.append(pd.read_csv(str(path)))
print(f'{len(rounds)} rounds loaded.')
rounds

# %% clean
rounds = rounds.replace({'Result': '\d-\d\t+NEG'}, {'Result':'NEG'}, regex=True)
rounds = rounds.replace({'Result': '\d-\d\t+AFF'}, {'Result':'AFF'}, regex=True)
# rounds = rounds.replace({'Aff': '.+&.+'}, {'Aff': ''})
rounds = rounds.dropna(subset=['Aff', 'Neg', 'Result'])
print(f'{len(rounds)} rounds after cleaning.')

# %%
aff_count = len(rounds[rounds.Result == 'Aff']) + len(rounds[rounds.Result == 'AFF'])
neg_count = len(rounds[rounds.Result == 'Neg']) + len(rounds[rounds.Result == 'NEG'])
if (aff_count > neg_count):
    print(f'{round(aff_count*100/(aff_count + neg_count) - 50, 2)}% Aff Bias')
else:
    print(f'{round(100 - aff_count*100/(aff_count + neg_count) - 50, 2)}% Neg Bias')

# %%
ratings = {}
for r in rounds.iterrows():
    if r[1]['Aff'] not in ratings:
        ratings[r[1]['Aff']] = ts.Rating()
    if r[1]['Neg'] not in ratings:
        ratings[r[1]['Neg']] = ts.Rating()
    if r[1]['Result'] == 'Aff':
        ratings[r[1]['Aff']], ratings[r[1]['Neg']] = ts.rate_1vs1(ratings[r[1]['Aff']], ratings[r[1]['Neg']])
    else:
        ratings[r[1]['Neg']], ratings[r[1]['Aff']] = ts.rate_1vs1(ratings[r[1]['Neg']], ratings[r[1]['Aff']])

# %%
teams_ranked = sorted(filter(lambda x: ratings[x].sigma < 2, list(ratings.keys())), key=lambda x: (-ratings[x].mu, ratings[x].sigma))
# teams_ranked = sorted(list(ratings.keys()), key=lambda x: (-(ratings[x].mu-ratings[x].sigma)))
print('TrueSkill Ranks:')
for i in range(50):
    team = teams_ranked[i]
    print(f'{i+1}. {team} ({round(ratings[team].mu, 2)} ± {round(ratings[team].sigma, 2)})')

# %%
for team in ratings:
    plt.hist([x.mu for x in ratings.values()])
# %%
print('Most Active Teams (# of rounds): ')
rounds['Aff'].append(rounds['Neg']).value_counts()[:30]

# %%

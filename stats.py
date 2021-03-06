# %%
import pandas as pd
import numpy as np
import trueskill as ts
from pathlib import Path
from collections import defaultdict
from sklearn.utils import shuffle

# %%
# ts.TrueSkill(backend='mpmath').make_as_global()
# ts_env = ts.TrueSkill(mu=25, sigma=25/3, beta=5, tau=0.3)
# ts_env.make_as_global()

# %% read round CSVs
rounds = pd.DataFrame()
pathlist = Path('data/TOC').rglob('*.csv')
for path in pathlist:
    rounds = rounds.append(pd.read_csv(str(path)))
print(f'{len(rounds)} rounds loaded.')

# %% clean
rounds = rounds.replace({'Result': '\d-\d\t+NEG'}, {'Result':'NEG'}, regex=True)
rounds = rounds.replace({'Result': '\d-\d\t+AFF'}, {'Result':'AFF'}, regex=True)
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
def rate(rounds):
    ratings = {}
    win_loss = defaultdict(lambda: [0,0])
    for r in rounds.iterrows():
        if r[1]['Aff'] not in ratings:
            ratings[r[1]['Aff']] = ts.Rating()
        if r[1]['Neg'] not in ratings:
            ratings[r[1]['Neg']] = ts.Rating()
        if r[1]['Result'] == 'Aff':
            win_loss[r[1]['Aff']][0] += 1
            win_loss[r[1]['Neg']][1] += 1
            ratings[r[1]['Aff']], ratings[r[1]['Neg']] = ts.rate_1vs1(ratings[r[1]['Aff']], ratings[r[1]['Neg']])
        else:
            win_loss[r[1]['Aff']][1] += 1
            win_loss[r[1]['Neg']][0] += 1
            ratings[r[1]['Neg']], ratings[r[1]['Aff']] = ts.rate_1vs1(ratings[r[1]['Neg']], ratings[r[1]['Aff']])
    return ratings, win_loss

ratings, win_loss = rate(rounds)
pool = 100
for i in range(pool-1):
    rounds = shuffle(rounds)
    temp, _ = rate(rounds)
    ratings = {team : ts.Rating(mu=(temp[team].mu + ratings[team].mu), sigma=(temp[team].sigma + ratings[team].sigma)) for team in temp}
ratings = {team : ts.Rating(mu=(ratings[team].mu/pool), sigma=(ratings[team].sigma/pool)) for team in ratings}

# %%
teams_ranked = sorted(filter(lambda x: ratings[x].sigma < 2.25, list(ratings.keys())), key=lambda x: (-ratings[x].mu, ratings[x].sigma))
labels = ('Team', 'TrueSkill', 'Wins', 'Losses', 'Win Percentage')
df = pd.DataFrame(columns=labels)
print('TrueSkill Ranks:')
for i, team in enumerate(teams_ranked):
    row = pd.Series([team, f'{round(ratings[team].mu, 2)} ?? {round(ratings[team].sigma, 2)}', win_loss[team][0], win_loss[team][1], f'{round(win_loss[team][0]*100/(win_loss[team][0]+win_loss[team][1]), 2)}%'], index=labels)
    df = df.append(row, ignore_index=True)
df.index = np.arange(1, len(df)+1)
print(df[:100].to_markdown())
df.to_csv(r'output.csv')

# %%
print('Most Active Teams (# of rounds): ')
rounds['Aff'].append(rounds['Neg']).value_counts()[:30]


# %%
print('Most Active Judges (# of rounds):')
labels = ('Judge', '# of rounds', 'Aff Votes', 'Neg Votes')
df = pd.DataFrame(columns=labels)
active = rounds['Judge'].value_counts()[:50]
for judge in active.iteritems():
    row = pd.Series([judge[0], judge[1], len(rounds[(rounds['Judge'] == judge[0]) & (rounds['Result'] == 'Aff')]), len(rounds[(rounds['Judge'] == judge[0]) & (rounds['Result'] == 'Neg')])], index=labels)
    df = df.append(row, ignore_index=True)
df.index = np.arange(1, len(df)+1)
print(df.to_markdown())
# %%

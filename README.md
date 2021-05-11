# TabroomStats2
Python data science stack based rewrite of TabroomStats. Rankings implemented with the TrueSkill algorithm (non-linear). Includes data for 2020-21 TOC bid tournaments.

## HS TOC 20-21
Top 50 Teams by TrueSkill Rating (σ < 2):
|     | Team                         | TrueSkill    |   Wins |   Losses | Win Percentage   |
|----:|:-----------------------------|:-------------|-------:|---------:|-----------------:|
|   1 | Minneapolis South CC         | 39.11 ± 1.78 |     64 |       20 | 76.19%           |
|   2 | Coppell KC                   | 38.66 ± 1.74 |     58 |       20 | 74.36%           |
|   3 | North Broward Prep DR        | 38.47 ± 1.77 |     82 |       25 | 76.64%           |
|   4 | Montgomery Bell MP           | 38.12 ± 1.85 |     37 |       10 | 78.72%           |
|   5 | Lexington BY                 | 37.65 ± 1.79 |     46 |       15 | 75.41%           |
|   6 | Caddo Magnet KL              | 37.39 ± 1.78 |     45 |       18 | 71.43%           |
|   7 | Glenbrook North BM           | 37.3 ± 1.8   |     42 |       17 | 71.19%           |
|   8 | Westminster SB               | 36.95 ± 1.74 |     49 |       24 | 67.12%           |
|   9 | Bellarmine  HM               | 36.77 ± 1.82 |     40 |       17 | 70.18%           |
|  10 | Glenbrook South MJ           | 36.47 ± 1.99 |     23 |       10 | 69.7%            |
|  11 | New Trier HM                 | 36.06 ± 1.78 |     44 |       18 | 70.97%           |
|  12 | Glenbrook North BC           | 35.89 ± 1.87 |     38 |       16 | 70.37%           |
|  13 | Chaminade AH                 | 35.78 ± 1.78 |     36 |       20 | 64.29%           |
|  14 | Glenbrook South JM           | 35.62 ± 1.99 |     28 |       12 | 70.0%            |
|  15 | Bellarmine  IG               | 35.45 ± 1.78 |     45 |       20 | 69.23%           |
|  16 | Peninsula RW                 | 35.32 ± 1.75 |     47 |       22 | 68.12%           |
|  17 | Little Rock Central GR       | 35.14 ± 1.78 |     49 |       24 | 67.12%           |
|  18 | West HS SLC GR               | 35.08 ± 1.75 |     46 |       25 | 64.79%           |
|  19 | New Trier RW                 | 35.06 ± 1.79 |     54 |       20 | 72.97%           |
|  20 | Gunn OS                      | 35.05 ± 1.77 |     56 |       23 | 70.89%           |
|  21 | McQueen LR                   | 35.03 ± 1.84 |     49 |       18 | 73.13%           |
|  22 | Edina AA                     | 35.01 ± 1.75 |     49 |       23 | 68.06%           |
|  23 | Maine East PP                | 34.96 ± 1.82 |     46 |       21 | 68.66%           |
|  24 | Northside  RS                | 34.84 ± 1.8  |     36 |       20 | 64.29%           |
|  25 | CK McClatchy BG              | 34.81 ± 1.82 |     46 |       19 | 70.77%           |
|  26 | Walter Payton MW             | 34.54 ± 1.9  |     32 |       15 | 68.09%           |
|  27 | Greenhill FS                 | 34.51 ± 1.78 |     43 |       18 | 70.49%           |
|  28 | Berkeley Prep KZ             | 34.48 ± 1.75 |     41 |       24 | 63.08%           |
|  29 | Montgomery Bell PC           | 34.43 ± 1.86 |     32 |       15 | 68.09%           |
|  30 | Westminster YL               | 34.29 ± 1.88 |     23 |       13 | 63.89%           |
|  31 | Eagan LS                     | 34.22 ± 1.74 |     42 |       26 | 61.76%           |
|  32 | Pine Crest ER                | 34.21 ± 1.82 |     47 |       22 | 68.12%           |
|  33 | Mamaroneck RM                | 34.2 ± 1.87  |     33 |       14 | 70.21%           |
|  34 | Mamaroneck DR                | 34.09 ± 1.75 |     61 |       28 | 68.54%           |
|  35 | Northview AI                 | 34.07 ± 1.79 |     37 |       20 | 64.91%           |
|  36 | North Broward Prep GG        | 34.06 ± 1.73 |     54 |       33 | 62.07%           |
|  37 | Reagan AG                    | 34.03 ± 1.86 |     46 |       16 | 74.19%           |
|  38 | Meadows HY                   | 34.01 ± 1.77 |     39 |       19 | 67.24%           |
|  39 | Liberal Arts and Science GP  | 33.89 ± 1.74 |     56 |       27 | 67.47%           |
|  40 | Notre Dame KS                | 33.83 ± 1.94 |     26 |       15 | 63.41%           |
|  41 | Little Rock Central LP       | 33.79 ± 1.93 |     24 |       13 | 64.86%           |
|  42 | Peninsula FP                 | 33.78 ± 1.78 |     37 |       22 | 62.71%           |
|  43 | Woodward GR                  | 33.69 ± 1.92 |     29 |       14 | 67.44%           |
|  44 | Westminster BW               | 33.39 ± 1.8  |     38 |       23 | 62.3%            |
|  45 | Washburn Rural PW            | 33.36 ± 1.81 |     34 |       18 | 65.38%           |
|  46 | Valley International Prep AU | 33.24 ± 1.74 |     50 |       26 | 65.79%           |
|  47 | Liberal Arts and Science BR  | 33.16 ± 1.75 |     56 |       28 | 66.67%           |
|  48 | Greenhill GR                 | 33.04 ± 1.78 |     35 |       21 | 62.5%            |
|  49 | SF Roosevelt LT              | 32.94 ± 1.8  |     44 |       20 | 68.75%           |
|  50 | Glenbrook North BG           | 32.92 ± 1.78 |     38 |       22 | 63.33%           |
|  51 | Lexington TK                 | 32.77 ± 1.96 |     27 |       15 | 64.29%           |
|  52 | Georgetown Day BS            | 32.77 ± 1.82 |     36 |       18 | 66.67%           |
|  53 | Stuyvesant NR                | 32.5 ± 1.83  |     42 |       21 | 66.67%           |
|  54 | Notre Dame DN                | 32.5 ± 1.78  |     47 |       23 | 67.14%           |
|  55 | New Trier JW                 | 32.47 ± 1.76 |     43 |       27 | 61.43%           |
|  56 | Westminster KY               | 32.43 ± 1.93 |     28 |       14 | 66.67%           |
|  57 | James Logan BM               | 32.43 ± 1.89 |     34 |       20 | 62.96%           |
|  58 | Westwood NY                  | 32.34 ± 1.81 |     45 |       23 | 66.18%           |
|  59 | Kent Denver CM               | 32.26 ± 1.87 |     35 |       21 | 62.5%            |
|  60 | Notre Dame AY                | 32.21 ± 1.86 |     33 |       17 | 66.0%            |
|  61 | Barstow BM                   | 32.19 ± 1.89 |     29 |       15 | 65.91%           |
|  62 | Shark RW                     | 32.0 ± 1.84  |     39 |       21 | 65.0%            |
|  63 | Georgetown Day MW            | 31.92 ± 1.79 |     30 |       20 | 60.0%            |
|  64 | Liberal Arts and Science HW  | 31.88 ± 1.74 |     47 |       28 | 62.67%           |
|  65 | Georgetown Day BL            | 31.87 ± 1.88 |     31 |       17 | 64.58%           |
|  66 | Archbishop Mitty DR          | 31.85 ± 1.87 |     35 |       18 | 66.04%           |
|  67 | Interlake CP                 | 31.82 ± 1.9  |     27 |       16 | 62.79%           |
|  68 | Bellarmine  MT               | 31.68 ± 1.9  |     28 |       18 | 60.87%           |
|  69 | Oak Park and River Forest SR | 31.65 ± 1.91 |     27 |       17 | 61.36%           |
|  70 | Damien DT                    | 31.61 ± 1.76 |     41 |       28 | 59.42%           |
|  71 | Calvert Hall BL              | 31.58 ± 1.76 |     47 |       27 | 63.51%           |
|  72 | Alpharetta SN                | 31.55 ± 1.86 |     29 |       19 | 60.42%           |
|  73 | Leland LZ                    | 31.17 ± 1.88 |     31 |       17 | 64.58%           |
|  74 | Liberal Arts and Science MC  | 31.11 ± 1.76 |     38 |       26 | 59.38%           |
|  75 | Niles West BB                | 30.98 ± 1.77 |     43 |       30 | 58.9%            |
|  76 | Peninsula MS                 | 30.85 ± 1.81 |     33 |       26 | 55.93%           |
|  77 | Berkeley Prep SS             | 30.83 ± 1.77 |     58 |       37 | 61.05%           |
|  78 | Mamaroneck LP                | 30.77 ± 1.81 |     36 |       24 | 60.0%            |
|  79 | Glenbrook South KK           | 30.75 ± 1.76 |     42 |       27 | 60.87%           |
|  80 | Lowell ST                    | 30.73 ± 1.78 |     39 |       25 | 60.94%           |
|  81 | Westwood CH                  | 30.5 ± 1.77  |     39 |       32 | 54.93%           |
|  82 | Montgomery Bell MH           | 30.3 ± 1.93  |     20 |       16 | 55.56%           |
|  83 | Nevada Union GW              | 30.25 ± 1.81 |     39 |       27 | 59.09%           |
|  84 | Alpharetta NT                | 30.12 ± 1.89 |     27 |       18 | 60.0%            |
|  85 | Glenbrook North KS           | 30.02 ± 1.94 |     29 |       18 | 61.7%            |
|  86 | Presentation BS              | 29.94 ± 1.97 |     18 |       17 | 51.43%           |
|  87 | OES CP                       | 29.92 ± 1.81 |     33 |       23 | 58.93%           |
|  88 | Bronx Science DS             | 29.69 ± 1.99 |     23 |       16 | 58.97%           |
|  89 | Bronx Science CM             | 29.67 ± 1.77 |     48 |       33 | 59.26%           |
|  90 | Sonoma JM                    | 29.62 ± 1.75 |     39 |       32 | 54.93%           |
|  91 | Glenbrook North WY           | 29.56 ± 1.97 |     29 |       17 | 63.04%           |
|  92 | Ferris MC                    | 29.33 ± 1.83 |     27 |       21 | 56.25%           |
|  93 | Damien AD                    | 29.24 ± 1.79 |     38 |       30 | 55.88%           |
|  94 | Jesuit MR                    | 29.14 ± 1.83 |     31 |       29 | 51.67%           |
|  95 | Mamaroneck BO                | 29.12 ± 1.81 |     32 |       26 | 55.17%           |
|  96 | Mamaroneck LS                | 29.06 ± 1.8  |     52 |       39 | 57.14%           |
|  97 | Peninsula LQ                 | 29.06 ± 1.98 |     26 |       15 | 63.41%           |
|  98 | Bronx Science CE             | 28.99 ± 1.86 |     30 |       25 | 54.55%           |
|  99 | Bronx Science FV             | 28.98 ± 1.76 |     36 |       29 | 55.38%           |
| 100 | ADL BT                       | 28.88 ± 1.99 |     23 |       18 | 56.1%            |
  

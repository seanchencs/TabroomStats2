# TabroomStats2
Python data science stack based rewrite of TabroomStats. Rankings implemented with the TrueSkill algorithm (non-linear). Includes data for 2020-21 TOC bid tournaments.

## HS TOC 20-21
Top 100 Teams by TrueSkill Rating (σ < 2, pool = 100):
|     | Team                         | TrueSkill    |   Wins |   Losses | Win Percentage   |
|----:|:-----------------------------|:-------------|-------:|---------:|:-----------------|
|   1 | Minneapolis South CC         | 38.07 ± 1.76 |     64 |       20 | 76.19%           |
|   2 | Montgomery Bell MP           | 37.8 ± 1.91  |     37 |       10 | 78.72%           |
|   3 | North Broward Prep DR        | 37.76 ± 1.78 |     82 |       25 | 76.64%           |
|   4 | Lexington BY                 | 37.33 ± 1.83 |     46 |       15 | 75.41%           |
|   5 | Caddo Magnet KL              | 36.79 ± 1.78 |     45 |       18 | 71.43%           |
|   6 | Glenbrook North BM           | 36.57 ± 1.8  |     42 |       17 | 71.19%           |
|   7 | Coppell KC                   | 36.29 ± 1.78 |     58 |       20 | 74.36%           |
|   8 | Bellarmine  HM               | 36.15 ± 1.82 |     40 |       17 | 70.18%           |
|   9 | New Trier HM                 | 36.11 ± 1.78 |     44 |       18 | 70.97%           |
|  10 | Glenbrook South MJ           | 35.72 ± 2.0  |     23 |       10 | 69.7%            |
|  11 | New Trier RW                 | 35.44 ± 1.79 |     54 |       20 | 72.97%           |
|  12 | Westminster SB               | 35.2 ± 1.73  |     49 |       24 | 67.12%           |
|  13 | Chaminade AH                 | 35.09 ± 1.76 |     36 |       20 | 64.29%           |
|  14 | McQueen LR                   | 34.92 ± 1.82 |     49 |       18 | 73.13%           |
|  15 | CK McClatchy BG              | 34.82 ± 1.8  |     46 |       19 | 70.77%           |
|  16 | Greenhill FS                 | 34.72 ± 1.78 |     43 |       18 | 70.49%           |
|  17 | Glenbrook North BC           | 34.69 ± 1.85 |     38 |       16 | 70.37%           |
|  18 | Glenbrook South JM           | 34.56 ± 1.99 |     28 |       12 | 70.0%            |
|  19 | Peninsula RW                 | 34.56 ± 1.78 |     47 |       22 | 68.12%           |
|  20 | Maine East PP                | 34.37 ± 1.79 |     46 |       21 | 68.66%           |
|  21 | SF Roosevelt LT              | 34.28 ± 1.8  |     44 |       20 | 68.75%           |
|  22 | Edina AA                     | 34.17 ± 1.76 |     49 |       23 | 68.06%           |
|  23 | Mamaroneck RM                | 34.1 ± 1.87  |     33 |       14 | 70.21%           |
|  24 | Bellarmine  IG               | 34.09 ± 1.78 |     45 |       20 | 69.23%           |
|  25 | Berkeley Prep KZ             | 34.06 ± 1.75 |     41 |       24 | 63.08%           |
|  26 | Montgomery Bell PC           | 34.04 ± 1.84 |     32 |       15 | 68.09%           |
|  27 | Reagan AG                    | 34.02 ± 1.85 |     46 |       16 | 74.19%           |
|  28 | Gunn OS                      | 34.01 ± 1.79 |     56 |       23 | 70.89%           |
|  29 | Mamaroneck DR                | 33.97 ± 1.77 |     61 |       28 | 68.54%           |
|  30 | Liberal Arts and Science GP  | 33.91 ± 1.76 |     56 |       27 | 67.47%           |
|  31 | Walter Payton MW             | 33.9 ± 1.87  |     32 |       15 | 68.09%           |
|  32 | Little Rock Central GR       | 33.72 ± 1.78 |     49 |       24 | 67.12%           |
|  33 | Notre Dame DN                | 33.62 ± 1.78 |     47 |       23 | 67.14%           |
|  34 | Pine Crest ER                | 33.47 ± 1.81 |     47 |       22 | 68.12%           |
|  35 | West HS SLC GR               | 33.47 ± 1.76 |     46 |       25 | 64.79%           |
|  36 | Westwood NY                  | 33.41 ± 1.79 |     45 |       23 | 66.18%           |
|  37 | Meadows HY                   | 33.38 ± 1.8  |     39 |       19 | 67.24%           |
|  38 | Little Rock Central LP       | 33.38 ± 1.95 |     24 |       13 | 64.86%           |
|  39 | Notre Dame KS                | 33.37 ± 1.93 |     26 |       15 | 63.41%           |
|  40 | Northside  RS                | 33.28 ± 1.79 |     36 |       20 | 64.29%           |
|  41 | Peninsula FP                 | 33.12 ± 1.79 |     37 |       22 | 62.71%           |
|  42 | Woodward GR                  | 33.1 ± 1.91  |     29 |       14 | 67.44%           |
|  43 | Northview AI                 | 33.03 ± 1.81 |     37 |       20 | 64.91%           |
|  44 | Westminster YL               | 33.01 ± 1.91 |     23 |       13 | 63.89%           |
|  45 | Liberal Arts and Science BR  | 32.75 ± 1.75 |     56 |       28 | 66.67%           |
|  46 | Barstow BM                   | 32.71 ± 1.88 |     29 |       15 | 65.91%           |
|  47 | Washburn Rural PW            | 32.61 ± 1.85 |     34 |       18 | 65.38%           |
|  48 | North Broward Prep GG        | 32.59 ± 1.74 |     54 |       33 | 62.07%           |
|  49 | Eagan LS                     | 32.58 ± 1.76 |     42 |       26 | 61.76%           |
|  50 | Calvert Hall BL              | 32.44 ± 1.76 |     47 |       27 | 63.51%           |
|  51 | Glenbrook North BG           | 32.31 ± 1.8  |     38 |       22 | 63.33%           |
|  52 | Lexington TK                 | 32.28 ± 1.93 |     27 |       15 | 64.29%           |
|  53 | Liberal Arts and Science HW  | 32.23 ± 1.72 |     47 |       28 | 62.67%           |
|  54 | James Logan BM               | 32.21 ± 1.84 |     34 |       20 | 62.96%           |
|  55 | Greenhill GR                 | 32.14 ± 1.8  |     35 |       21 | 62.5%            |
|  56 | Archbishop Mitty DR          | 32.06 ± 1.86 |     35 |       18 | 66.04%           |
|  57 | Georgetown Day BS            | 32.02 ± 1.83 |     36 |       18 | 66.67%           |
|  58 | Interlake CP                 | 31.83 ± 1.9  |     27 |       16 | 62.79%           |
|  59 | Oak Park and River Forest SR | 31.82 ± 1.9  |     27 |       17 | 61.36%           |
|  60 | Westminster KY               | 31.8 ± 1.94  |     28 |       14 | 66.67%           |
|  61 | Valley International Prep AU | 31.75 ± 1.78 |     50 |       26 | 65.79%           |
|  62 | Stuyvesant NR                | 31.65 ± 1.84 |     42 |       21 | 66.67%           |
|  63 | Georgetown Day BL            | 31.53 ± 1.87 |     31 |       17 | 64.58%           |
|  64 | Georgetown Day MW            | 31.53 ± 1.82 |     30 |       20 | 60.0%            |
|  65 | Westminster BW               | 31.51 ± 1.82 |     38 |       23 | 62.3%            |
|  66 | Notre Dame AY                | 31.51 ± 1.86 |     33 |       17 | 66.0%            |
|  67 | New Trier JW                 | 31.41 ± 1.76 |     43 |       27 | 61.43%           |
|  68 | Alpharetta SN                | 31.36 ± 1.86 |     29 |       19 | 60.42%           |
|  69 | Interlake GQ                 | 31.33 ± 1.96 |     20 |       13 | 60.61%           |
|  70 | Bellarmine  MT               | 31.29 ± 1.88 |     28 |       18 | 60.87%           |
|  71 | Leland LZ                    | 31.24 ± 1.9  |     31 |       17 | 64.58%           |
|  72 | CK McClatchy SP              | 31.21 ± 1.96 |     27 |       14 | 65.85%           |
|  73 | Glenbrook South KK           | 31.21 ± 1.76 |     42 |       27 | 60.87%           |
|  74 | Shark RW                     | 31.07 ± 1.85 |     39 |       21 | 65.0%            |
|  75 | Bronx Science CM             | 30.97 ± 1.74 |     48 |       33 | 59.26%           |
|  76 | Berkeley Prep SS             | 30.81 ± 1.75 |     58 |       37 | 61.05%           |
|  77 | Niles West BB                | 30.65 ± 1.78 |     43 |       30 | 58.9%            |
|  78 | Damien DT                    | 30.65 ± 1.78 |     41 |       28 | 59.42%           |
|  79 | Lowell ST                    | 30.55 ± 1.77 |     39 |       25 | 60.94%           |
|  80 | Nevada Union GW              | 30.52 ± 1.78 |     39 |       27 | 59.09%           |
|  81 | Kent Denver CM               | 30.29 ± 1.83 |     35 |       21 | 62.5%            |
|  82 | Mamaroneck LS                | 30.28 ± 1.75 |     52 |       39 | 57.14%           |
|  83 | Liberal Arts and Science MC  | 30.05 ± 1.79 |     38 |       26 | 59.38%           |
|  84 | Montgomery Bell MH           | 29.97 ± 1.96 |     20 |       16 | 55.56%           |
|  85 | Mamaroneck LP                | 29.84 ± 1.81 |     36 |       24 | 60.0%            |
|  86 | Peninsula MS                 | 29.8 ± 1.81  |     33 |       26 | 55.93%           |
|  87 | Glenbrook North WY           | 29.73 ± 1.96 |     29 |       17 | 63.04%           |
|  88 | Westwood CH                  | 29.7 ± 1.78  |     39 |       32 | 54.93%           |
|  89 | Glenbrook North KS           | 29.64 ± 1.92 |     29 |       18 | 61.7%            |
|  90 | Cypress Bay LL               | 29.57 ± 1.88 |     27 |       18 | 60.0%            |
|  91 | Alpharetta NT                | 29.12 ± 1.9  |     27 |       18 | 60.0%            |
|  92 | Sonoma JM                    | 29.05 ± 1.77 |     39 |       32 | 54.93%           |
|  93 | Presentation BS              | 28.98 ± 1.98 |     18 |       17 | 51.43%           |
|  94 | Damien AD                    | 28.69 ± 1.77 |     38 |       30 | 55.88%           |
|  95 | Peninsula LQ                 | 28.62 ± 1.98 |     26 |       15 | 63.41%           |
|  96 | OES CP                       | 28.61 ± 1.84 |     33 |       23 | 58.93%           |
|  97 | Bronx Science CE             | 28.56 ± 1.86 |     30 |       25 | 54.55%           |
|  98 | Mamaroneck BO                | 28.51 ± 1.81 |     32 |       26 | 55.17%           |
|  99 | Jesuit MR                    | 28.43 ± 1.82 |     31 |       29 | 51.67%           |
| 100 | ADL BT                       | 28.26 ± 1.96 |     23 |       18 | 56.1%            |
     
Most Active Judges (# of rounds):  
|    | Judge             |   # of rounds |   Aff Votes |   Neg Votes |
|---:|:------------------|--------------:|------------:|------------:|
|  1 | Tim Freehan       |            71 |          38 |          33 |
|  2 | KJ Reese          |            60 |          30 |          30 |
|  3 | Dhruv Sudesh      |            59 |          31 |          28 |
|  4 | Magi Ortiz        |            56 |          18 |          38 |
|  5 | David Kilpatrick  |            54 |          22 |          32 |
|  6 | David Sposito     |            52 |          20 |          32 |
|  7 | Parth Shah        |            52 |          26 |          26 |
|  8 | Mac Cronin        |            51 |          20 |          31 |
|  9 | Ethan Muse        |            51 |          25 |          26 |
| 10 | Cade Cottrell     |            50 |          22 |          28 |
| 11 | Ansh Khullar      |            50 |          21 |          29 |
| 12 | Cody Morrow       |            48 |          28 |          20 |
| 13 | Daniel Iskhakov   |            48 |          31 |          17 |
| 14 | Maddie Pieropan   |            47 |          17 |          30 |
| 15 | Larry Dang        |            46 |          29 |          17 |
| 16 | Debnil Sur        |            46 |          25 |          21 |
| 17 | Kevin Hirn        |            44 |          23 |          21 |
| 18 | Chris Paredes     |            43 |          19 |          24 |
| 19 | Scott Wheeler     |            42 |          21 |          21 |
| 20 | Nick Pereda       |            42 |          16 |          26 |
| 21 | Robin Forsyth     |            42 |          24 |          18 |
| 22 | H Dylan Willett   |            41 |          22 |          19 |
| 23 | Will Halverson    |            40 |          20 |          20 |
| 24 | Kenny Delph       |            40 |          17 |          23 |
| 25 | Kelly Skoulikaris |            39 |          15 |          24 |
| 26 | Allie Chase       |            39 |          20 |          19 |
| 27 | Misty Tippets     |            39 |          21 |          18 |
| 28 | Dan Stanfield     |            39 |          18 |          21 |
| 29 | Wayne Tang        |            38 |          23 |          15 |
| 30 | Ashton Smith      |            38 |          15 |          23 |
| 31 | Maggie Wells      |            38 |          21 |          17 |
| 32 | Simon Weiss       |            36 |          15 |          21 |
| 33 | Sam Gustavson     |            36 |          20 |          16 |
| 34 | Isaac Segal       |            36 |          16 |          20 |
| 35 | Brianna Aaron     |            36 |          22 |          14 |
| 36 | Tim Ellis         |            35 |          17 |          18 |
| 37 | Nate Graziano     |            35 |          22 |          13 |
| 38 | DJ Williams       |            35 |          20 |          15 |
| 39 | Aidan Kane        |            34 |          20 |          14 |
| 40 | Joshua Gonzalez   |            34 |          15 |          19 |
| 41 | April Ma          |            34 |          15 |          19 |
| 42 | Alex Sherman      |            34 |          17 |          17 |
| 43 | Roman Kezios      |            34 |          20 |          14 |
| 44 | Colton Gilbert    |            33 |          18 |          15 |
| 45 | Cat Jacob         |            33 |          12 |          21 |
| 46 | Yao Yao Chen      |            33 |          15 |          18 |
| 47 | David Coates      |            33 |          18 |          15 |
| 48 | Jack Moore        |            33 |          19 |          14 |
| 49 | Jorman Antigua    |            33 |          15 |          18 |
| 50 | Robert Whitaker   |            32 |          18 |          14 |
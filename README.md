# TabroomStats2
Python data science stack based rewrite of TabroomStats. Rankings implemented with the TrueSkill algorithm (non-linear). Includes data for 2020-21 TOC bid tournaments.

## HS TOC 20-21
Top 100 Teams by TrueSkill Rating (σ < 2, pool = 10):
|     | Team                         | TrueSkill    |   Wins |   Losses | Win Percentage   |
|----:|:-----------------------------|:-------------|-------:|---------:|:-----------------|
|   1 | Minneapolis South CC         | 38.08 ± 1.77 |     64 |       20 | 76.19%           |
|   2 | North Broward Prep DR        | 37.96 ± 1.78 |     82 |       25 | 76.64%           |
|   3 | Montgomery Bell MP           | 37.81 ± 1.91 |     37 |       10 | 78.72%           |
|   4 | Lexington BY                 | 37.55 ± 1.83 |     46 |       15 | 75.41%           |
|   5 | Caddo Magnet KL              | 36.99 ± 1.78 |     45 |       18 | 71.43%           |
|   6 | Glenbrook North BM           | 36.51 ± 1.79 |     42 |       17 | 71.19%           |
|   7 | Coppell KC                   | 36.5 ± 1.77  |     58 |       20 | 74.36%           |
|   8 | New Trier HM                 | 36.0 ± 1.78  |     44 |       18 | 70.97%           |
|   9 | Bellarmine  HM               | 35.88 ± 1.81 |     40 |       17 | 70.18%           |
|  10 | New Trier RW                 | 35.81 ± 1.78 |     54 |       20 | 72.97%           |
|  11 | Glenbrook South MJ           | 35.63 ± 1.99 |     23 |       10 | 69.7%            |
|  12 | Chaminade AH                 | 35.19 ± 1.77 |     36 |       20 | 64.29%           |
|  13 | CK McClatchy BG              | 35.19 ± 1.81 |     46 |       19 | 70.77%           |
|  14 | Westminster SB               | 35.13 ± 1.73 |     49 |       24 | 67.12%           |
|  15 | Greenhill FS                 | 34.98 ± 1.79 |     43 |       18 | 70.49%           |
|  16 | Peninsula RW                 | 34.86 ± 1.76 |     47 |       22 | 68.12%           |
|  17 | Glenbrook North BC           | 34.65 ± 1.87 |     38 |       16 | 70.37%           |
|  18 | McQueen LR                   | 34.63 ± 1.82 |     49 |       18 | 73.13%           |
|  19 | Maine East PP                | 34.51 ± 1.8  |     46 |       21 | 68.66%           |
|  20 | Berkeley Prep KZ             | 34.39 ± 1.76 |     41 |       24 | 63.08%           |
|  21 | Glenbrook South JM           | 34.38 ± 1.99 |     28 |       12 | 70.0%            |
|  22 | Liberal Arts and Science GP  | 34.26 ± 1.74 |     56 |       27 | 67.47%           |
|  23 | Edina AA                     | 34.25 ± 1.75 |     49 |       23 | 68.06%           |
|  24 | Mamaroneck RM                | 34.17 ± 1.88 |     33 |       14 | 70.21%           |
|  25 | Mamaroneck DR                | 34.04 ± 1.77 |     61 |       28 | 68.54%           |
|  26 | Montgomery Bell PC           | 33.91 ± 1.84 |     32 |       15 | 68.09%           |
|  27 | Gunn OS                      | 33.9 ± 1.8   |     56 |       23 | 70.89%           |
|  28 | Walter Payton MW             | 33.89 ± 1.89 |     32 |       15 | 68.09%           |
|  29 | SF Roosevelt LT              | 33.87 ± 1.8  |     44 |       20 | 68.75%           |
|  30 | Bellarmine  IG               | 33.79 ± 1.79 |     45 |       20 | 69.23%           |
|  31 | Meadows HY                   | 33.66 ± 1.8  |     39 |       19 | 67.24%           |
|  32 | Reagan AG                    | 33.63 ± 1.85 |     46 |       16 | 74.19%           |
|  33 | Little Rock Central GR       | 33.63 ± 1.78 |     49 |       24 | 67.12%           |
|  34 | Notre Dame DN                | 33.61 ± 1.77 |     47 |       23 | 67.14%           |
|  35 | Pine Crest ER                | 33.58 ± 1.82 |     47 |       22 | 68.12%           |
|  36 | Little Rock Central LP       | 33.43 ± 1.95 |     24 |       13 | 64.86%           |
|  37 | West HS SLC GR               | 33.36 ± 1.76 |     46 |       25 | 64.79%           |
|  38 | Notre Dame KS                | 33.34 ± 1.92 |     26 |       15 | 63.41%           |
|  39 | Northside  RS                | 33.3 ± 1.79  |     36 |       20 | 64.29%           |
|  40 | Peninsula FP                 | 33.25 ± 1.79 |     37 |       22 | 62.71%           |
|  41 | Woodward GR                  | 33.21 ± 1.92 |     29 |       14 | 67.44%           |
|  42 | Northview AI                 | 33.18 ± 1.81 |     37 |       20 | 64.91%           |
|  43 | Westwood NY                  | 33.04 ± 1.79 |     45 |       23 | 66.18%           |
|  44 | Westminster YL               | 32.92 ± 1.93 |     23 |       13 | 63.89%           |
|  45 | Eagan LS                     | 32.85 ± 1.76 |     42 |       26 | 61.76%           |
|  46 | Washburn Rural PW            | 32.8 ± 1.85  |     34 |       18 | 65.38%           |
|  47 | Liberal Arts and Science BR  | 32.68 ± 1.75 |     56 |       28 | 66.67%           |
|  48 | North Broward Prep GG        | 32.47 ± 1.73 |     54 |       33 | 62.07%           |
|  49 | Glenbrook North BG           | 32.42 ± 1.79 |     38 |       22 | 63.33%           |
|  50 | Lexington TK                 | 32.35 ± 1.92 |     27 |       15 | 64.29%           |
|  51 | Greenhill GR                 | 32.31 ± 1.81 |     35 |       21 | 62.5%            |
|  52 | Calvert Hall BL              | 32.3 ± 1.76  |     47 |       27 | 63.51%           |
|  53 | Barstow BM                   | 32.3 ± 1.89  |     29 |       15 | 65.91%           |
|  54 | James Logan BM               | 32.26 ± 1.85 |     34 |       20 | 62.96%           |
|  55 | Archbishop Mitty DR          | 32.01 ± 1.86 |     35 |       18 | 66.04%           |
|  56 | Stuyvesant NR                | 31.99 ± 1.84 |     42 |       21 | 66.67%           |
|  57 | Westminster KY               | 31.95 ± 1.94 |     28 |       14 | 66.67%           |
|  58 | Oak Park and River Forest SR | 31.87 ± 1.89 |     27 |       17 | 61.36%           |
|  59 | Georgetown Day MW            | 31.84 ± 1.81 |     30 |       20 | 60.0%            |
|  60 | Liberal Arts and Science HW  | 31.8 ± 1.72  |     47 |       28 | 62.67%           |
|  61 | Georgetown Day BS            | 31.73 ± 1.85 |     36 |       18 | 66.67%           |
|  62 | Interlake CP                 | 31.61 ± 1.91 |     27 |       16 | 62.79%           |
|  63 | Valley International Prep AU | 31.59 ± 1.79 |     50 |       26 | 65.79%           |
|  64 | Westminster BW               | 31.58 ± 1.82 |     38 |       23 | 62.3%            |
|  65 | New Trier JW                 | 31.58 ± 1.76 |     43 |       27 | 61.43%           |
|  66 | Georgetown Day BL            | 31.5 ± 1.87  |     31 |       17 | 64.58%           |
|  67 | Bellarmine  MT               | 31.49 ± 1.87 |     28 |       18 | 60.87%           |
|  68 | Notre Dame AY                | 31.4 ± 1.86  |     33 |       17 | 66.0%            |
|  69 | CK McClatchy SP              | 31.32 ± 1.98 |     27 |       14 | 65.85%           |
|  70 | Alpharetta SN                | 31.24 ± 1.86 |     29 |       19 | 60.42%           |
|  71 | Shark RW                     | 31.23 ± 1.84 |     39 |       21 | 65.0%            |
|  72 | Damien DT                    | 31.2 ± 1.78  |     41 |       28 | 59.42%           |
|  73 | Leland LZ                    | 31.01 ± 1.88 |     31 |       17 | 64.58%           |
|  74 | Berkeley Prep SS             | 30.99 ± 1.76 |     58 |       37 | 61.05%           |
|  75 | Interlake GQ                 | 30.96 ± 1.96 |     20 |       13 | 60.61%           |
|  76 | Glenbrook South KK           | 30.84 ± 1.75 |     42 |       27 | 60.87%           |
|  77 | Kent Denver CM               | 30.74 ± 1.83 |     35 |       21 | 62.5%            |
|  78 | Bronx Science CM             | 30.74 ± 1.76 |     48 |       33 | 59.26%           |
|  79 | Lowell ST                    | 30.6 ± 1.79  |     39 |       25 | 60.94%           |
|  80 | Niles West BB                | 30.53 ± 1.77 |     43 |       30 | 58.9%            |
|  81 | Nevada Union GW              | 30.39 ± 1.78 |     39 |       27 | 59.09%           |
|  82 | Liberal Arts and Science MC  | 30.21 ± 1.78 |     38 |       26 | 59.38%           |
|  83 | Westwood CH                  | 30.01 ± 1.78 |     39 |       32 | 54.93%           |
|  84 | Mamaroneck LS                | 30.0 ± 1.75  |     52 |       39 | 57.14%           |
|  85 | Peninsula MS                 | 29.87 ± 1.81 |     33 |       26 | 55.93%           |
|  86 | Glenbrook North WY           | 29.84 ± 1.96 |     29 |       17 | 63.04%           |
|  87 | Mamaroneck LP                | 29.62 ± 1.81 |     36 |       24 | 60.0%            |
|  88 | Glenbrook North KS           | 29.57 ± 1.93 |     29 |       18 | 61.7%            |
|  89 | Montgomery Bell MH           | 29.56 ± 1.97 |     20 |       16 | 55.56%           |
|  90 | Cypress Bay LL               | 29.49 ± 1.88 |     27 |       18 | 60.0%            |
|  91 | Alpharetta NT                | 29.26 ± 1.88 |     27 |       18 | 60.0%            |
|  92 | Presentation BS              | 29.11 ± 1.99 |     18 |       17 | 51.43%           |
|  93 | Sonoma JM                    | 28.92 ± 1.76 |     39 |       32 | 54.93%           |
|  94 | Damien AD                    | 28.9 ± 1.78  |     38 |       30 | 55.88%           |
|  95 | Peninsula LQ                 | 28.88 ± 1.99 |     26 |       15 | 63.41%           |
|  96 | Mamaroneck BO                | 28.8 ± 1.81  |     32 |       26 | 55.17%           |
|  97 | Bronx Science CE             | 28.71 ± 1.86 |     30 |       25 | 54.55%           |
|  98 | Jesuit MR                    | 28.58 ± 1.83 |     31 |       29 | 51.67%           |
|  99 | OES CP                       | 28.54 ± 1.83 |     33 |       23 | 58.93%           |
| 100 | ADL BT                       | 28.41 ± 1.95 |     23 |       18 | 56.1%            |
     
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
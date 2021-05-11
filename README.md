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
  
## NDT-CEDA 2020-21  
Top 100 Teams by TrueSkill Rating (σ < 2, pool = 100):  
|     | Team                        | TrueSkill    |   Wins |   Losses | Win Percentage   |
|----:|:----------------------------|:-------------|-------:|---------:|:-----------------|
|   1 | Michigan PR                 | 33.93 ± 1.21 |     46 |       15 | 75.41%           |
|   2 | Rutgers-Newark AH           | 33.59 ± 1.55 |     27 |        9 | 75.0%            |
|   3 | Kentucky EG                 | 33.18 ± 1.82 |     18 |        7 | 72.0%            |
|   4 | Kansas RM                   | 32.94 ± 1.77 |     16 |        8 | 66.67%           |
|   5 | Northwestern FL             | 32.43 ± 1.88 |     16 |        7 | 69.57%           |
|   6 | Emory GK                    | 32.2 ± 1.21  |     35 |       18 | 66.04%           |
|   7 | Wake Forest KM              | 32.07 ± 1.4  |     27 |       14 | 65.85%           |
|   8 | Michigan MM                 | 31.91 ± 1.2  |     40 |       18 | 68.97%           |
|   9 | Kansas MS                   | 31.42 ± 1.52 |     24 |       11 | 68.57%           |
|  10 | Wake Forest FH              | 31.41 ± 1.49 |     24 |       12 | 66.67%           |
|  11 | Harvard AH                  | 31.38 ± 1.69 |     17 |        9 | 65.38%           |
|  12 | Wake Forest BD              | 31.34 ± 1.5  |     22 |       11 | 66.67%           |
|  13 | Dartmouth TV                | 31.15 ± 1.1  |     38 |       27 | 58.46%           |
|  14 | UC Berkeley BW              | 31.01 ± 1.36 |     27 |       15 | 64.29%           |
|  15 | Northwestern FW             | 30.9 ± 1.37  |     23 |       16 | 58.97%           |
|  16 | Michigan PS                 | 30.85 ± 1.11 |     45 |       25 | 64.29%           |
|  17 | Southern California KS      | 30.82 ± 1.18 |     35 |       24 | 59.32%           |
|  18 | Kansas MR                   | 30.81 ± 1.36 |     25 |       16 | 60.98%           |
|  19 | Kentucky DG                 | 30.7 ± 1.46  |     22 |       13 | 62.86%           |
|  20 | Minnesota PR                | 30.67 ± 1.93 |     17 |        7 | 70.83%           |
|  21 | Louisville BY               | 30.58 ± 1.47 |     22 |       14 | 61.11%           |
|  22 | Harvard AF                  | 30.57 ± 1.55 |     21 |       12 | 63.64%           |
|  23 | UC Berkeley EE              | 30.32 ± 1.19 |     38 |       22 | 63.33%           |
|  24 | Pittsburgh MO               | 30.28 ± 1.75 |     15 |       10 | 60.0%            |
|  25 | Minnesota FR                | 30.22 ± 1.18 |     39 |       21 | 65.0%            |
|  26 | Kansas SM                   | 30.18 ± 1.58 |     21 |       12 | 63.64%           |
|  27 | Texas DW                    | 30.09 ± 1.31 |     32 |       18 | 64.0%            |
|  28 | Georgetown MW               | 30.05 ± 1.19 |     36 |       22 | 62.07%           |
|  29 | Georgetown EN               | 29.92 ± 1.86 |     18 |        8 | 69.23%           |
|  30 | Samford EG                  | 29.77 ± 1.19 |     39 |       21 | 65.0%            |
|  31 | Cal State Fullerton BW      | 29.71 ± 1.22 |     39 |       21 | 65.0%            |
|  32 | Dartmouth MS                | 29.59 ± 1.21 |     34 |       20 | 62.96%           |
|  33 | Emory MS                    | 29.5 ± 1.48  |     23 |       14 | 62.16%           |
|  34 | Pittsburgh OM               | 29.48 ± 1.47 |     22 |       13 | 62.86%           |
|  35 | Pittsburgh LR               | 29.36 ± 1.4  |     24 |       16 | 60.0%            |
|  36 | Kansas BF                   | 29.2 ± 1.25  |     29 |       23 | 55.77%           |
|  37 | Emory PR                    | 29.13 ± 1.29 |     26 |       20 | 56.52%           |
|  38 | Michigan HS                 | 29.0 ± 1.28  |     33 |       19 | 63.46%           |
|  39 | Iowa BR                     | 28.8 ± 1.67  |     16 |       12 | 57.14%           |
|  40 | Emory GM                    | 28.56 ± 1.36 |     24 |       19 | 55.81%           |
|  41 | UNLV RR                     | 28.35 ± 1.23 |     34 |       23 | 59.65%           |
|  42 | George Mason LM             | 28.24 ± 1.18 |     37 |       25 | 59.68%           |
|  43 | NYU ST                      | 28.19 ± 1.25 |     33 |       21 | 61.11%           |
|  44 | Michigan HM                 | 28.16 ± 1.27 |     33 |       21 | 61.11%           |
|  45 | Rochester AM                | 27.96 ± 1.37 |     25 |       19 | 56.82%           |
|  46 | Michigan State GS           | 27.82 ± 1.46 |     21 |       18 | 53.85%           |
|  47 | Emporia State KS            | 27.8 ± 1.3   |     29 |       21 | 58.0%            |
|  48 | Georgetown AG               | 27.71 ± 1.11 |     42 |       30 | 58.33%           |
|  49 | Central Oklahoma CH         | 27.46 ± 1.27 |     29 |       21 | 58.0%            |
|  50 | Dartmouth GS                | 27.46 ± 1.32 |     24 |       22 | 52.17%           |
|  51 | West Georgia DS             | 27.39 ± 1.61 |     15 |       15 | 50.0%            |
|  52 | Purdue SJ                   | 27.31 ± 1.86 |     12 |        9 | 57.14%           |
|  53 | Wake Forest KT              | 27.29 ± 1.63 |     18 |       14 | 56.25%           |
|  54 | Michigan RV                 | 27.2 ± 1.28  |     33 |       24 | 57.89%           |
|  55 | George Mason BG             | 27.05 ± 1.33 |     24 |       21 | 53.33%           |
|  56 | Kansas PS                   | 26.95 ± 1.91 |     12 |       10 | 54.55%           |
|  57 | Liberty WW                  | 26.94 ± 1.08 |     39 |       35 | 52.7%            |
|  58 | Houston FL                  | 26.87 ± 1.78 |     13 |       11 | 54.17%           |
|  59 | Johnson County Community BB | 26.86 ± 1.58 |     18 |       15 | 54.55%           |
|  60 | Michigan State AM           | 26.86 ± 1.29 |     25 |       22 | 53.19%           |
|  61 | Harvard OY                  | 26.84 ± 1.45 |     19 |       17 | 52.78%           |
|  62 | Georgia MW                  | 26.7 ± 1.8   |     12 |       10 | 54.55%           |
|  63 | Baylor Nguyen & Wyatt       | 26.63 ± 1.98 |     15 |       12 | 55.56%           |
|  64 | Michigan State BK           | 26.59 ± 1.44 |     19 |       21 | 47.5%            |
|  65 | Gonzaga HM                  | 26.58 ± 1.29 |     27 |       23 | 54.0%            |
|  66 | Kansas SP                   | 26.52 ± 1.67 |     16 |       13 | 55.17%           |
|  67 | Georgetown LM               | 26.46 ± 1.55 |     16 |       15 | 51.61%           |
|  68 | Kentucky BL                 | 26.44 ± 1.53 |     18 |       17 | 51.43%           |
|  69 | CSU Long Beach CF           | 25.89 ± 1.97 |      8 |       10 | 44.44%           |
|  70 | Liberty CoRo                | 25.89 ± 1.25 |     25 |       26 | 49.02%           |
|  71 | Binghamton AM               | 25.71 ± 1.54 |     17 |       16 | 51.52%           |
|  72 | Wichita State BM            | 25.7 ± 1.73  |     13 |       14 | 48.15%           |
|  73 | Missouri State EG           | 25.64 ± 1.52 |     17 |       17 | 50.0%            |
|  74 | Navy LR                     | 25.57 ± 1.07 |     39 |       40 | 49.37%           |
|  75 | Liberty CaRa                | 25.51 ± 1.81 |     11 |       12 | 47.83%           |
|  76 | Northwestern LS             | 25.41 ± 1.96 |     10 |       11 | 47.62%           |
|  77 | George Mason AS             | 24.99 ± 1.43 |     19 |       20 | 48.72%           |
|  78 | Missouri State KR           | 24.89 ± 1.84 |     10 |       12 | 45.45%           |
|  79 | Kansas SW                   | 24.87 ± 2.0  |      9 |       11 | 45.0%            |
|  80 | Wayne State MR              | 24.84 ± 1.97 |     10 |       12 | 45.45%           |
|  81 | Kentucky DW                 | 24.54 ± 1.53 |     15 |       19 | 44.12%           |
|  82 | Liberty CR                  | 24.41 ± 1.38 |     20 |       24 | 45.45%           |
|  83 | Louisville BD               | 24.4 ± 1.81  |     12 |       14 | 46.15%           |
|  84 | UC Berkeley FQ              | 24.34 ± 1.91 |     10 |       14 | 41.67%           |
|  85 | Wyoming KP                  | 24.07 ± 1.99 |      9 |       11 | 45.0%            |
|  86 | Liberty SW                  | 24.04 ± 1.58 |     17 |       20 | 45.95%           |
|  87 | UT Dallas BK                | 23.84 ± 1.9  |      9 |       12 | 42.86%           |
|  88 | Texas HN                    | 23.77 ± 1.94 |     10 |       11 | 47.62%           |
|  89 | James Madison HS            | 23.74 ± 1.21 |     24 |       34 | 41.38%           |
|  90 | UT Dallas LM                | 23.59 ± 1.5  |     19 |       21 | 47.5%            |
|  91 | Minnesota FM                | 23.4 ± 1.29  |     23 |       31 | 42.59%           |
|  92 | Wyoming MR                  | 23.23 ± 1.49 |     17 |       23 | 42.5%            |
|  93 | Cal State Fullerton RH      | 22.91 ± 1.86 |      9 |       15 | 37.5%            |
|  94 | Harvard/Amherst GM          | 22.24 ± 1.78 |      9 |       17 | 34.62%           |
|  95 | Binghamton PP               | 22.23 ± 1.52 |     15 |       23 | 39.47%           |
|  96 | NYU HP                      | 21.95 ± 1.37 |     20 |       33 | 37.74%           |
|  97 | Samford GT                  | 21.81 ± 1.32 |     20 |       31 | 39.22%           |
|  98 | Wyoming PP                  | 21.47 ± 1.9  |     10 |       15 | 40.0%            |
|  99 | Minnesota GJ                | 21.38 ± 1.97 |      9 |       16 | 36.0%            |
| 100 | Emory NP                    | 20.87 ± 1.83 |     10 |       19 | 34.48%           |  
  
Most Active Judges (# of rounds):  
|    | Judge               |   # of rounds |   Aff Votes |   Neg Votes |
|---:|:--------------------|--------------:|------------:|------------:|
|  1 | Gabriel Morbeck     |            40 |          18 |          22 |
|  2 | Lauren Pepper       |            39 |          21 |          18 |
|  3 | Flynn Makuch        |            35 |          19 |          16 |
|  4 | Will Baker          |            32 |          17 |          15 |
|  5 | Habiba Ahmed        |            32 |          19 |          13 |
|  6 | Michelle Thomas     |            28 |          13 |          15 |
|  7 | Brandon Kelley      |            27 |          14 |          13 |
|  8 | Jackie Poapst       |            27 |          13 |          14 |
|  9 | Genevieve Hackman   |            26 |          11 |          15 |
| 10 | Devane Murphy       |            25 |          16 |           9 |
| 11 | Derek Hilligoss     |            25 |          14 |          11 |
| 12 | Simon Sheaff        |            25 |          13 |          12 |
| 13 | John Turner         |            24 |           9 |          15 |
| 14 | Nathan Fleming      |            23 |          10 |          13 |
| 15 | Timothy Byram       |            23 |           8 |          15 |
| 16 | Josh Lamet          |            23 |          12 |          11 |
| 17 | Pablo Gannon        |            23 |          15 |           8 |
| 18 | Jada Stinnett       |            22 |          13 |           9 |
| 19 | Douglas Husic       |            22 |          16 |           6 |
| 20 | Brett Bricker       |            22 |          11 |          11 |
| 21 | David Kilpatrick    |            22 |           9 |          13 |
| 22 | Rebecca Steiner     |            22 |          11 |          11 |
| 23 | Young Kwon          |            22 |          13 |           9 |
| 24 | Anthony Joseph      |            22 |          15 |           7 |
| 25 | Michael Barlow      |            22 |           9 |          13 |
| 26 | Miles Gray          |            21 |           5 |          16 |
| 27 | Jenna Bauer         |            21 |           9 |          12 |
| 28 | Tyler Wiseman       |            20 |           8 |          12 |
| 29 | V Keenan            |            20 |           7 |          13 |
| 30 | Christopher Jackson |            20 |          14 |           6 |
| 31 | Will Katz           |            20 |          12 |           8 |
| 32 | Sean Kennedy        |            20 |           8 |          12 |
| 33 | Marquis Ard         |            19 |          11 |           8 |
| 34 | Jefferson Yahom     |            19 |           6 |          13 |
| 35 | Brianna Thomas      |            19 |           7 |          12 |
| 36 | Matt Harkins        |            19 |           9 |          10 |
| 37 | Nyx Moore           |            19 |           7 |          12 |
| 38 | Ryan Galloway       |            18 |           9 |           9 |
| 39 | Connor Munsinger    |            18 |           6 |          12 |
| 40 | Armands Revelins    |            18 |           7 |          11 |
| 41 | Hannah Call         |            18 |          13 |           5 |
| 42 | Parker Hopkins      |            18 |           6 |          12 |
| 43 | Lincoln Garrett     |            17 |          13 |           4 |
| 44 | Caitlin Walrath     |            17 |           8 |           9 |
| 45 | Ezra Louvis         |            17 |          11 |           6 |
| 46 | Vladimir Pavlov     |            17 |           9 |           8 |
| 47 | Jazmine Pickens     |            16 |           6 |          10 |
| 48 | Victoria Yonter     |            16 |           4 |          12 |
| 49 | Jesse Keleman       |            16 |           7 |           9 |
| 50 | Nate Graziano       |            16 |           6 |          10 |
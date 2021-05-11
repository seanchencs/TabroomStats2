# TabroomStats2
Python data science stack based rewrite of TabroomStats. Rankings implemented with the TrueSkill algorithm (non-linear). Includes data for 2020-21 TOC bid tournaments.

## HS TOC 20-21
Top 50 Teams by TrueSkill Rating (σ < 2):
|    | Team                         | TrueSkill    |   Wins |   Losses |
|---:|:-----------------------------|:-------------|-------:|---------:|
|  1 | Minneapolis South CC         | 39.11 ± 1.78 |     64 |       20 |
|  2 | Coppell KC                   | 38.66 ± 1.74 |     58 |       20 |
|  3 | North Broward Prep DR        | 38.47 ± 1.77 |     82 |       25 |
|  4 | Montgomery Bell MP           | 38.12 ± 1.85 |     37 |       10 |
|  5 | Lexington BY                 | 37.65 ± 1.79 |     46 |       15 |
|  6 | Caddo Magnet KL              | 37.39 ± 1.78 |     45 |       18 |
|  7 | Glenbrook North BM           | 37.3 ± 1.8   |     42 |       17 |
|  8 | Westminster SB               | 36.95 ± 1.74 |     49 |       24 |
|  9 | Bellarmine  HM               | 36.77 ± 1.82 |     40 |       17 |
| 10 | Glenbrook South MJ           | 36.47 ± 1.99 |     23 |       10 |
| 11 | New Trier HM                 | 36.06 ± 1.78 |     44 |       18 |
| 12 | Glenbrook North BC           | 35.89 ± 1.87 |     38 |       16 |
| 13 | Chaminade AH                 | 35.78 ± 1.78 |     36 |       20 |
| 14 | Glenbrook South JM           | 35.62 ± 1.99 |     28 |       12 |
| 15 | Bellarmine  IG               | 35.45 ± 1.78 |     45 |       20 |
| 16 | Peninsula RW                 | 35.32 ± 1.75 |     47 |       22 |
| 17 | Little Rock Central GR       | 35.14 ± 1.78 |     49 |       24 |
| 18 | West HS SLC GR               | 35.08 ± 1.75 |     46 |       25 |
| 19 | New Trier RW                 | 35.06 ± 1.79 |     54 |       20 |
| 20 | Gunn OS                      | 35.05 ± 1.77 |     56 |       23 |
| 21 | McQueen LR                   | 35.03 ± 1.84 |     49 |       18 |
| 22 | Edina AA                     | 35.01 ± 1.75 |     49 |       23 |
| 23 | Maine East PP                | 34.96 ± 1.82 |     46 |       21 |
| 24 | Northside  RS                | 34.84 ± 1.8  |     36 |       20 |
| 25 | CK McClatchy BG              | 34.81 ± 1.82 |     46 |       19 |
| 26 | Walter Payton MW             | 34.54 ± 1.9  |     32 |       15 |
| 27 | Greenhill FS                 | 34.51 ± 1.78 |     43 |       18 |
| 28 | Berkeley Prep KZ             | 34.48 ± 1.75 |     41 |       24 |
| 29 | Montgomery Bell PC           | 34.43 ± 1.86 |     32 |       15 |
| 30 | Westminster YL               | 34.29 ± 1.88 |     23 |       13 |
| 31 | Eagan LS                     | 34.22 ± 1.74 |     42 |       26 |
| 32 | Pine Crest ER                | 34.21 ± 1.82 |     47 |       22 |
| 33 | Mamaroneck RM                | 34.2 ± 1.87  |     33 |       14 |
| 34 | Mamaroneck DR                | 34.09 ± 1.75 |     61 |       28 |
| 35 | Northview AI                 | 34.07 ± 1.79 |     37 |       20 |
| 36 | North Broward Prep GG        | 34.06 ± 1.73 |     54 |       33 |
| 37 | Reagan AG                    | 34.03 ± 1.86 |     46 |       16 |
| 38 | Meadows HY                   | 34.01 ± 1.77 |     39 |       19 |
| 39 | Liberal Arts and Science GP  | 33.89 ± 1.74 |     56 |       27 |
| 40 | Notre Dame KS                | 33.83 ± 1.94 |     26 |       15 |
| 41 | Little Rock Central LP       | 33.79 ± 1.93 |     24 |       13 |
| 42 | Peninsula FP                 | 33.78 ± 1.78 |     37 |       22 |
| 43 | Woodward GR                  | 33.69 ± 1.92 |     29 |       14 |
| 44 | Westminster BW               | 33.39 ± 1.8  |     38 |       23 |
| 45 | Washburn Rural PW            | 33.36 ± 1.81 |     34 |       18 |
| 46 | Valley International Prep AU | 33.24 ± 1.74 |     50 |       26 |
| 47 | Liberal Arts and Science BR  | 33.16 ± 1.75 |     56 |       28 |
| 48 | Greenhill GR                 | 33.04 ± 1.78 |     35 |       21 |
| 49 | SF Roosevelt LT              | 32.94 ± 1.8  |     44 |       20 |
| 50 | Glenbrook North BG           | 32.92 ± 1.78 |     38 |       22 |
  
Most Active Teams (# of rounds):   
North Broward Prep DR           107  
Berkeley Prep SS                 95  
Mamaroneck LS                    91  
Mamaroneck DR                    89  
North Broward Prep GG            87  
Liberal Arts and Science BR      84  
Peninsula LL                     84  
Minneapolis South CC             84  
Liberal Arts and Science GP      83  
Bronx Science CM                 81  
Gunn OS                          79  
Coppell KC                       78  
Valley International Prep AU     76  
Liberal Arts and Science HW      75  
New Trier RW                     74  
Calvert Hall BL                  74  
Little Rock Central GR           73  
Niles West BB                    73  
Westminster SB                   73  
Edina AA                         72  
Sonoma JM                        71  
Westwood CH                      71  
West HS SLC GR                   71  
Notre Dame DN                    70  
New Trier JW                     70  
Pine Crest ER                    69  
Damien DT                        69  
Glenbrook South KK               69  
Peninsula RW                     69  
Peninsula OP                     68  
  
Most Active Judges (# of rounds):  
Tim Freehan          71  
KJ Reese             60  
Dhruv Sudesh         59  
Magi Ortiz           56  
David Kilpatrick     54  
Parth Shah           52  
David Sposito        52  
Mac Cronin           51  
Ethan Muse           51  
Cade Cottrell        50  
Ansh Khullar         50  
Daniel Iskhakov      48  
Cody Morrow          48  
Maddie Pieropan      47  
Larry Dang           46  
Debnil Sur           46  
Kevin Hirn           44  
Chris Paredes        43  
Scott Wheeler        42  
Robin Forsyth        42  
Nick Pereda          42  
H Dylan Willett      41  
Kenny Delph          40  
Will Halverson       40  
Dan Stanfield        39  
Allie Chase          39  
Kelly Skoulikaris    39  
Misty Tippets        39  
Wayne Tang           38  
Ashton Smith         38  
  

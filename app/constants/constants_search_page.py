#################################################################
TITLES = [
    "*** GENERAL INFO ***",
    "*** STATS ***",
    "*** Upcoming Fights ***",
    "*** Career History ***",
]

LEFT_SEARCH_BOX_TITLE = "---------------- Search Fighter ----------------"
LEFT_DB_BOX_TITLE = "-------------------- Database --------------------"
LEFT_SORT_BOX_TITLE = "-------------------- Sort by -----------------------"

#################################################################
INFO_TEXT_NAMES = [
    '\tName: ', '\t Alias: ', f"{8*' '}Nationality: ",
    f"{12*' '}Affilation: ", f"{16*' '}Height: ", f"{15*' '}Weight: ",
    f"{21*' '}Age: ", f"{19*' '}Born: ", f"{5*' '}Recent fight: ",
    f"{10*' '}First fight: ", f"{4*' '}Fightning for: ",
    'Fights: ', 'Pro MMA record (w/l/d): ', 'Last streak: ',
    'Wins: ', 'Losses: ',  'Draws / No contest: ',
    'By KO/TKO: ', 'By SUB: ', 'By DEC: ',
    'BY KO/TKO: ', 'BY SUB: ', 'BY DEC: ',
]
INFO_TEXT_X_VALUES = [
    10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 600, 600,
    600, 600, 600, 600, 635, 635, 635, 635, 635, 635
]
INFO_TEXT_Y_VALUES = [
    76, 103, 130, 157, 184, 211, 238, 265, 292, 319, 346, 73,
    100, 127, 154, 246, 348, 177, 199, 221, 271, 293, 315
]

#################################################################
INFO_ENTRY_NAMES = [
    'f_name', 'f_alias', 'f_nationality', 'f_affilation',
    'f_height', 'f_weight', 'f_age', 'f_born', 'f_recent',
    'f_first', 'f_age2', 'f_fights', 'f_mma_record', 'f_streak',
]
INFO_ENTRY_X_VALUES = (
    145, 145, 145, 145, 145, 145, 145,
    145, 145, 145, 145, 815, 815, 815,
)
INFO_ENTRY_Y_VALUES = (
    78, 105, 132, 159, 186, 213, 240,
    267, 294, 321, 348, 78, 105, 132
)

#################################################################
STAT_ENTRY_NAMES = [
    'f_w_ko', 'f_w_ko_perc', 'f_w_sub',
    'f_w_sub_perc', 'f_w_dec', 'f_w_dec_perc',
    'f_l_ko', 'f_l_ko_perc', 'f_l_sub',
    'f_l_sub_perc', 'f_l_dec', 'f_l_dec_perc'
]
STAT_ENTRY_X_VALUES = (
    815, 1005, 815, 1005, 815, 1005,
    815, 1005, 815, 1005, 815, 1005,
)
STAT_ENTRY_Y_VALUES = (
    177, 177, 199, 199, 221, 221,
    273, 273, 295, 295, 317, 317
)
ENTRY_ABBREVIATIONS = (
    '', '', '', '', ' CM', ' KG', ' years', '', '', '', ' years',
    '', '', '', '', '%', '', '%', '', '%', '', '%', '', '%', '', '%', '',
)

#################################################################
BAR_NAMES = [
    'f_w_ko_bar', 'f_w_sub_bar', 'f_w_dec_bar',
    'f_l_ko_bar', 'f_l_sub_bar', 'f_l_dec_bar'
]

STAT_PERC_ENTRY_NAMES = [
    'f_w_ko_perc', 'f_w_sub_perc', 'f_w_dec_perc',
    'f_l_ko_perc', 'f_l_sub_perc',  'f_l_dec_perc'
]

#################################################################
SORT_BOX_VARIANTS = [
    f"{28*'*'}  AGE  {28*'*'}",
    "AGE:    Young-old", "AGE:    Old-young",
    "AGE:    <=20", "AGE:    20-30", "AGE:    30-40", "AGE:    40+",

    f"{26*'*'}  HEIGHT  {26*'*'}",
    "HEIGHT:    Small-high", "HEIGHT:    High-small",
    "HEIGHT:    <=170", "HEIGHT:    171-180", "HEIGHT:    181-190", "HEIGHT:    190+",

    f"{26*'*'}  WEIGHT  {25*'*'}",
    "WEIGHT:    Light-heavy", "WEIGHT:    Heavy-light",
    "WEIGHT:    <=70", "WEIGHT:    71-80", "WEIGHT:    80-99", "WEIGHT:    100+",

    f"{26*'*'}  FIGHTS  {26*'*'}",
    "AMOUNT:    Low-high", "AMOUNT:    High-low",
    "AMOUNT:    <=10", "AMOUNT:    11-25", "AMOUNT:    26+",

    f"{21*'*'}  YEARS OF FIGHT  {21*'*'}",
    "YEARS:    Low-high", "YEARS:    High-low",
    "YEARS:    <=4", "YEARS:    5-14", "YEARS:    15+",

    f"{25*'*'}  STREAK  {26*'*'}",
    "STREAK:    WIN", "STREAK:    LOSS",

    f"{18*'*'}  WINS/LOSSES DETAILS  {17*'*'}",
    "WINS:    KO/TKO", "WINS:    SUB", "WINS:    DEC",
    "LOSSES:    KO/TKO", "LOSSES:    SUB", "LOSSES:    DEC",

    f"{23*'*'}  NATIONALITY  {23*'*'}",
    "NAT:    Poland", "NAT:    USA", "NAT:    Brazil",
    "NAT:    France", "NAT:    England", "NAT:    Russia",
]

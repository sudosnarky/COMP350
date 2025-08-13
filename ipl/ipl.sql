
create table if not exists matches (
    id INTEGER,
    city TEXT,
    date TEXT,
    season TEXT,
    match_number TEXT,
    team1 TEXT,
    team2 TEXT,
    venue TEXT,
    toss_winner TEXT,
    toss_decision TEXT,
    super_over TEXT,
    winning_team TEXT,
    won_by TEXT,
    margin INTEGER,
    method TEXT,
    player_of_match TEXT,
    team1players TEXT,
    team2players TEXT,
    umpire1 TEXT,
    umpire2 TEXT
);

create table if not exists deliveries (
    id INTEGER,
    innings INTEGER,
    overs INTEGER,
    ballnumber INTEGER,
    batter TEXT,
    bowler TEXT,
    nonstriker TEXT,
    extra_type TEXT,
    batsman_run INTEGER,
    extras_run INTEGER,
    total_run INTEGER,
    non_boundary INTEGER,
    is_wicket_delivery INTEGER,
    player_out TEXT,
    kind TEXT,
    fielders_involved TEXT,
    batting_team TEXT
);

.mode csv
.import --skip 1 IPL_Matches_2008_2022.csv matches
.import --skip 1 IPL_Ball_by_Ball_2008_2022.csv deliveries


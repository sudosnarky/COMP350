from typing import NamedTuple
import pickle


class Match(NamedTuple):
    row_id: int
    id: int
    city: str
    date: str
    season: str
    match_number: int
    team1: str
    team2: str
    venue: str
    toss_winner: str
    toss_decision: str
    super_over: str
    winning_team: str
    won_by: str
    margin: int
    method: str
    player_of_match: str
    team1_players: str
    team2_players: str
    umpire1: str
    umpire2: str


def as_set(players: str) -> set[str]:
    """
    The `team1_players` and `team2_players` are given as a string representation
    of python list of strings - formatted like "['R Ashwin', 'F Du Plessis', ...]".
    This converts that string into a set of player names.
    """
    return set(s[1:-1] for s in players[1:-1].split(", "))


class Delivery(NamedTuple):
    row_id: int
    id: int
    innings: int
    overs: int
    ballnumber: int
    batter: str
    bowler: str
    nonstriker: str
    extra_type: str
    batsman_run: int
    extras_run: int
    total_run: int
    non_boundary: int
    is_wicket_delivery: int
    player_out: str
    kind: str
    fielders_involved: str
    batting_team: str


def csv2tuples(file, tupleclass):
    import pandas as pd

    return [tupleclass(row_id, *row) for (row_id, row) in pd.read_csv(file).iterrows()]


matches: list[Match] = csv2tuples("IPL_Matches_2008_2022.csv", Match)
deliveries: list[Delivery] = csv2tuples("IPL_Ball_by_Ball_2008_2022.csv", Delivery)

from ipl import Match, matches, Delivery, deliveries
from typing import NamedTuple


def all_participating_teams(year: str) -> list[str]:
    """
    Given the year, return a list of names of teams
    that participated in that year's IPL. You have the
    `matches` and `deliveries` lists to use.

    matches: list[Match]
    deliveries: list[Delivery]

    - first find how you'll locate the data pertaining
      to a particular IPL year. It might be known by a
      different name.
    """
    return []


def bowlers_in_team(year: str, team: str) -> list[str]:
    """
    Given a team name and a year, give a list of all
    the bowlers on the team for that year.
    """
    return []


def matches_played_by(team: str, year: str) -> list[int]:
    """
    Given a team name and the IPL year, compute the list
    of ids of the matches that they played in.
    """
    return []


class RunsInOver(NamedTuple):
    match_id: int
    innings: int
    over: int
    total_runs: int


def runs_each_over(match_id: int) -> list[RunsInOver]:
    """
    Given a match identified by its match id, produce a list
    of overs in sequence and the total runs in the over for
    each of the innings played.
    """
    return []


class BowlerMaxRuns(NamedTuple):
    year: str
    name: str
    max_runs: int


def max_runs_by_bowler(year: str) -> list[BowlerMaxRuns]:
    """
    In a particular IPL year, for each bowler who bowled, find
    the maximum runs they gave across all of the overs they bowled.
    """
    return []


def number_of_overs_by_bowler(year: str, bowler: str) -> int:
    """
    Given the name of the bowler and a year, find the total
    number of overs they bowled in all matches that year.
    """
    return 0


def bowling_average(bowler: str, year: str | None) -> float:
    """
    For a given year, find the average runs given by the bowler across
    all matches. If `year` happens to be `None`, then find the
    average for the bowler across all years.
    """
    return 0.0


class OversBowled(NamedTuple):
    bowler: str
    overs: int


def top_n_bowlers(n: int) -> list[OversBowled]:
    """
    For a given n, find the top-n bowlers by the number of overs
    they bowled across all of IPL. Sort the result in descending
    order of the number of overs.
    """
    return []

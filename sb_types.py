from typing import TypedDict, NotRequired


class Record(TypedDict):
    wins: int
    losses: int
    ties: int
    winrate: float


class MeanSD(TypedDict):
    mean: float
    sd: float


class Rank(TypedDict):
    rank: int
    percentile: float
    team_count: int


class Ranks(TypedDict):
    total: Rank
    country: Rank
    state: NotRequired[Rank]
    district: NotRequired[Rank]


class Stats(TypedDict):
    start: float
    pre_champs: float
    max: float


class EPA(TypedDict):
    total_points: MeanSD
    unitless: float
    norm: float
    conf: list[float]
    breakdown: dict[str, float]
    stats: Stats
    ranks: Ranks


class Competing(TypedDict):
    this_week: bool
    next_event_key: str | None
    next_event_name: str | None
    next_event_week: int | None


class TeamYear(TypedDict):
    team: int
    year: int
    name: str
    country: str
    state: str | None
    district: str | None
    rookie_year: int
    epa: EPA
    record: Record
    district_points: int
    district_rank: int
    competing: Competing

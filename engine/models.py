from dataclasses import dataclass, field
from typing import List


@dataclass
class Day:

    day: int
    title: str
    start: str
    destination: str
    distance_km: int
    ride_time: str

    fuel_stops: list = field(default_factory=list)

    lunch: dict = field(default_factory=dict)

    sights: list = field(default_factory=list)

    tips: list = field(default_factory=list)

    coordinates: dict = field(default_factory=dict)


@dataclass
class Project:
    name: str
    version: str
    language: str
    theme: str
    days: List[Day] = field(default_factory=list)

    def summary(self):
        return (
            f"Project : {self.name}\n"
            f"Version : {self.version}\n"
            f"Language: {self.language}\n"
            f"Theme   : {self.theme}\n"
            f"Days    : {len(self.days)}"
        )
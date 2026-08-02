
from dataclasses import dataclass

@dataclass
class Day:

    day: int
    title: str
    start: str
    destination: str
    distance_km: int
    ride_time: str

    def summary(self):

        return (
            f"Dag {self.day}\n"
            f"{self.title}\n"
            f"{self.distance_km} km\n"
            f"{self.ride_time}"
        )

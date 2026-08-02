
import yaml

from engine.day import Day

class DayLoader:

    def __init__(self, path):
        self.path = path

    def load(self):

        with open(self.path, encoding="utf-8") as f:

            data = yaml.safe_load(f)

        return Day(

            day=data["day"],

            title=data["title"],

            start=data["start"],

            destination=data["destination"],

            distance_km=data["distance_km"],

            ride_time=data["ride_time"]

        )

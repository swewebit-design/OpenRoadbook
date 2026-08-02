
import yaml

from engine.day import Day

class DayLoader:

    def __init__(self, path):
        self.path = path

    def load(self):

        with open(self.path, encoding="utf-8") as f:

            data = yaml.safe_load(f)

        return Day(
    day=day_data["day"],
    title=day_data["title"],
    start=day_data["start"],
    destination=day_data["destination"],
    distance_km=day_data["distance_km"],
    ride_time=day_data["ride_time"],
    fuel_stops=day_data.get("fuel_stops", []),
    lunch=day_data.get("lunch", {}),
    sights=day_data.get("sights", []),
    tips=day_data.get("tips", []),
    coordinates=day_data.get("coordinates", {})
)

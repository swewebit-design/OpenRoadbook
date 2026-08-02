from pathlib import Path
import yaml

from engine.models import Project, Day


class ProjectLoader:

    def __init__(self, project_path):
        self.project_path = Path(project_path)

    def load(self):

        with open(
            self.project_path / "project.yaml",
            encoding="utf-8"
        ) as f:
            data = yaml.safe_load(f)

        days = []

        for day_file in data["days"]:

            with open(
                self.project_path / "days" / day_file,
                encoding="utf-8"
            ) as f:
                day_data = yaml.safe_load(f)

            days.append(
                Day(
                    day=day_data["day"],
                    title=day_data["title"],
                    start=day_data["start"],
                    destination=day_data["destination"],
                    distance_km=day_data["distance_km"],
                    ride_time=day_data["ride_time"],

                    fuel_stops=day_data.get(
                        "fuel_stops",
                        []
                    ),

                    lunch=day_data.get(
                        "lunch",
                        {}
                    ),

                    sights=day_data.get(
                        "sights",
                        []
                    ),

                    tips=day_data.get(
                        "tips",
                        []
                    ),

                    coordinates=day_data.get(
                        "coordinates",
                        {}
                    ),

                    waypoints=day_data.get(
                        "waypoints",
                        []
                    )
                )
            )

        return Project(
            name=data["name"],
            version=data["version"],
            language=data["language"],
            theme=data["theme"],
            days=days
        )
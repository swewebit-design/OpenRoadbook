from pathlib import Path
import gpxpy
import gpxpy.gpx


class GPXBuilder:

    def __init__(self, output_path):

        self.output_path = Path(output_path)

        self.output_path.mkdir(
            exist_ok=True
        )


    def build_day(self, day):

        gpx = gpxpy.gpx.GPX()

        gpx.name = day.title


        # Startpunkt
        start = day.coordinates.get(
            "start",
            {}
        )

        if start:

            gpx.waypoints.append(
                gpxpy.gpx.GPXWaypoint(
                    start.get("lat"),
                    start.get("lon"),
                    name="Start"
                )
            )


        # Egna waypoints
        for point in day.waypoints:

            gpx.waypoints.append(
                gpxpy.gpx.GPXWaypoint(
                    point["lat"],
                    point["lon"],
                    name=point["name"]
                )
            )


        # Målpunkt
        destination = day.coordinates.get(
            "destination",
            {}
        )

        if destination:

            gpx.waypoints.append(
                gpxpy.gpx.GPXWaypoint(
                    destination.get("lat"),
                    destination.get("lon"),
                    name="Mål"
                )
            )


        filename = (
            self.output_path /
            f"Dag{day.day:02}.gpx"
        )


        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                gpx.to_xml()
            )


        return filename
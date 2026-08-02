from pathlib import Path


class RoadbookBuilder:

    def __init__(self, output_path):

        self.output_path = Path(output_path)

        self.output_path.mkdir(
            exist_ok=True
        )


    def build_day(self, day):

        filename = (
            self.output_path /
            f"Dag{day.day:02}.txt"
        )


        content = f"""
================================
Dag {day.day}

{day.title}

Sträcka:
{day.distance_km} km

Körtid:
{day.ride_time}


Tankstopp:
"""

        for stop in day.fuel_stops:
            content += (
                f"- {stop['name']} "
                f"({stop['km']} km)\n"
            )


        content += """

Lunch:
"""

        if day.lunch:
            content += (
                f"- {day.lunch.get('place','')}\n"
            )


        content += """

Sevärdheter:
"""

        for sight in day.sights:
            content += (
                f"- {sight}\n"
            )


        content += """

Tips:
"""

        for tip in day.tips:
            content += (
                f"- {tip}\n"
            )


        filename.write_text(
            content,
            encoding="utf-8"
        )

        return filename
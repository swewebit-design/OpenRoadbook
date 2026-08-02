from pathlib import Path

days_folder = Path(
    "projects/MC_Grand_Tour_2027/days"
)

template = """
day: {day}
title: "Etapp {day}"
start: ""
destination: ""
distance_km: 0
ride_time: ""
"""

for i in range(2, 15):

    file = days_folder / f"day{i:02}.yaml"

    if not file.exists():
        file.write_text(
            template.format(day=i),
            encoding="utf-8"
        )

        print(f"Created {file}")
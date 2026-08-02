
from engine.project_loader import ProjectLoader

loader = ProjectLoader("projects/MC_Grand_Tour_2027")

project = loader.load()

print("="*40)
print("OpenRoadbook v0.2")
print("="*40)

print(project.summary())

from engine.preview import RoadbookPreview

preview = RoadbookPreview()

for day in project.days:

    preview.show_day(day)

from engine.roadbook_builder import RoadbookBuilder


builder = RoadbookBuilder(
    "output"
)


for day in project.days:

    file = builder.build_day(day)

    print(
        f"Skapad: {file}"
    )

from engine.gpx_builder import GPXBuilder


gpx_builder = GPXBuilder(
    "output/gpx"
)


for day in project.days:

    file = gpx_builder.build_day(day)

    print(
        f"GPX skapad: {file}"
    )
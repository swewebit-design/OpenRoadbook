
from engine.project_loader import ProjectLoader

loader = ProjectLoader("projects/MC_Grand_Tour_2027")

project = loader.load()

print("="*40)
print("OpenRoadbook v0.2")
print("="*40)

print(project.summary())

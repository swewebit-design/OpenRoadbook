
from pathlib import Path
import yaml

from engine.models import Project

class ProjectLoader:

    def __init__(self, project_path):
        self.project_path = Path(project_path)

    def load(self):

        with open(self.project_path / "project.yaml", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return Project(
            name=data["name"],
            version=data["version"],
            language=data["language"],
            theme=data["theme"],
            days=data["days"]
        )

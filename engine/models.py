
from dataclasses import dataclass

@dataclass
class Project:
    name: str
    version: str
    language: str
    theme: str
    days: int

    def summary(self):
        return (
            f"Project : {self.name}\n"
            f"Version : {self.version}\n"
            f"Language: {self.language}\n"
            f"Theme   : {self.theme}\n"
            f"Days    : {self.days}"
        )

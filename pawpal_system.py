from dataclasses import dataclass


# -------------------------
# PET MODEL
# -------------------------
@dataclass
class Pet:
    name: str
    species: str
    age: int


# -------------------------
# TASK MODEL
# -------------------------
@dataclass
class Task:
    name: str
    duration: int
    priority: str
    recurring: bool
    completed: bool = False


# -------------------------
# OWNER MODEL
# -------------------------
class Owner:
    def __init__(self, name: str, available_time: int, preferences: list[str] = None):
        self.name = name
        self.available_time = available_time
        self.preferences = preferences or []
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        if pet in self.pets:
            self.pets.remove(pet)


# -------------------------
# SCHEDULER LOGIC
# -------------------------
class Scheduler:
    def __init__(self, tasks: list[Task], available_time: int):
        self.tasks = tasks
        self.available_time = available_time

    def sort_tasks(self) -> list[Task]:
        priority_map = {
            "High": 3,
            "Medium": 2,
            "Low": 1
        }

        return sorted(
            self.tasks,
            key=lambda task: (
                -priority_map.get(task.priority, 0),
                task.duration
            )
        )

    def filter_tasks(self) -> list[Task]:
        sorted_tasks = self.sort_tasks()

        selected_tasks = []
        total_time = 0

        for task in sorted_tasks:
            if total_time + task.duration <= self.available_time:
                selected_tasks.append(task)
                total_time += task.duration

        return selected_tasks

    def generate_plan(self) -> list[Task]:
        return self.filter_tasks()

    def explain_plan(self) -> list[str]:
        plan = self.generate_plan()

        explanations = []
        for task in plan:
            explanations.append(
                f"{task.name} selected because it has {task.priority} priority "
                f"and fits within available time."
            )

        return explanations
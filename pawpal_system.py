from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Pet:
    """Store pet information and the tasks linked to that pet."""

    name: str
    species: str
    age: int
    tasks: list["Task"] = field(default_factory=list)

    def add_task(self, task: "Task") -> None:
        """Add a task to this pet and link it to the pet."""
        self.tasks.append(task)
        task.pet = self

    def remove_task(self, task: "Task") -> None:
        """Remove a task from this pet if it is present."""
        if task in self.tasks:
            self.tasks.remove(task)
            if task.pet is self:
                task.pet = None


@dataclass
class Task:
    """Represent a single pet care activity."""

    name: str
    description: str
    scheduled_time: str
    frequency: str
    priority: str
    duration: int = 30
    completed: bool = False
    pet: Optional["Pet"] = None

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True


class Owner:
    """Manage an owner and the pets they care for."""

    def __init__(self, name: str, available_time: int, preferences: Optional[list[str]] = None):
        """Initialize the owner with basic profile details."""
        self.name = name
        self.available_time = available_time
        self.preferences = preferences or []
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list of pets."""
        if pet not in self.pets:
            self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner's list of pets."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_all_tasks(self) -> list[Task]:
        """Return every task from all of the owner's pets."""
        all_tasks: list[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    """Create a simple daily plan from an owner's tasks."""

    def __init__(self, owner: Owner, available_time: int):
        """Initialize the scheduler with an owner and a time limit."""
        self.owner = owner
        self.available_time = available_time

    def get_pending_tasks(self) -> list[Task]:
        """Return the tasks that are still incomplete."""
        return [task for task in self.owner.get_all_tasks() if not task.completed]

    def sort_tasks(self, tasks: Optional[list[Task]] = None) -> list[Task]:
        """Sort tasks by scheduled time and priority."""
        tasks_to_sort = tasks if tasks is not None else self.get_pending_tasks()
        priority_rank = {"High": 0, "Medium": 1, "Low": 2}

        return sorted(
            tasks_to_sort,
            key=lambda task: (
                task.scheduled_time,
                priority_rank.get(task.priority, 99),
                task.name,
            ),
        )

    def generate_schedule(self) -> list[Task]:
        """Create a daily schedule that fits within the available time."""
        sorted_tasks = self.sort_tasks()
        planned_tasks: list[Task] = []
        total_duration = 0

        for task in sorted_tasks:
            if total_duration + task.duration <= self.available_time:
                planned_tasks.append(task)
                total_duration += task.duration

        return planned_tasks
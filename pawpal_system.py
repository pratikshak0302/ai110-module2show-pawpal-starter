from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
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
    scheduled_date: Optional[date] = None

    def mark_complete(self) -> None:
        """Mark the task complete and create the next recurring task when needed."""
        self.completed = True

        if self.frequency == "Daily" and self.pet is not None:
            next_date = self.scheduled_date + timedelta(days=1) if self.scheduled_date else date.today() + timedelta(days=1)
            recurring_task = Task(
                name=self.name,
                description=self.description,
                scheduled_time=self.scheduled_time,
                frequency=self.frequency,
                priority=self.priority,
                duration=self.duration,
                scheduled_date=next_date,
            )
            self.pet.add_task(recurring_task)
        elif self.frequency == "Weekly" and self.pet is not None:
            next_date = self.scheduled_date + timedelta(days=7) if self.scheduled_date else date.today() + timedelta(days=7)
            recurring_task = Task(
                name=self.name,
                description=self.description,
                scheduled_time=self.scheduled_time,
                frequency=self.frequency,
                priority=self.priority,
                duration=self.duration,
                scheduled_date=next_date,
            )
            self.pet.add_task(recurring_task)


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

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks in chronological order by their scheduled time."""
        def to_minutes(time_value: str) -> int:
            hours, minutes = time_value.split(":")
            return int(hours) * 60 + int(minutes)

        return sorted(tasks, key=lambda task: to_minutes(task.scheduled_time))

    def filter_tasks(self, tasks: list[Task], pet_name: Optional[str] = None, completed: Optional[bool] = None) -> list[Task]:
        """Return tasks matching the selected pet and completion filters."""
        filtered_tasks = list(tasks)

        if pet_name is not None:
            filtered_tasks = [task for task in filtered_tasks if task.pet is not None and task.pet.name == pet_name]

        if completed is not None:
            filtered_tasks = [task for task in filtered_tasks if task.completed is completed]

        return filtered_tasks

    def sort_tasks(self, tasks: Optional[list[Task]] = None) -> list[Task]:
        """Sort tasks by scheduled time and priority."""
        tasks_to_sort = tasks if tasks is not None else self.get_pending_tasks()
        priority_rank = {"High": 0, "Medium": 1, "Low": 2}

        return sorted(
            tasks_to_sort,
            key=lambda task: (
                self._time_to_minutes(task.scheduled_time),
                priority_rank.get(task.priority, 99),
                task.name,
            ),
        )

    def _time_to_minutes(self, time_value: str) -> int:
        """Convert an HH:MM time string into minutes for simple sorting."""
        hours, minutes = time_value.split(":")
        return int(hours) * 60 + int(minutes)

    def detect_conflicts(self, tasks: list[Task]) -> list[str]:
        """Return warnings when multiple tasks share the same scheduled time."""
        grouped_tasks: dict[str, list[Task]] = {}

        # Group tasks by their scheduled time so shared slots are easy to spot.
        for task in tasks:
            grouped_tasks.setdefault(task.scheduled_time, []).append(task)

        warnings: list[str] = []
        for scheduled_time, time_tasks in grouped_tasks.items():
            if len(time_tasks) > 1:
                pet_names = sorted({task.pet.name for task in time_tasks if task.pet is not None})
                if pet_names:
                    warnings.append(
                        f"⚠ Conflict detected: {', '.join(pet_names)} have tasks at {scheduled_time}"
                    )

        return warnings

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
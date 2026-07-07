import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pawpal_system import Owner, Pet, Scheduler, Task


def test_task_mark_complete_updates_status():
    """Verify that marking a task complete changes its status."""
    task = Task(
        name="Feed pet",
        description="Morning meal",
        scheduled_time="08:00",
        frequency="Daily",
        priority="High",
        duration=30,
    )

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_pet_add_task_increases_task_list():
    """Verify that adding a task to a pet updates the pet's task list."""
    pet = Pet(name="Buddy", species="Dog", age=3)
    task = Task(
        name="Walk pet",
        description="Afternoon walk",
        scheduled_time="16:00",
        frequency="Daily",
        priority="Medium",
        duration=45,
    )

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] is task
    assert task.pet is pet


def test_scheduler_sort_and_filter_tasks():
    """Verify that the scheduler can sort tasks by time and filter by pet and status."""
    owner = Owner(name="Ava", available_time=180, preferences=["Morning care"])
    buddy = Pet(name="Buddy", species="Dog", age=3)
    luna = Pet(name="Luna", species="Cat", age=2)
    owner.add_pet(buddy)
    owner.add_pet(luna)

    task1 = Task(name="Feed", description="Feed Buddy", scheduled_time="08:30", frequency="Daily", priority="High", duration=20)
    task2 = Task(name="Walk", description="Walk Buddy", scheduled_time="14:00", frequency="Daily", priority="Medium", duration=30)
    task3 = Task(name="Clean", description="Clean litter", scheduled_time="09:00", frequency="Daily", priority="Low", duration=15, completed=True)

    buddy.add_task(task1)
    buddy.add_task(task2)
    luna.add_task(task3)

    scheduler = Scheduler(owner=owner, available_time=120)

    sorted_tasks = scheduler.sort_by_time(owner.get_all_tasks())
    assert [task.name for task in sorted_tasks] == ["Feed", "Clean", "Walk"]

    filtered_tasks = scheduler.filter_tasks(owner.get_all_tasks(), pet_name="Buddy")
    assert [task.name for task in filtered_tasks] == ["Feed", "Walk"]

    completed_tasks = scheduler.filter_tasks(owner.get_all_tasks(), completed=True)
    assert [task.name for task in completed_tasks] == ["Clean"]


def test_recurring_task_creates_next_occurrence():
    """Verify that completing a recurring task creates a new task for the next day or week."""
    pet = Pet(name="Buddy", species="Dog", age=3)
    task = Task(
        name="Feed",
        description="Morning meal",
        scheduled_time="08:00",
        frequency="Daily",
        priority="High",
        duration=20,
    )
    pet.add_task(task)

    task.mark_complete()

    assert task.completed is True
    assert len(pet.tasks) == 2
    new_task = pet.tasks[1]
    assert new_task.name == "Feed"
    assert new_task.scheduled_date == date.today() + timedelta(days=1)


def test_detect_conflicts_returns_warning_for_shared_time():
    """Verify that overlapping tasks produce a conflict warning."""
    owner = Owner(name="Ava", available_time=180, preferences=["Morning care"])
    buddy = Pet(name="Buddy", species="Dog", age=3)
    luna = Pet(name="Luna", species="Cat", age=2)
    owner.add_pet(buddy)
    owner.add_pet(luna)

    task1 = Task(name="Feed", description="Feed Buddy", scheduled_time="08:00", frequency="Daily", priority="High", duration=20)
    task2 = Task(name="Clean", description="Clean litter", scheduled_time="08:00", frequency="Daily", priority="Medium", duration=15)

    buddy.add_task(task1)
    luna.add_task(task2)

    scheduler = Scheduler(owner=owner, available_time=120)
    warnings = scheduler.detect_conflicts(owner.get_all_tasks())

    assert len(warnings) == 1
    assert "Conflict detected" in warnings[0]

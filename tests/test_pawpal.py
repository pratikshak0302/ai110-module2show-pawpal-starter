import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pawpal_system import Pet, Task


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

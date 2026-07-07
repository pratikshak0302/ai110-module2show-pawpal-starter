from pawpal_system import Owner, Pet, Scheduler, Task


def print_tasks(title: str, tasks: list[Task]) -> None:
    """Print a readable list of tasks with a heading."""
    print(f"\n{title}")
    print("-" * 40)
    if not tasks:
        print("No tasks to show.")
        return

    for task in tasks:
        pet_name = task.pet.name if task.pet else "Unassigned"
        status = "Done" if task.completed else "Pending"
        print(
            f"Time: {task.scheduled_time} | Pet: {pet_name} | "
            f"Task: {task.description} | Priority: {task.priority} | Status: {status}"
        )


def main() -> None:
    """Create a sample PawPal+ setup and demonstrate sorting and filtering."""
    owner = Owner(name="Ava", available_time=180, preferences=["Morning care", "Quick tasks"])

    buddy = Pet(name="Buddy", species="Dog", age=3)
    luna = Pet(name="Luna", species="Cat", age=2)

    owner.add_pet(buddy)
    owner.add_pet(luna)

    feed_buddy = Task(
        name="Feed Buddy",
        description="Morning meal",
        scheduled_time="08:00",
        frequency="Daily",
        priority="High",
        duration=30,
    )
    walk_buddy = Task(
        name="Walk Buddy",
        description="Afternoon walk",
        scheduled_time="08:00",
        frequency="Daily",
        priority="Medium",
        duration=45,
    )
    clean_luna = Task(
        name="Clean Luna",
        description="Clean litter box",
        scheduled_time="08:00",
        frequency="Daily",
        priority="High",
        duration=20,
        completed=True,
    )

    buddy.add_task(feed_buddy)
    buddy.add_task(walk_buddy)
    luna.add_task(clean_luna)

    all_tasks = owner.get_all_tasks()
    scheduler = Scheduler(owner=owner, available_time=120)

    print_tasks("Unsorted Tasks", all_tasks)
    sorted_tasks = scheduler.sort_by_time(all_tasks)
    print_tasks("Sorted Tasks", sorted_tasks)
    filtered_tasks = scheduler.filter_tasks(all_tasks, pet_name="Buddy")
    print_tasks("Filtered Tasks (Buddy)", filtered_tasks)

    schedule = scheduler.generate_schedule()
    print_tasks("Generated Schedule", schedule)

    conflicts = scheduler.detect_conflicts(all_tasks)
    print("\nConflict Warnings")
    print("-" * 40)
    if conflicts:
        for warning in conflicts:
            print(warning)
    else:
        print("No scheduling conflicts found.")


if __name__ == "__main__":
    main()

from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    """Create a sample PawPal+ setup and print today's schedule."""
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
        scheduled_time="16:00",
        frequency="Daily",
        priority="Medium",
        duration=45,
    )
    clean_luna = Task(
        name="Clean Luna",
        description="Clean litter box",
        scheduled_time="12:00",
        frequency="Daily",
        priority="High",
        duration=20,
    )

    buddy.add_task(feed_buddy)
    buddy.add_task(walk_buddy)
    luna.add_task(clean_luna)

    scheduler = Scheduler(owner=owner, available_time=120)
    schedule = scheduler.generate_schedule()

    print("\nToday's Schedule")
    print("-" * 40)
    for task in schedule:
        pet_name = task.pet.name if task.pet else "Unassigned"
        status = "Done" if task.completed else "Pending"
        print(
            f"Time: {task.scheduled_time} | Pet: {pet_name} | "
            f"Task: {task.description} | Priority: {task.priority} | Status: {status}"
        )


if __name__ == "__main__":
    main()

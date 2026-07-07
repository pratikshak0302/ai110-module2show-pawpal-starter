# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

PawPal+ is a beginner-friendly Python project that helps a pet owner organize care tasks for one or more pets. The project combines an object-oriented backend with a simple Streamlit interface so a user can create pets, add tasks, and review a schedule.

## Features

- Task management: Create tasks, attach them to pets, and track whether they are completed.
- Scheduling helpers:
  - Scheduler.sort_by_time() sorts tasks in chronological order.
  - Scheduler.filter_tasks() filters tasks by pet name and/or completion status.
  - Scheduler.detect_conflicts() warns when multiple tasks share the same scheduled time.
- Recurring tasks: Task.mark_complete() creates the next Daily or Weekly task automatically.
- Streamlit UI integration: The app provides forms for adding pets and tasks, then displays the generated schedule and conflict warnings.

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

### Run the CLI demo

```bash
python main.py
```

## Demo Walkthrough

The Streamlit app provides a simple workflow for building a pet-care plan:

- Main UI features: forms for adding pets and tasks, a view of your pets and tasks, and a button to generate a schedule.
- What actions a user can perform: enter basic owner and pet information, assign tasks to a specific pet, set a scheduled time, frequency, priority, and duration, and review the generated schedule.
- Example workflow:
  1. Add owner and pet information.
  2. Add pet care tasks such as feeding, walks, or litter box cleaning.
  3. Generate today's schedule.
  4. Review the sorted tasks and any conflict warnings.

## Sample CLI Output

The CLI demo in main.py creates a simple example setup and prints the tasks, the sorted schedule, and any warnings. A typical run looks like this:

```text
Pets created:
- Buddy (Dog)
- Luna (Cat)

Tasks:
- Feed Buddy at 08:00
- Walk Buddy at 08:00
- Clean Luna at 08:00

Sorted schedule:
- Feed Buddy at 08:00
- Walk Buddy at 08:00

Conflict warning:
- ⚠ Conflict detected: Buddy have tasks at 08:00
```

## Testing PawPal+

Run the automated test suite with:

```bash
python -m pytest
```

The tests cover the core scheduling behaviors, including task completion and recurrence, sorting, filtering, and conflict detection.

Example successful test output:

```text
6 passed in 0.65s
```

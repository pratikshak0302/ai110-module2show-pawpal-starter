# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
Today's Schedule
----------------------------------------
Time: 08:00 | Pet: Buddy | Task: Morning meal | Priority: High | Status: Pending
Time: 12:00 | Pet: Luna | Task: Clean litter box | Priority: High | Status: Pending
Time: 16:00 | Pet: Buddy | Task: Afternoon walk | Priority: Medium | Status: Pending
```

## 🧪 Testing PawPal+

Run the automated test suite with:

```bash
python -m pytest
```

The tests cover the main scheduling behaviors, including:
- Task completion and recurrence logic
- Sorting tasks chronologically
- Filtering tasks
- Conflict detection
- Handling edge cases

Example successful test output:

```text
6 passed in 0.65s
```

Confidence Level: ⭐⭐⭐⭐⭐ (5/5)

This confidence level is based on passing automated tests that cover the main scheduling behaviors in the project.

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.


| Feature            | Method(s)       |Notes                                                                     |
| ------------------ | ------------------------------ | ------------------------------------------------------------------------- |
| Task sorting       | `Scheduler.sort_by_time()`     | Sorts tasks chronologically by their scheduled time.                      |
| Task filtering     | `Scheduler.filter_tasks()`     | Filters tasks by pet name and/or completion status.                       |
| Conflict detection | `Scheduler.detect_conflicts()` | Returns warning messages when multiple tasks share the same time slot.    |
| Recurring tasks    | `Task.mark_complete()`         | Creates the next daily or weekly task when a recurring task is completed. |


## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->

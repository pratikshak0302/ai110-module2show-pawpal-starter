import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs")

# Streamlit is stateless, so session_state is used to keep the owner object between reruns.
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", available_time=180, preferences=["Morning care"])

owner = st.session_state.owner

with st.form("add_pet_form"):
    st.markdown("### Add Pet")
    pet_name = st.text_input("Pet name")
    pet_species = st.selectbox("Species", ["dog", "cat", "other"])
    pet_age = st.number_input("Age", min_value=0, max_value=30, value=1)
    submitted_pet = st.form_submit_button("Add Pet")

    if submitted_pet:
        pet = Pet(name=pet_name, species=pet_species, age=int(pet_age))
        owner.add_pet(pet)
        st.success(f"{pet.name} was added to {owner.name}'s account.")

st.markdown("### Your Pets")
if owner.pets:
    for pet in owner.pets:
        st.write(f"- {pet.name} ({pet.species}, {pet.age} years)")
else:
    st.info("No pets yet. Add one above.")

with st.form("add_task_form"):
    st.markdown("### Add Task")
    if owner.pets:
        pet_names = [pet.name for pet in owner.pets]
        selected_pet_name = st.selectbox("Select pet", pet_names)
        selected_pet = next(pet for pet in owner.pets if pet.name == selected_pet_name)

        task_name = st.text_input("Task name")
        task_description = st.text_input("Description")
        task_time = st.text_input("Scheduled time", value="08:00")
        task_frequency = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])
        task_priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        task_duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
        submitted_task = st.form_submit_button("Add Task")

        if submitted_task:
            task = Task(
                name=task_name,
                description=task_description,
                scheduled_time=task_time,
                frequency=task_frequency,
                priority=task_priority,
                duration=int(task_duration),
            )
            selected_pet.add_task(task)
            st.success(f"{task.name} was added to {selected_pet.name}.")
    else:
        st.info("Add a pet before creating tasks.")
        st.form_submit_button("Add Task", disabled=True)

st.markdown("### Pets and Tasks")
if owner.pets:
    for pet in owner.pets:
        st.write(f"**{pet.name}**")
        if pet.tasks:
            for task in pet.tasks:
                st.write(
                    f"- {task.name}: {task.description} at {task.scheduled_time} "
                    f"({task.priority}, {task.duration} min)"
                )
        else:
            st.write("No tasks yet.")
else:
    st.info("No pets to show tasks for yet.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.warning(
        "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
    )
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )

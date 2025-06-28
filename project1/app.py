import streamlit as st
import requests
import pandas as pd

st.title("Project Management App")

st.header("Add a Developer")

dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Experience (Years)", min_value=0, max_value=50, value=0)

if st.button("Create Developer"):
    if dev_name.strip():
        dev_data = {"name": dev_name.strip(), "experience": dev_experience}
        try:
            response = requests.post("http://localhost:8000/developers/", json=dev_data)
            response.raise_for_status()
            st.success("Developer created successfully.")
            st.json(response.json())
        except requests.exceptions.RequestException as e:
            st.error(f"Error creating developer: {e}")
    else:
        st.warning("Please enter a developer name.")

st.header("Add a Project")

proj_title = st.text_input("Project Title")
proj_desc = st.text_input("Project Description")
proj_lang = st.text_input("Languages Used (Comma-separated)")
lead_dev_name = st.text_input("Lead Developer Name")
lead_dev_exp = st.number_input("Lead Developer Experience (Years)", min_value=0, max_value=50, value=0)

if st.button("Create Project"):
    if proj_title.strip() and lead_dev_name.strip():
        lead_dev_data = {
            "name": lead_dev_name.strip(),
            "experience": lead_dev_exp
        }

        proj_data = {
            "title": proj_title.strip(),
            "description": proj_desc.strip(),
            "language": [lang.strip() for lang in proj_lang.split(",") if lang.strip()],
            "lead_developer": lead_dev_data
        }

        try:
            response = requests.post("http://localhost:8000/projects/", json=proj_data)
            response.raise_for_status()
            st.success("Project created successfully.")
            st.json(response.json())
        except requests.exceptions.RequestException as e:
            st.error(f"Error creating project: {e}")
    else:
        st.warning("Please enter both project title and lead developer name.")

st.header("Project Dashboard")

if st.button("Get Project"):
    try:
        response = requests.get("http://localhost:8000/projects/")
        response.raise_for_status()
        project_data = response.json().get("projects", [])

        if project_data:
            projects_df = pd.DataFrame(project_data)
            st.subheader("Project Overview")
            st.dataframe(projects_df)

            st.subheader("Project Details")
            for project in project_data:
                st.markdown(f"**Title:** {project['title']}")
                st.markdown(f"**Description:** {project['description']}")
                st.markdown(f"**Languages:** {', '.join(project['language'])}")
                st.markdown(
                    f"**Lead Developer:** {project['lead_developer']['name']} "
                    f"({project['lead_developer']['experience']} years experience)"
                )
                st.markdown("---")
        else:
            st.warning("No projects found.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching projects: {e}")

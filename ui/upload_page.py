# Upload page placeholder
import streamlit as st

def upload_files():

    st.title("Smart Resume Screening System")

    resumes = st.file_uploader(
        "Upload Resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    job_file = st.file_uploader(
        "Upload Job Description",
        type=["txt"]
    )

    return resumes, job_file
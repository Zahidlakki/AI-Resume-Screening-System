import streamlit as st
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Background & Global */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
    color: #f8fafc;
}

/* Main container */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(16px);
    border-right: 1px solid rgba(255, 255, 255, 0.05);
}
section[data-testid="stSidebar"] * {
    color: #e2e8f0;
}

/* Metric cards (Like Buttons) */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%) !important;
    border: 2px solid #8b5cf6 !important;
    padding: 20px !important;
    border-radius: 16px !important;
    box-shadow: 0 8px 25px rgba(139, 92, 246, 0.4) !important;
    transition: all 0.3s ease-in-out !important;
    text-align: center !important;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-5px) scale(1.02) !important;
    box-shadow: 0 12px 35px rgba(139, 92, 246, 0.6) !important;
}
[data-testid="stMetric"] * {
    color: #ffffff !important;
}
[data-testid="stMetricValue"] {
    font-size: 2.8rem !important;
    font-weight: 900 !important;
    background: none !important;
    -webkit-text-fill-color: #ffffff !important;
}
[data-testid="stMetricLabel"] {
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}

/* Buttons */
.stButton button {
    width: 100%;
    border-radius: 12px;
    height: 3.5em;
    font-weight: 600;
    font-size: 1rem;
    background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%);
    color: white !important;
    border: none;
    box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4);
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.stButton button:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 25px rgba(139, 92, 246, 0.6);
}
.stButton button:active {
    transform: scale(0.98);
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background: rgba(255, 255, 255, 0.02);
    border-radius: 16px;
    padding: 10px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

/* File Uploader Container & Labels */
[data-testid="stFileUploader"] label {
    color: #f8fafc !important;
    font-weight: 600 !important;
    font-size: 1.1rem !important;
}

[data-testid="stFileUploader"] small {
    color: #cbd5e1 !important;
}

/* File Uploader Dropzone */
[data-testid="stFileUploadDropzone"] {
    background: rgba(15, 23, 42, 0.6) !important;
    border: 2px dashed #8b5cf6 !important;
    border-radius: 16px !important;
    padding: 2rem !important;
    transition: all 0.3s ease !important;
}

[data-testid="stFileUploadDropzone"]:hover {
    background: rgba(139, 92, 246, 0.1) !important;
    border-color: #3b82f6 !important;
}

[data-testid="stFileUploadDropzone"] div {
    color: #f8fafc !important;
}

/* The Browse Files Button and all Uploader text */
[data-testid="stFileUploader"] p,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] div {
    color: #f8fafc !important;
}

[data-testid="stFileUploader"] button,
button[kind="secondary"],
div[data-testid="stFileUploadDropzone"] button {
    background-color: #ec4899 !important;
    background-image: linear-gradient(90deg, #ec4899 0%, #8b5cf6 100%) !important;
    color: #ffffff !important;
    font-weight: 800 !important;
    border-radius: 10px !important;
    border: 2px solid #ec4899 !important;
    box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4) !important;
    padding: 0.5rem 1rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    opacity: 1 !important;
    visibility: visible !important;
}

[data-testid="stFileUploader"] button:hover,
button[kind="secondary"]:hover,
div[data-testid="stFileUploadDropzone"] button:hover {
    background-color: #8b5cf6 !important;
    background-image: none !important;
    border-color: #8b5cf6 !important;
    transform: scale(1.05) !important;
    box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6) !important;
}

/* Titles and Typography */
h1 {
    font-size: 3.5rem !important;
    font-weight: 800 !important;
    background: -webkit-linear-gradient(45deg, #60a5fa, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem !important;
    text-align: center;
}
h2, h3 {
    font-weight: 600 !important;
    color: #f1f5f9 !important;
}

/* Dividers */
hr {
    border-color: rgba(255, 255, 255, 0.1) !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------------
# Imports
# ----------------------------------

from ui.upload_page import upload_files

from src.resume_parser.pdf_parser import extract_pdf_text
from src.resume_parser.docx_parser import extract_docx_text

from src.matching_engine.matcher import calculate_match
from src.matching_engine.skill_matcher import match_skills

from src.information_extractor.candidate_details import (
    extract_candidate_details
)

from src.skill_extractor.skill_extractor import (
    extract_skills
)

from src.ai_analyzer.gemini_analyzer import (
    analyze_candidate
)

# ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    st.title("🤖 ATS Dashboard")

    st.success(
        "AI Recruitment Assistant"
    )

    st.markdown("---")
    st.markdown("### 📊 System Architecture")
    st.markdown(
        """
        - **Data Ingestion**: Parses unstructured resumes (PDF/DOCX).
        - **NLP Engine**: Computes TF-IDF similarity and extracts key entities.
        - **AI Analysis**: Generates automated, unbiased candidate insights.
        """
    )
    st.markdown("---")
    st.info("Ready for processing. Awaiting file upload.")

# ----------------------------------
# Main Header
# ----------------------------------

st.title(
    "🤖 AI Resume Screening System"
)

st.caption(
    "AI-Powered Recruitment & Candidate Ranking Platform"
)

# ----------------------------------
# Upload Files
# ----------------------------------

resumes, job_file = upload_files()

# ----------------------------------
# Process Files
# ----------------------------------

if resumes and job_file:

    job_text = job_file.read().decode("utf-8")

    job_skills = extract_skills(
        job_text
    )

    results = []

    candidate_profiles = []

    for resume in resumes:

        try:

            # --------------------------
            # Extract Resume Text
            # --------------------------

            if resume.name.endswith(".pdf"):

                resume_text = extract_pdf_text(
                    resume
                )

            elif resume.name.endswith(".docx"):

                resume_text = extract_docx_text(
                    resume
                )

            else:

                continue

            # --------------------------
            # Candidate Details
            # --------------------------

            details = extract_candidate_details(
                resume_text
            )

            # --------------------------
            # Skills
            # --------------------------

            resume_skills = extract_skills(
                resume_text
            )

            # --------------------------
            # Skill Matching
            # --------------------------

            skill_result = match_skills(
                job_skills,
                resume_skills
            )

            # --------------------------
            # TF-IDF Score
            # --------------------------

            tfidf_score = calculate_match(
                resume_text,
                job_text
            )

            # --------------------------
            # Save Candidate Profile
            # --------------------------

            candidate_profiles.append({

                "candidate":
                resume.name,

                "resume_text":
                resume_text,

                "email":
                details.get(
                    "email",
                    "Not Found"
                ),

                "phone":
                details.get(
                    "phone",
                    "Not Found"
                ),

                "experience":
                details.get(
                    "experience",
                    "Not Found"
                ),

                "skills":
                resume_skills,

                "matched_skills":
                skill_result[
                    "matched_skills"
                ],

                "missing_skills":
                skill_result[
                    "missing_skills"
                ],

                "projects":
                details.get(
                    "projects",
                    []
                ),

                "skill_score":
                skill_result[
                    "skill_score"
                ]

            })

            # --------------------------
            # Ranking Table
            # --------------------------

            results.append({

                "Candidate":
                resume.name,

                "Email":
                details.get(
                    "email",
                    "Not Found"
                ),

                "Experience":
                details.get(
                    "experience",
                    "Not Found"
                ),

                "Skill Match %":
                skill_result[
                    "skill_score"
                ],

                "TFIDF Score":
                round(
                    tfidf_score,
                    2
                )

            })

        except Exception as e:

            st.error(
                f"Error processing {resume.name}: {str(e)}"
            )

    # ----------------------------------
    # Sort Results
    # ----------------------------------

    results = sorted(
        results,
        key=lambda x:
        x["Skill Match %"],
        reverse=True
    )

    # ----------------------------------
    # Dashboard Cards
    # ----------------------------------

    st.subheader(
        "📊 Recruitment Dashboard"
    )

    col1, col2, col3, col4 = st.columns(4)

    total_candidates = len(results)

    top_score = max(
        r["Skill Match %"]
        for r in results
    )

    average_score = round(
        sum(
            r["Skill Match %"]
            for r in results
        ) / len(results),
        2
    )

    shortlisted = len([
        r
        for r in results
        if r["Skill Match %"] >= 60
    ])

    col1.metric(
        "Candidates",
        total_candidates
    )

    col2.metric(
        "Top Score",
        f"{top_score}%"
    )

    col3.metric(
        "Average Score",
        f"{average_score}%"
    )

    col4.metric(
        "Shortlisted",
        shortlisted
    )

    st.divider()

    # ----------------------------------
    # Ranking Table
    # ----------------------------------

    st.subheader(
        "🏆 Candidate Ranking"
    )

    st.dataframe(
        results,
        use_container_width=True
    )

    st.divider()

    # ----------------------------------
    # Candidate Profile
    # ----------------------------------

    st.subheader(
        "👤 Candidate Profile"
    )

    candidate_names = [

        p["candidate"]

        for p in candidate_profiles

    ]

    selected_candidate = st.selectbox(

        "Select Candidate",

        candidate_names

    )

    for profile in candidate_profiles:

        if profile["candidate"] == selected_candidate:

            st.write(
                f"### {profile['candidate']}"
            )

            st.write(
                f"📧 Email: {profile['email']}"
            )

            st.write(
                f"📱 Phone: {profile['phone']}"
            )

            st.write(
                f"💼 Experience: {profile['experience']}"
            )

            st.progress(
                profile["skill_score"] / 100
            )

            st.write(
                f"Skill Match: {profile['skill_score']}%"
            )

            st.subheader(
                "🛠 Skills"
            )

            st.write(
                profile["skills"]
            )

            st.subheader(
                "✅ Matched Skills"
            )

            st.write(
                profile["matched_skills"]
            )

            st.subheader(
                "❌ Missing Skills"
            )

            st.write(
                profile["missing_skills"]
            )

            st.subheader(
                "📂 Projects"
            )

            st.write(
                profile["projects"]
            )

            # ----------------------------------
            # AI Analysis
            # ----------------------------------

            if st.button(
                "🤖 Generate AI Analysis"
            ):

                with st.spinner(
                    "Analyzing Candidate..."
                ):

                    analysis = analyze_candidate(

                        profile[
                            "resume_text"
                        ],

                        job_text

                    )

                    st.subheader(
                        "🤖 AI Analysis"
                    )

                    st.markdown(
                        analysis
                    )

else:

    st.info(
        "Please upload resumes and a job description."
    )
# JD analyzer placeholder
from src.skill_extractor.skill_extractor import extract_skills


def analyze_job_description(job_text):

    skills = extract_skills(job_text)

    return skills
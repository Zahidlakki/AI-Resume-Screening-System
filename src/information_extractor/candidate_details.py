from src.information_extractor.email_extractor import extract_email
from src.information_extractor.phone_extractor import extract_phone
from src.information_extractor.experience_extractor import extract_experience
from src.information_extractor.project_extractor import extract_projects


def extract_candidate_details(text):

    details = {}

    details["email"] = extract_email(text)
    details["phone"] = extract_phone(text)
    details["experience"] = extract_experience(text)
    details["projects"] = extract_projects(text)

    return details
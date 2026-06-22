import re

def extract_experience(text):

    pattern = r'(\d+)\+?\s*(year|years)'

    matches = re.findall(pattern, text.lower())

    if matches:
        return matches[0][0] + " Years"

    return "Not Found"
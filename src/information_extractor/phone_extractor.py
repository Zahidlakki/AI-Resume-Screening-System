# Phone extractor placeholder
import re

def extract_phone(text):

    pattern = r'(\+92\d{10}|03\d{9})'

    phones = re.findall(pattern, text)

    return phones[0] if phones else "Not Found"
SKILLS = [
    "python",
    "java",
    "c++",
    "javascript",
    "html",
    "css",
    "sql",
    "mysql",
    "mongodb",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "nlp",
    "fastapi",
    "flask",
    "django",
    "streamlit",
    "opencv",
    "git",
    "github",
    "docker",
    "aws",
    "linux"
]

def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return found_skills
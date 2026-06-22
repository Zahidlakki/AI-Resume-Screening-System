# Matching engine placeholder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match(resume_text, job_text):

    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )

    score = similarity[0][0] * 100

    return round(score, 2)
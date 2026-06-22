import google.generativeai as genai

API_KEY = "paste api key here"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def analyze_candidate(
    resume_text,
    job_description
):

    prompt = f"""
You are an HR recruitment expert.

Job Description:
{job_description}

Candidate Resume:
{resume_text}

Analyze the candidate.

Give:

1. Candidate Summary
2. Strengths
3. Weaknesses
4. Hiring Recommendation

Keep response professional.
"""

    response = model.generate_content(
        prompt
    )

    return response.text
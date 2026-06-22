def match_skills(
    job_skills,
    resume_skills
):

    job_set = set(job_skills)

    resume_set = set(
        resume_skills
    )

    matched_skills = list(

        job_set.intersection(
            resume_set
        )

    )

    missing_skills = list(

        job_set.difference(
            resume_set
        )

    )

    if len(job_set) > 0:

        skill_score = (

            len(
                matched_skills
            )

            /

            len(job_set)

        ) * 100

    else:

        skill_score = 0

    return {

        "matched_skills":
        matched_skills,

        "missing_skills":
        missing_skills,

        "skill_score":
        round(
            skill_score,
            2
        )

    }
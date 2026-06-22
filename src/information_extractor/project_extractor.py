def extract_projects(text):

    keywords = [
        "project",
        "projects",
        "developed",
        "built",
        "created"
    ]

    projects = []

    lines = text.split("\n")

    for line in lines:

        for keyword in keywords:

            if keyword in line.lower():

                projects.append(line.strip())

    return projects[:5]
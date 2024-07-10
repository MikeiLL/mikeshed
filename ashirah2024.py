import math

workbooks = [
    {
        "title": "Word Study Phonix",
        "workpages": 151,
        "completed": 26
    },
    {
        "title": "Language Arts",
        "workpages": 149,
        "completed": 12
    },
    {
        "title": "Spectrum 6th Grade",
        "workpages": 277,
        "completed": 0
    },
    {
        "title": "Word Problems",
        "workpages": 114,
        "completed": 7
    },
    {
        "title": "Reading",
        "workpages": 151,
        "completed": 19
    },
    {
        "title": "Spelling",
        "workpages": 131,
        "completed": 32
    },
    {
        "title": "Critical Thinking Math",
        "workpages": 102,
        "completed": 11
    },
    {
        "title": "World Geography",
        "workpages": 91,
        "completed": 16
    },
    {
        "title": "Writing",
        "workpages": 129,
        "completed": 23
    },
    {
        "title": "Math",
        "workpages": 148,
        "completed": 8
    },
    {
        "title": "Fractions",
        "workpages": 83,
        "completed": 22
    },
    {
        "title": "Vocabulary",
        "workpages": 148,
        "completed": 25
    },
    {
        "title": "Science",
        "workpages": 151,
        "completed": 15
    },
    {
        "title": "Ultimate Math",
        "workpages": 207,
        "completed": 26
    },
    {
        "title": "Test Practice",
        "workpages": 154,
        "completed": 61
    },
    {
        "title": "Algebra 6 - 8",
        "workpages": 106,
        "completed": 9
    },
]

print("\n\nAshirah's Workbook Progress:\n")
for workbook in workbooks:
    workbook["remaining"] = workbook["workpages"] - workbook["completed"]
    workbook["completion"] = str(math.floor(workbook["completed"] / workbook["workpages"] * 100)) + "%"
    print(f"{workbook['title']}:")
    print(f"\tWork Pages: {workbook['workpages']}")
    print(f"\tDone: {workbook['completed']}")
    print(f"\tRemaining: {workbook['remaining']}")
    print(f"\tCompletion: {workbook['completion']}\n")

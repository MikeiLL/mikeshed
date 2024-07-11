import math
from datetime import datetime
from pathlib import Path
import sys
import random


# Good source for emojis: https://emojicombos.com/ https://emojipedia.org/man-fairy-medium-skin-tone
# A source with some color codes https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal#287944

fun_unicode_characters = [ "🩷", "🧚🏻‍♀️", "✨",  "🏳️‍🌈", "🍭", "🌈", "⭐" ]
no_problem_phrases = [ "No worries!", "No problem!", "No sweat!", "No biggie", "No problemo!", "No problem at all", "Coolio"]
congratulatory_phrases = [ "Great job!", "Keep up the good work!", "You're doing great!", "You're it!", "You're doing fantastic!", "You're doing amazing!", "You're doing wonderful!", "You're doing superb!", "Excellent!", "You're doing outstanding!", "You're doing incredible!", "You're doing phenomenal!", "Marvelous!", "You're doing splendid!", "You're doing terrific!", "You're doing fabulous!", "You're doing grand!", "You're doing brilliant!", "You're doing exceptional!", "You're doing magnificent!", "You're doing glorious!", "You're doing sublime!", "You're doing majestic!", "The dutchess!"]

if len(sys.argv) > 1:
    print("\n\033[0;35mLooks like just want a review.\033[0;0m\n")
    overview = True
else:
    overview = False
    enterpages = input("\n\n\033[1;35mHi, Ashirah. Would you like to enter some workbook pages? (y/n) \033[0;0m")
    if not enterpages.lower().startswith("y"):
        print("\n\n\033[1;32mOkay, maybe next time. \n\n\033[1mHere's a summary of your work so far\033[0m:\n\n")
        overview = True
    else:
      print("\n\033[1;31mOkay!\033[0m \033[1;33mLet's get started on tracking today's work.\033[0m\n\n\033[1;36mEnter number of pages for each book you worked on today.\033[0m\n\n")


# Seed the first file with the workbook data
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
        "completed": 8
    },
]

today = datetime.today().date()

todays_work = []

files = Path("ashirah").glob("*.csv")
filelist = list(files)
if len(filelist) == 0:
    print("No files found")
    with open(f"ashirah/{today}.csv", "w") as file:
        file.write("Title\tWork Pages\tCompleted\tRemaining\tCompletion\n")
        for workbook in workbooks:
            workbook["remaining"] = workbook["workpages"] - workbook["completed"]
            workbook["completion"] = str(math.floor(workbook["completed"] / workbook["workpages"] * 100)) + "%"
            file.write(f"{workbook['title']}\t{workbook['workpages']}\t{workbook['completed']}\t{workbook['remaining']}\t{workbook['completion']}\n")
else:
    latest_file = sorted(filelist)[-1]
    with open(latest_file, "r") as file:
      workbooks = file.readlines()
      if not overview:
          with open(f"ashirah/{today}.csv", "w") as file:
            file.write("Title\tWork Pages\tCompleted\tRemaining\tCompletion\n")
            for i in range(1, len(workbooks)):
              workbook = workbooks[i].strip().split("\t")
              if len(workbook) < 5:
                  continue
              completed = int(input(f"Pages in {workbook[0]} today? "))
              workbook = {
                  "title": workbook[0],
                  "workpages": int(workbook[1]),
                  "completed": int(workbook[2]),
                  "remaining": int(workbook[3]),
                  "completion": workbook[4]
              }
              workbook["completed"] += completed
              workbook["remaining"] -= completed
              workbook["completion"] = str(math.floor(workbook["completed"] / workbook["workpages"] * 100)) + "%"
              print("Value of completed: ", completed)
              if completed > 0:
                  todays_work.append({
                      "title": workbook["title"],
                      "completed": f"{completed} page" + ("s" if completed > 1 else ""),
                      "active": True,
                  })
                  print(f"\n{random.choice(fun_unicode_characters)} {random.choice(congratulatory_phrases)}\n")
              else:
                  todays_work.append({
                      "title": workbook["title"],
                      "completed": f"{completed} page" + ("s" if completed > 1 else ""),
                  })
                  print(f"\n{random.choice(fun_unicode_characters)} {random.choice(no_problem_phrases)}\n")
              file.write(f"{workbook['title']}\t{workbook['workpages']}\t{workbook['completed']}\t{workbook['remaining']}\t{workbook['completion']}\n")
          file.close()
          print("\nYour work has been saved!\n\n")
          print("\033[1mSummary of today's work:\033[0m\n")
          for work in todays_work:
              if "active" in work: print(f"\t{random.choice(fun_unicode_characters)} {random.choice(fun_unicode_characters)} {random.choice(fun_unicode_characters)} {work['title']}: {work['completed']}")
              else: print(f"\t{work['title']}: {work['completed']}")
          print("\n----------------\n\033[105mOverall progress:\033[0m\n")
          meal = input(f"{random.choice(fun_unicode_characters)} {random.choice(fun_unicode_characters)} What are you thinking about meal on Friday? ")
          if (meal != ""):
              print(f"\nSounds good! Moving toward {meal} on Friday! {random.choice(fun_unicode_characters)} {random.choice(fun_unicode_characters)} {random.choice(fun_unicode_characters)}\n\n")
      for book in workbooks[1:]:
          workbook = book.strip().split("\t")
          print(f"\t{random.choice(fun_unicode_characters)} {workbook[0]}: {workbook[4]} complete\n\t-----------------------------\n")
      print(f"\n\n{random.choice(fun_unicode_characters)} Getting there, homie!!! {random.choice(fun_unicode_characters)} Bye for now.  {random.choice(fun_unicode_characters)} {random.choice(fun_unicode_characters)}\n\n")

import requests
import json
from datetime import datetime
import os
from pathlib import Path

import get
import settings

current_dir = Path(__file__).parent

headers = {"x-api-key": settings.OTLPLUS_API_KEY}

os.makedirs("logs", exist_ok=True)

result = requests.get(
    f"{settings.OTLPLUS_BASE_URL}/defaultSemester", headers=headers
).json()
semesters = [(result["year"], result["semester"])]

def put_previous_semester(semesters, count):
    if count == 0:
        return
    year, semester = semesters[-1]
    if semester == 1:
        year -= 1
        semester = 3
    elif semester == 3:
        semester = 1
    else:
        raise ValueError("Invalid semester: " + semesters[0])
    semesters.append((year, semester))
    put_previous_semester(semesters, count - 1)


put_previous_semester(semesters, 1)


def save_log(filetype, data):
    date_str = datetime.now().strftime("%Y-%m-%d")

    num = 0
    while True:
        filename = f"{current_dir}/logs/{date_str}_{filetype}_{num}.log"
        if not os.path.exists(filename):
            break
        num += 1

    # Write data to file
    with open(filename, "w", encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


for year, semester in semesters:
    try:
        lectures = get.get_lecture_type(lecture_year=year, lecture_term=semester)
        charges = get.get_charge_type(lecture_year=year, lecture_term=semester)

        result = requests.post(
            f"{settings.OTLPLUS_BASE_URL}/scholarDB",
            json={
                "year": year,
                "semester": semester,
                "lectures": lectures,
                "charges": charges,
            },
            headers=headers,
        )

        save_log(f"{year}-{semester}_scholarDB", result.json())
    except Exception as e:
        print(e)
        print(result)
        print(result.text)

    try:
        classtimes = get.get_time_type(lecture_year=year, lecture_term=semester)
        for classtime in classtimes:
            teaching = classtime["room_k_name"]
            classtime["room_k_name"] = classtime["room_e_name"]
            classtime["room_e_name"] = classtime["teaching"]
            classtime["teaching"] = teaching

        result = requests.post(
            f"{settings.OTLPLUS_BASE_URL}/classtime",
            json={"year": year, "semester": semester, "classtimes": classtimes},
            headers=headers,
        )

        save_log(f"{year}-{semester}_classtime", result.json())
    except Exception as e:
        print(e)
        print(result)
        print(result.text)

    try:
        examtimes = get.get_exam_time_type(lecture_year=year, lecture_term=semester)

        result = requests.post(
            f"{settings.OTLPLUS_BASE_URL}/examtime",
            json={"year": year, "semester": semester, "examtimes": examtimes},
            headers=headers,
        )

        save_log(f"{year}-{semester}_examtime", result.json())
    except Exception as e:
        print(e)
        print(result)
        print(result.text)

for year, semester in semesters:
    try:
        attend = get.get_attend_type(lecture_year=year, lecture_term=semester)

        result = requests.post(
            f"{settings.OTLPLUS_BASE_URL}/takenLecture",
            json={"year": year, "semester": semester, "attend": attend},
            headers=headers,
        )

        save_log(f"{year}-{semester}_takenLecture", result.json())
    except Exception as e:
        print(e)
        print(result)
        print(result.text)

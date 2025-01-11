import requests
import settings

urls = [
    "charge_type2" "lecture_type2",
    "exam_time_type2",
    "time_type2",
    "attend_type2",
    "report_e_degree_k",
    "kds_students_other_major",
]

headers = {"AUTH_KEY": settings.SCHOLAR_AUTH_KEY, "Content-Type": "application/json"}


def _get(url: str):
    response = requests.get(
        f"{settings.SCHOLAR_BASE_URL}{url}",
        headers=headers,
        verify=False,
    )
    response.encoding = "utf-8"
    return response.json()


def get_charge_type(lecture_year: str = None, lecture_term: str = None):
    params = []
    if lecture_year:
        params.append(f"lecture_year={lecture_year}")
    if lecture_term:
        params.append(f"lecture_term={lecture_term}")

    return _get(f"/charge_type2?{'&'.join(params)}")["OutBlock_1"]


def get_lecture_type(lecture_year: str = None, lecture_term: str = None):
    params = []
    if lecture_year:
        params.append(f"lecture_year={lecture_year}")
    if lecture_term:
        params.append(f"lecture_term={lecture_term}")

    return _get(f"/lecture_type2?{'&'.join(params)}")["OutBlock_1"]


def get_exam_time_type(lecture_year: str = None, lecture_term: str = None):
    params = []
    if lecture_year:
        params.append(f"lecture_year={lecture_year}")
    if lecture_term:
        params.append(f"lecture_term={lecture_term}")

    return _get(f"/exam_time_type2?{'&'.join(params)}")["OutBlock_1"]


def get_time_type(lecture_year: str = None, lecture_term: str = None):
    params = []
    if lecture_year:
        params.append(f"lecture_year={lecture_year}")
    if lecture_term:
        params.append(f"lecture_term={lecture_term}")

    return _get(f"/time_type2?{'&'.join(params)}")["OutBlock_1"]


def get_attend_type(
    lecture_year: str = None, lecture_term: str = None, student_no: str = None
):
    params = []
    if lecture_year:
        params.append(f"lecture_year={lecture_year}")
    if lecture_term:
        params.append(f"lecture_term={lecture_term}")
    if student_no:
        params.append(f"student_no={student_no}")

    return _get(f"/attend_type2?{'&'.join(params)}")["OutBlock_1"]


def get_report_e_degree_k(student_no: str = None):
    params = []
    if student_no:
        params.append(f"student_no={student_no}")

    return _get(f"/report_e_degree_k?{'&'.join(params)}")


def get_kds_students_other_major():
    return _get("/kds_students_other_major")["OutBlock_1"]

def get_view_kds_students_other_major():
    return _get("/view_kds_students_other_major")["OutBlock_1"]
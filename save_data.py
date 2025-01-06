import get as get

NAME_IDENTIFIER = "250102_1"

print("2025_get_charge_type")
with open(f'./data/test_all_get_charge_type_{NAME_IDENTIFIER}.json', 'wt') as f:
    f.write(get.get_charge_type())

print("2025_get_lecture_type")
with open(f'./data/test_all_get_lecture_type_{NAME_IDENTIFIER}.json', 'wt') as f:
    f.write(get.get_lecture_type())

print("2025_get_exam_time_type")
with open(f'./data/est_all_get_exam_time_type_{NAME_IDENTIFIER}.json', 'wt') as f:
    f.write(get.get_exam_time_type())

print("2025_get_time_type")
with open(f'./data/test_all_get_time_type_{NAME_IDENTIFIER}.json', 'wt') as f:
    f.write(get.get_time_type())

print("2025_get_attend_type")
with open(f'./data/test_all_get_attend_type_{NAME_IDENTIFIER}.json', 'wt') as f:
    f.write(get.get_attend_type())

print("get_report_e_degree_k")
with open(f'./data/test_get_report_e_degree_k_{NAME_IDENTIFIER}.json', 'wt') as f:
    f.write(get.get_report_e_degree_k())
  
print("get_kds_students_other_major")
with open(f'./data/test_get_kds_students_other_major_{NAME_IDENTIFIER}.json', 'wt') as f:
    f.write(get.get_kds_students_other_major())

with open(f'./data/20190448_get_attend_type_{NAME_IDENTIFIER}.json', 'wt') as f:
    f.write(get.get_attend_type(student_no=20190448))

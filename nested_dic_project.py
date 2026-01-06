"""
Project: Deep Nested Dictionary Cleaning, Uncoupling, and Aggregation
Author: Udeme Ebere
Description:
    This script demonstrates how to:
    - Traverse deeply nested dictionaries
    - Clean invalid records safely
    - Remove empty structures
    - Uncouple nested data into flat rows
    - Perform aggregation and averages
"""

# -----------------------------
# DATASET
# -----------------------------
system = {
    "universities": {
        "UniA": {
            "faculties": {
                "Science": {
                    "departments": {
                        "Math": {
                            "students": {
                                1: {
                                    "name": "Ada",
                                    "scores": {"calc": 78, "algebra": 85},
                                    "fees_paid": True
                                },
                                2: {
                                    "name": "John",
                                    "scores": {"calc": None, "algebra": 65},
                                    "fees_paid": True
                                }
                            }
                        },
                        "Physics": {
                            "students": {
                                3: {
                                    "name": "Mary",
                                    "scores": {"calc": 45, "algebra": -10},
                                    "fees_paid": False
                                }
                            }
                        }
                    }
                },
                "Arts": {
                    "departments": {
                        "History": {
                            "students": {
                                4: {
                                    "name": None,
                                    "scores": {"calc": 88, "algebra": 90},
                                    "fees_paid": True
                                }
                            }
                        }
                    }
                }
            }
        },
        "UniB": {
            "faculties": {
                "Engineering": {
                    "departments": {
                        "Civil": {
                            "students": {
                                5: {
                                    "name": "Grace",
                                    "scores": {"calc": 92, "algebra": 89},
                                    "fees_paid": True
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

# -----------------------------
# TASK 1: CLEAN INVALID STUDENTS
# -----------------------------
universities = system["universities"]

for uni_data in universities.values():
    for fac_data in uni_data["faculties"].values():
        for dept_data in fac_data["departments"].values():

            to_delete = []

            for stu_id, info in dept_data["students"].items():
                name = info["name"]
                calc = info["scores"]["calc"]
                algebra = info["scores"]["algebra"]

                if name is None:
                    to_delete.append(stu_id)
                    continue

                if calc is None or calc < 0 or calc > 100:
                    to_delete.append(stu_id)
                    continue

                if algebra < 0 or algebra > 100:
                    to_delete.append(stu_id)

            for stu_id in to_delete:
                del dept_data["students"][stu_id]

# -----------------------------
# TASK 2: STRUCTURAL CLEANUP
# -----------------------------
# Remove empty departments
for uni_data in universities.values():
    for fac_data in uni_data["faculties"].values():
        dept_to_delete = []

        for dept_name, dept_data in fac_data["departments"].items():
            if not dept_data["students"]:
                dept_to_delete.append(dept_name)

        for dept_name in dept_to_delete:
            del fac_data["departments"][dept_name]

# Remove empty faculties
for uni_data in universities.values():
    fac_to_delete = []

    for fac_name, fac_data in uni_data["faculties"].items():
        if not fac_data["departments"]:
            fac_to_delete.append(fac_name)

    for fac_name in fac_to_delete:
        del uni_data["faculties"][fac_name]

# Remove empty universities
uni_to_delete = []

for uni_name, uni_data in universities.items():
    if not uni_data["faculties"]:
        uni_to_delete.append(uni_name)

for uni_name in uni_to_delete:
    del universities[uni_name]

# -----------------------------
# TASK 3: UNCOUPLING (FLATTEN)
# -----------------------------
rows = []

for uni_name, uni_data in universities.items():
    for fac_name, fac_data in uni_data["faculties"].items():
        for dept_name, dept_data in fac_data["departments"].items():
            for stu_id, info in dept_data["students"].items():

                row = (
                    uni_name,
                    fac_name,
                    dept_name,
                    stu_id,
                    info["name"],
                    info["scores"]["calc"],
                    info["scores"]["algebra"]
                )

                rows.append(row)

# -----------------------------
# TASK 4: AGGREGATION
# -----------------------------
# Average calc score per department
calc_by_dept = {}

for _, _, dept, _, _, calc, _ in rows:
    calc_by_dept.setdefault(dept, []).append(calc)

calc_avg_by_dept = {
    dept: sum(scores) / len(scores)
    for dept, scores in calc_by_dept.items()
}

# Average algebra score per faculty
algebra_by_faculty = {}

for _, faculty, _, _, _, _, algebra in rows:
    algebra_by_faculty.setdefault(faculty, []).append(algebra)

algebra_avg_by_faculty = {
    fac: sum(scores) / len(scores)
    for fac, scores in algebra_by_faculty.items()
}

# -----------------------------
# OUTPUT
# -----------------------------
print("FLATTENED ROWS:")
for row in rows:
    print(row)

print("\nAVERAGE CALC SCORE PER DEPARTMENT:")
print(calc_avg_by_dept)

print("\nAVERAGE ALGEBRA SCORE PER FACULTY:")
print(algebra_avg_by_faculty)

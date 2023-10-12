from models.laboratory_model import LaboratoryModel


laboratories = [
    "Acad 1 - 103",
    "Acad 1 - 104",
    "Room 1",
    "Room 2",
    "Room 3",
    "Room 4",
    "MAC Lab",
    "IT Lab 1",
    "IT Lab 2",
    "NAS Lab",
    "CS Lab",
    "RISE Lab",
    "ERP Lab",
    "LIS Lab",
    "Open Lab",
    "Field",
]


def seed():
    if len(LaboratoryModel().all()) == 0:
        for lab in laboratories:
            LaboratoryModel().insert_laboratory(lab)
        LaboratoryModel().commit_and_close()

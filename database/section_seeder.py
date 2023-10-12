from models.section_model import SectionModel


sections = [
    "BSCS 1A",
    "BSCS 1B",
    "BSCS 2A",
    "BSCS 2B",
    "BSCS 3A",
    "BSCS 3B",
    "BSCS 4A",
    "BSCS 4B",
    "BSIT 1A",
    "BSIT 1B",
    "BSIT 1C",
    "BSIT 1D",
    "BSIT 1E",
    "BSIT 1F",
    "BSIT 1G",
    "BSIT 1H",
    "BSIT 2A",
    "BSIT 2B",
    "BSIT 2C",
    "BSIT 2D",
    "BSIT 2E",
    "BSIT 2F",
    "BSIT 2G",
    "BSIT 2H",
    "BSIT 3A",
    "BSIT 3B",
    "BSIT 3C",
    "BSIT 3D",
    "BSIT 3E",
    "BSIT 3F",
    "BSIT 4A",
    "BSIT 4B",
    "BSIT 4C",
    "BSIT 4D",
    "BLIS 1A",
    "BLIS 2A",
    "BLIS 3A",
    "BLIS 4A",
    "BLIS 4B",
    "BSIS 1A",
    "BSIS 1B",
    "BSIS 1C",
    "BSIS 2A",
    "BSIS 2B",
    "BSIS 2C",
    "BSIS 3A",
    "BSIS 3B",
    "BSIS 3C",
    "BSIS 4A",
    "BSIS 4B",
]


def seed():
    if len(SectionModel().all()) == 0:
        for section in sections:
            sectionArr = section.split(" ")
            program = sectionArr[0]
            year = sectionArr[1][0]
            section = sectionArr[1][1]

            SectionModel().insert_section(program, year, section)

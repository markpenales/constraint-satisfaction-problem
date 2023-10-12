from models.instructor_model import InstructorModel


instructor_data = [
    ["Ms. ", "Ichelle F. Baluis", ["Capstone Project 2"]],
    ["Ms. ", "Brenda D. Benosa", ["Methods of Research in Computing"]],
    [
        "Ms. ",
        "Kay Angeline O. Broqueza",
        ["Information Literacy", "Management of Libraries and Information Centers I"],
    ],
    ["Ms. ", "Charmane Recah V. De lima-Millano", []],
    [
        "Ms. ",
        "Kaela Marie N. Fortuno",
        [
            "Data Structures and Algorithms",
            "Algorithms and Complexity",
            "Architecture and Organization",
        ],
    ],
    [
        "Ms. ",
        "Ayra A. Gonowon",
        ["Indexing and Abstracting", "Introduction to Records Management and Archives"],
    ],
    ["Ms. ", "Leni Girlie M. Idian", []],
    [
        "Ms. ",
        "Josefina H. LLagas",
        ["Introduction to Computing", "Systems Integration and Architecture 1"],
    ],
    ["Ms. ", "Shiela Dona S. Manlapaz", ["Information Assurance and Security 1"]],
    ["Ms. ", "Rosel O. Onesa", ["CS Thesis 2"]],
    [
        "Ms. ",
        "Maricris L. Ramizares",
        ["Capstone Project 2", "Systems Integration and Architecture 1"],
    ],
    [
        "Ms. ",
        "Tiffany Lyn O. Pandes",
        [
            "Software Engineering 1",
            "Fundamentals of Programming",
            "Automata Theory and Formal Languages",
        ],
    ],
    [
        "Ms. ",
        "Kezia Abegail T. Velasco",
        ["Networking 1", "Data Structures and Algorithms"],
    ],
    ["Ms. ", "Laiza Mae R. Agnote", []],
    ["Ms. ", "Ms. maria Rica B. Arce", []],
    ["Ms. ", "Suzanne S. Causapin", []],
    ["Ms. ", "Cathyrine D. Chua", []],
    ["Ms. ", "Karen E. Comprado", []],
    ["Ms. ", "Maria Theresa B. Goleta", []],
    ["Ms. ", "Mercy O. Gonowon", []],
    ["Ms. ", "Mary France D. Raluta", []],
    ["Ms. ", "Marivic L. Ramizares", []],
    ["Ms. ", "Mae Ann Ll. Tagum", []],
    ["Ms. ", "Rosemarie C. Vidal", []],
    ["Ms. ", "Mildred A. Volante", []],
    ["Ms. ", "Joyce Arbaja", []],
    ["Ms. ", "Mae. M. Bayobo", []],
    ["Ms. ", "Maria Daisy R. Belardo", []],
    ["Ms. ", "Kathleen May Corbito", []],
    ["Ms. ", "Mary Chie A. De La Cruz", []],
    ["Ms. ", "Mariane Christine C. Lico", []],
    ["Ms. ", "Jillian N. Orante", []],
    ["Ms. ", "Jeniffer R. Sevilla", []],
    ["Ms. ", "Elaine Mae G. Tormes", []],
    ["Dr. ", "Ian P. Benitez", ["Systems Administration and Maintenance"]],
    ["Dr. ", "Challiz D. Omorog", ["Methods of Research in Computing"]],
    [
        "Mr. ",
        "Jonuel Rey N. Colle",
        ["Advanced Database Systems", "Distributed Database Management"],
    ],
    ["Mr. ", "Rey T. Cortez", ["Networking 1"]],
    ["Mr. ", "Niño jeffrey L. Luzon", ["IS Project Management 1"]],
    ["Mr. ", "Jeremy Jireh S. Neo", ["Enterprice Architecture"]],
    ["Mr. ", "Joseph Jessie S. Oñate", ["Introduction to Artificial Intelligence"]],
    ["Mr. ", "Freddie B. Prianes", []],
    ["Mr. ", "Vencel Angelo R. Sanglay", ["Multimedia Systems"]],
    ["Mr. ", "Philip Alger M. Serrano", []],
    ["Mr. ", "James Nicolo S. Sias", []],
    [
        "Mr. ",
        "Jayvee Niel S. Sias",
        ["Mobile Technology 1", "Business Process Progeramming 1"],
    ],
    [
        "Mr. ",
        "Jethro Ralph N. Abonal",
        [
            "Introduction to Computing",
            "Digital Foensics 1",
        ],
    ],
    ["Mr. ", "Kevin Von Erick D. Albania", []],
    ["Mr. ", "Jonathan Balbuena", []],
    ["Mr. ", "Guilbert Corporal", []],
    ["Mr. ", "Mark Anthony S. Dancalan", []],
    ["Mr. ", "Eisen Rose D. Galvante ", []],
    ["Mr. ", "Allan O. Ibo Jr.", []],
    ["Mr. ", "Jay-R H. Leonidas", []],
    ["Mr. ", "Mark Kenneth R. Limjoco", []],
    ["Mr. ", "Mark Joseph B. Norvadez", []],
    ["Mr. ", "Richard F. Nonato", []],
    ["Mr. ", "Noel B. Paguio Jr.", []],
    ["Mr. ", "Leomir K. Paz", []],
    ["Mr. ", "Lawrence A. Rebulado", []],
    ["Mr. ", "Jp Remaro R. Serrano", []],
    ["Mr. ", "Mark Anthony Taduran", []],
    ["Mr. ", "Nelson P. Vargas", []],
    ["Mr. ", "Domingo J. Vinluan Jr.", []],
    ["Mr. ", "Jonie M. Beriña", []],
    ["Mr. ", "Mark Kevin P. Candelaria", []],
    ["Mr. ", "Vincent B. Cortez", []],
    ["Mr. ", "Yves Aristeo A. Febres", []],
    ["Mr. ", "Derick S. Parañal", []],
    ["Mr. ", "Leo Pol Ramos", []],
]


def seed():
    instructor_model = InstructorModel()

    if len(instructor_model.all()) == 0:
        for title, name, expertise in instructor_data:
            instructor_model.insert_instructor(title, name, expertise)

        instructor_model.commit_and_close()

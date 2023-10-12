from models.course_model import CourseModel


courses = {
    "bscs": {
        1: {
            "Introduction to Computing": 3,
            "Fundamentals of Programming": 3,
            "Linear Algebra": 3,
            "Understanding the Self": 3,
            "Reading in Philippine History": 3,
            "Gender and Society": 3,
            "Physical Activities Toward Health and Fitness 1": 2,
            "National Service Training Program 1": 3,
        },
        2: {
            "Data Structures and Algorithms": 3,
            "Algorithms and Complexity": 3,
            "Discrete Structures 2": 3,
            "Object Oriented Programming": 3,
            "Operating Systems": 3,
            "Introduction to Artificial Intelligence": 3,
            "Art Appreciation": 3,
            "Physical Education 3": 2,
            "Gender and Society": 3,
        },
        3: {
            "Application Development And Emerging Technologies": 3,
            "Automata Theory And Formal Languages": 3,
            "Architecture and Organization": 3,
            "Information Assurance and Security": 3,
            "Software Engineering 1": 3,
            "Defensive Programming": 3,
            "Network Security": 3,
            "Digital Forensics 1": 3,
            "Reading Visual Art": 3,
        },
        4: {
            "Social issues and Professional Practice 1": 3,
            "Computer Science Thesis 2": 3,
            "Modeling and Simulation": 3,
        },
    },
    "bsit": {
        1: {
            "Introduction to Computing": 3,
            "Computer Programming 1": 3,
            "Networking 1": 3,
            "Multimedia Systems": 3,
            "Purposive Communication": 3,
            "Understanding the Self": 3,
            "Ethics": 3,
            "Physical Activities Toward Health and Fitness 1": 2,
            "National Service Training Program 1": 3,
        },
        2: {
            "Data Structures and Algorithms": 3,
            "Information Management 1": 3,
            "Object Oriented Programming": 3,
            "Web Systems and Technologies 2": 3,
            "Mobile Technology 1": 3,
            "Multimedia Systems": 3,
            "Art Appreciation": 3,
            "Science, Technology and Society": 3,
            "Physical Education 3": 3,
        },
        3: {
            "Advanced Database Systems": 3,
            "Networking 2": 3,
            "Systems Integration and Architecture 1": 3,
            "Quantitative Methods": 3,
            "Information Assurance and Security 1": 3,
            "Integrative Programming and Technologies 2": 3,
            "Event Driven Programming": 3,
            "Reading Visual Art": 3,
        },
        4: {
            "Systems Administration and Maintenance": 3,
            "Capstone Project 2": 3,
        },
    },
    "blis": {
        1: {
            "Introduction to Library and Information Science": 3,
            "School/Academic Librarianship": 3,
            "Operating System": 3,
            "Understanding the Self": 3,
            "Reading in the Philippine History": 3,
            "Purposive Communication": 3,
            "Physical Activities Toward Health and Fitness 1": 2,
            "National Service Training Program 1": 3,
        },
        2: {
            "Information Resources and Services 1": 3,
            "Organization Of Information Resources 1": 3,
            "Information Processing and Handling in Libraries and Information Centers": 3,
            "Database Design for Libraries": 3,
            "Preservation of Information Resources": 3,
            "Art Appreciation": 3,
            "Science, Technology And Society": 3,
            "Gender and Society": 3,
            "Physical Activities Toward Health and Fitness 1": 2,
        },
        3: {
            "Indexing and Abstracting": 3,
            "Management of Libraries and Information Centers I": 3,
            "Introduction to Records Management and Archives": 3,
            "Research Methods in Library and Information Science": 3,
            "Systems Analysis and Design in Libraries and Information Centers": 3,
            "Platform Security": 3,
            "Quantitative Methods": 3,
            "Educational Technology": 3,
        },
        4: {
            "Multimedia Systems": 3,
            "Philosophies and Principles of Teaching": 3,
            "Library Practice 1": 4,
            "Reading Visual Art": 3,
        },
    },
    "bsis": {
        1: {
            "Introduction to Computing": 3,
            "Computer Programming 1": 3,
            "Organization and Management Concepts": 3,
            "Mathematics in the Modern World": 3,
            "Understanding the Self": 3,
            "Readings in Philippine History": 3,
            "Physical Activities Toward Health and Fitness 1": 2,
            "National Service Training Program 1": 3,
        },
        2: {
            "Data Structures and Algorithm": 3,
            "Information Management 1": 3,
            "Professional Issues in IS": 3,
            "IT Infrastructure and Network Technologies": 3,
            "Accounting for ITE": 3,
            "Art Appreciation": 3,
            "Science, Technology and Society": 3,
            "Physical Education 3": 2,
            "Gender and Society": 3,
        },
        3: {
            "Enterprise Architecture": 3,
            "Business Process Management": 3,
            "Quantitative methods": 3,
            "IS Project Management 1": 3,
            "Distributed Database Management": 3,
            "Multimedia Systems": 3,
            "Business Process Programming 1": 3,
            "Methods of Research in Computing": 3,
        },
        4: {
            "IS Strategy, Management And Acquisition": 3,
            "Capstone Project 2": 3,
            "Foreign Language": 3,
            "Reading Visual Art": 3,
        },
    },
}


def seed():
    course_model = CourseModel()
    if len(course_model.all()) < 1:
        course_model.seed_courses(courses)

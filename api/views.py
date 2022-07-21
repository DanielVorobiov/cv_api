from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class CurriculumVitaeViewSet(ViewSet):

    @action(detail=False, methods=['GET'], url_path='about')
    def about(self, request, *args, **kwargs):
        return Response(
            "Personal profile: A software developer, eager to expand the current knowledge base and learn modern "
            "and useful technologies to make the world a better place. An open-minded team player with strong "
            "soft skills that can quickly adapt to a new environment.",
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='experience')
    def experience(self, request, *args, **kwargs):
        return Response(
            "Work experience: \n"
            "Feb 2022 - July 2022: Python Developer at EBS Integrator \n"
            "Developed RESTful APIs for projects like online shops, online education, HRM, and CRM \n"
            "Worked on: Implementation of new models and business logic, integration with other services "
            "automatic periodic tasks, CI/CD pipelines, unit testing \n"
            "Used technologies: Python, Django Rest Framework, Git, PostgreSQL, Swagger, Docker, Celery \n"
            "\n"
            "Sep 2021 - Feb 2022: SCRUM Master at Mooving \n"
            "Implementing SCRUM principles \n"
            "Managing Jira issues and Backlog \n"
            "Running SCRUM meetings \n"
            "\n"
            "Jul 2021 - Feb 2022: Python Developer at Mooving \n"
            "Developed an API for a website \n"
            "Worked on: authentication, users, chat, calendar functionalities, unit testing \n"
            "Used technologies: Python, Django Rest Framework, Git, PostgreSQL, Redis, Docker, Postman \n"
            "\n"
            "Sep 2019 - Jul 2022: ICT Teacher at STEP IT Academy \n"
            " Taught 8-14 years old kids modern technology like 3D Printing, VR & AR, Video Games Development.",
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='education')
    def education(self, request, *args, **kwargs):
        return Response(
            "Educational history: \n"
            "Sep 2018 - Jul 2022, Technical University of Moldova \n"
            "BA in Computer Science \n"
            "\n"
            "Studied the main concepts of the IT industry: Algorithms & Data Structures, OOP, Design Patterns & "
            "SOLID Principles, Linux, Databases, Version Control, Mobile Development, Web Development, JIRA \n"
            "Learned programming languages: Python, C#, JS, TS \n"
            "Developed a Sudoku mobile game using Django and Flutter.",
            status=status.HTTP_200_OK
        )

    # Volunteering exp
    @action(detail=False, methods=['GET'], url_path='volunteering')
    def volunteering(self, request, *args, **kwargs):
        return Response(
            "Volunteering experience: \n"
            "Oct 2018 - Dec 2019: Active member at BEST Chisinau \n"
            "As a Team-Leader successfully completed the event Planning, Execution, Monitoring "
            "& Control and Closure phases of the project \n"
            "Directly responsible for creating Gantt Chart, Budget, Project Dairy, Risk Log, "
            "and Team Members Schedule & Tasks on several projects \n"
            "Created and delivered presentations about project updates and soft skills \n"
            "\n"
            "Sep 2016 - May 2018: Volunteer at American Resource Center in Chisinau \n"
            "Co-organizer and moderator of two Debate Club Contests \n"
            "Mentor of Photography Club and 3D Printing & Modelling program \n"
            "Weekly events moderator in english.",
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='contacts')
    def contacts(self, request, *args, **kwargs):
        return Response(
            "Phone number: +37360240103 \n"
            "Email: vorobiov.daniel@gmail.com \n"
            "Github: github.com/DanielVorobiov \n"
            "LinkedIn: @vorobiovdaniel",
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='soft-skills')
    def soft_skills(self, request, *args, **kwargs):
        return Response(
            "Adaptability 4/4 \n"
            "Communication & Public Speaking 4/4 \n"
            "Scrum & Agile Methodologies 3/4 \n"
            "Team Work 3/4 \n"
            "Teaching & Mentoring 3/4 \n"
            "Ability to Work Under Pressure: 3/4 \n"
            "Leadership & Team Building 3/4 \n"
            "Time Management 3/4 \n"
            "Tracking & Monitoring 3/4 \n"
            "Organization 3/4 \n",
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='technical-skills')
    def technical_skills(self, request, *args, **kwargs):
        return Response(
            "Microsoft Office & Google Suit 3/4 \n"
            "OOP, SOLID & Design Patterns 3/4 \n"
            "Git, GitLab & GitHub 3/4 \n"
            "JavaScript / TypeScript 3/4 \n"
            "Python Development - DRF 3/4 \n"
            "Databases(SQL) 2/4 \n"
            "Flutter Development 2/4",
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='languages')
    def languages(self, request, *args, **kwargs):
        return Response(
            "Romanian 4/4 \n"
            "English 3/4 \n"
            "Russian 2/4",
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='awards')
    def awards(self, request, *args, **kwargs):
        return Response(
            "The Project Management Course: Beginner to PROject Manager, Udemy, 2021 \n"
            "3rd Place Winner, IoT Bootcamp, MicroLab, 2020 \n"
            "First place Winner at National Public Speaking Contest in English, 2018 \n"
            "First Place Winner at the Public Speaking Competition at Gaudeamus Lyceum, 2017",
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='hobbies')
    def hobbies(self, request, *args, **kwargs):
        return Response(
            "Photography & Videography \n"
            "Board Games \n"
            "Playing piano \n"
            "Travelling \n"
            "Sudoku",
            status=status.HTTP_200_OK
        )
# Set Up
A virtual environment  is necessary in order to start the project. Create one in the same folder as the source code of the project using the following command:
```sh
python -m venv venv
```
Afterwards make sure to install the required libraries for the project using the following command from the source folder of the project:

```sh
pip install -r requirements.txt
```

To launch the project use the following command:

```sh
python manage.py runserver
```
This command will start the local server on http://127.0.0.1:8000/

# Using the API

The purpose of this API is to show information about the candidate from his Curriculum Vitae. As a CV, the API separates the info based on different categories. Since the API is used only to read data, GET is the only acceptable type of request. All available categories and their endpoints are specified below.

- To get a short description of the candidate use http://127.0.0.1:8000/api/about/
- To get information about the working experience of the candidate use http://127.0.0.1:8000/api/experience/
- To get data about the educational background of the candidate use  http://127.0.0.1:8000/api/education/
- To get information about the candidate's volunteering activities use http://127.0.0.1:8000/api/volunteering/
- To get data about the soft skills that the candidate posses use: http://127.0.0.1:8000/api/soft-skills/
- To get data about the technical skills that the candidate posses use: http://127.0.0.1:8000/api/technical-skills/
- To get information about the languages the candidate can speak use: http://127.0.0.1:8000/api/languages/
- To get data about the awards and certifications the candidate has recieved, use: http://127.0.0.1:8000/api/awards/
- To get data about the candidate's hobbies use: http://127.0.0.1:8000/api/hobbies/
- To get the contact information of the candidate use: http://127.0.0.1:8000/api/contacts/


# Testing the API
The API can be tested automatically using the following command:
```sh
python manage.py test 
```

# CLI Commands
To print the information from a specific category use this command:
```sh
python manage.py show_data 'category name'
```
Here is the list of all available categories:
- about
- experience
- education
- volunteering
- soft-skills
- technical-skills
- languages
- awards
- hobbies
- contacts
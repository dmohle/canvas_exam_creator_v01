import requests

# Constants
API_KEY = '5496~G6V6mJPNgI3XPfiC92BvJX1GyRGDcTSvTLAz3o0a5WMunIjcflAZI4vJT3m83KWE'
BASE_URL = 'https://scccd.instructure.com/api/v1/'
course_id = '107524'  # Make sure this course ID exists in your Canvas instance


def create_exam(course_id):
    url = f'{BASE_URL}courses/{course_id}/quizzes'  # Construct URL
    headers = {'Authorization': f'Bearer {API_KEY}'}
    exam_data = {
        'quiz': {
            'title': 'Test Quiz - Delete TEST!, Spr \'24',
            'description': 'Final Exam for the Course',
            'quiz_type': 'assignment',
            'published': True
        }
    }

    # Debug: Print the URL to check it's correct
    print("Request URL:", url)

    response = requests.post(url, headers=headers, json=exam_data)

    if response.status_code == 201:
        print("Exam created successfully!")
    else:
        print(f"Failed to create exam: Status Code {response.status_code}, Response: {response.text}")


create_exam(course_id)

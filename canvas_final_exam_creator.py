import requests

# Replace 'YOUR_API_KEY' with your actual Canvas API key
API_KEY = '5496~7LiRhR2VQBoeh4w8UViHXDwcwbgK6dfNBIUodjXyBx4fQ0Y9aR1PvfShjvfn3QNj'

# Base URL for the Canvas API
BASE_URL = 'https://scccd.instructure.com/api/v1/'

# Headers containing authentication information
headers = {
    'Authorization': 'Bearer ' + API_KEY,
}

# Function to make a GET request to the Canvas API and handle pagination
def canvas_get(endpoint):
    results = []
    url = BASE_URL + endpoint
    while url:
        response = requests.get(url, headers=headers)
        data = response.json()
        results.extend(data)
        links = requests.utils.parse_header_links(response.headers.get('link', ''))
        url = None
        for link in links:
            if link['rel'] == 'next':
                url = link['url']
                break
    return results

# Function to make a POST request to the Canvas API
def canvas_post(endpoint, data):
    response = requests.post(BASE_URL + endpoint, headers=headers, json=data)
    return response.json()

# Function to fetch all quizzes for a course
def get_quizzes(course_id):
    endpoint = f'courses/{course_id}/quizzes'
    return canvas_get(endpoint)

# Function to check if a quiz with a specific title already exists
def quiz_exists(course_id, title):
    quizzes = get_quizzes(course_id)
    for quiz in quizzes:
        if quiz['title'].lower() == title.lower():
            return True
    return False

# Function to create a quiz in a course
def create_quiz(course_id, quiz_data):
    endpoint = f'courses/{course_id}/quizzes'
    return canvas_post(endpoint, quiz_data)

# Main function to set up and create the quiz if it does not exist
def main():
    course_id = 107524  # Course ID for CIT-95
    quiz_title = "CIT-95 Final Exam_v02, Spr '24"

    if not quiz_exists(course_id, quiz_title):
        quiz_data = {
            "quiz": {
                "title": quiz_title,
                "description": "Final Exam: CIT-95, Spring 2024 \n\n25 multiple choice questions.\n\nOpen book/note.",
                "quiz_type": "assignment",
                "time_limit": 120,
                "shuffle_answers": True,
                "hide_results": "always",
                "points_possible": 100,
                "due_at": "2024-05-16T23:59:00Z",
                "published": True
            }
        }
        created_quiz = create_quiz(course_id, quiz_data)
        print("Created Quiz:")
        for key, value in created_quiz.items():
            print(f"{key}: {value}")
    else:
        print(f"A quiz titled '{quiz_title}' already exists in this course.")

if __name__ == "__main__":
    main()

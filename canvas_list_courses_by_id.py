import requests

API_KEY = '5496~Er0lmRlRRRh3mjYJqOLVpAk63pNBwrMcWtYgEiXwKvL79j8GgTMXOh4GjB8Y0Kth'
BASE_URL = 'https://scccd.instructure.com/api/v1/'


def list_courses():
    headers = {'Authorization': f'Bearer {API_KEY}'}
    url = f'{BASE_URL}courses'

    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            courses = response.json()
            for course in courses:
                # Debugging line to inspect the structure of each course object
                print(course)  # This will show the structure of the course dictionary

                # Check if 'name' and 'id' keys exist in the course dictionary before accessing them
                if 'name' in course and 'id' in course:
                    print(f"Course Name: {course['name']}, Course ID: {course['id']}")
                else:
                    print("Name or ID not found in course:", course)

            # Handle pagination
            url = response.links.get('next', {}).get('url')
        else:
            print(f"Failed to retrieve courses: Status Code {response.status_code}, Response: {response.text}")
            break


def main():
    """
    Main function to initiate course listing.
    This allows the script to be imported and the function
    'list_courses' to be used in other contexts without
    automatically running it.
    """
    list_courses()


if __name__ == "__main__":
    main()
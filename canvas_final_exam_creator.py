# canvas_final_exam_creator.py
# dH, 5/7/24

import requests

# Constants
API_KEY = '5496~G6V6mJPNgI3XPfiC92BvJX1GyRGDcTSvTLAz3o0a5WMunIjcflAZI4vJT3m83KWE'
BASE_URL = 'https://scccd.instructure.com/api/v1/'

def update_quiz_points(course_id, quiz_id, total_points):
    url = BASE_URL + f"courses/{course_id}/quizzes/{quiz_id}"
    headers = {'Authorization': 'Bearer ' + API_KEY}
    quiz_data = {
        'quiz': {
            'points_possible': total_points
        }
    }
    response = requests.put(url, headers=headers, json=quiz_data)
    if response.status_code == 200:
        print("Quiz points updated successfully!")
    else:
        print(f"Failed to update quiz points: Status Code {response.status_code}, Response: {response.text}")

def create_canvas_exam(course_id, exam_title, questions):
    url = BASE_URL + f"courses/{course_id}/quizzes"
    headers = {'Authorization': 'Bearer ' + API_KEY}
    exam_data = {
        'quiz': {
            'title': exam_title,
            'description': 'Final Exam for C++ Programming',
            'quiz_type': 'assignment',
            'due_at': '2024-05-17T23:59:00Z',
            'unlock_at': '2024-05-07T00:00:00Z',
            'lock_at': '2024-05-18T00:00:00Z',
            'published': True
        }
    }
    exam_response = requests.post(url, headers=headers, json=exam_data)
    exam = exam_response.json()
    total_points = 0

    if exam_response.status_code in [200, 201]:
        print("Exam created successfully! Exam ID:", exam['id'])
        for question in questions:
            question_url = BASE_URL + f"courses/{course_id}/quizzes/{exam['id']}/questions"
            question_data = {
                'question': {
                    'question_text': question['prompt'],
                    'question_type': 'multiple_choice_question',
                    'points_possible': 4,
                    'answers': [{'text': option, 'weight': 100 if option == question['correct_answer'] else 0} for option in question['options']]
                }
            }
            question_response = requests.post(question_url, headers=headers, json=question_data)
            if question_response.status_code == 200:
                print("Question added successfully:", question['prompt'])
                total_points += 4  # Add points for each question
            else:
                print(f"Failed to post question: Status Code {question_response.status_code}, Response: {question_response.text}")

        # Update total points for the quiz
        update_quiz_points(course_id, exam['id'], total_points)

    else:
        print(f"Failed to create exam: Status Code {exam_response.status_code}, Response: {exam_response.text}")

def main():
    course_id = 105015
    exam_title = "CIT-63 Final Exam, Spr '24"
    exam_questions = [
        {"prompt": "What does the '++' operator do in Java?",
         "options": ["Increment a value by one", "Decrement a value by one", "Multiply a value by two",
                     "None of the above"], "correct_answer": "Increment a value by one"},
        {"prompt": "What is the output of the following Java code snippet?<br><code>System.out.println(1 + 5);</code>",
         "options": ["6", "15", "1", "5"], "correct_answer": "6"},
        {"prompt": "How do you read a line of text from a file in Java using 'BufferedReader'?",
         "options": ["bufferedReader.read( )", "bufferedReader.readLine( )", "bufferedReader.readFile( )",
                     "bufferedReader.readLines( )"], "correct_answer": "bufferedReader.readLine( )"},
        {"prompt": "What does the 'static' keyword do when applied to a variable within a class in Java?",
         "options": ["Makes the variable belong to instances of the class",
                     "Makes the variable belong to the class, rather than any instance",
                     "Makes the variable change every time it is accessed",
                     "Deletes the variable after the program executes"],
         "correct_answer": "Makes the variable belong to the class, rather than any instance"},
        {"prompt": "In Java, what does the 'new' keyword do?",
         "options": ["Deletes an existing object", "Creates a new object", "Declares a new variable",
                     "Initializes a static variable"], "correct_answer": "Creates a new object"},
        {"prompt": "Which method in Java is used to write a single character to a file?",
         "options": ["FileWriter.writeChar( )", "FileWriter.write( )", "FileWriter.saveChar( )", "FileWriter.save( )"],
         "correct_answer": "FileWriter.write( )"},
        {"prompt": "What is the purpose of 'finally' block in Java?",
         "options": ["To execute code after a 'try' block only if no exceptions were thrown",
                     "To execute code after a 'try' block regardless of whether an exception was thrown",
                     "To handle the exception thrown by 'try' block",
                     "To declare variables that are used in 'try' and 'catch' blocks"],
         "correct_answer": "To execute code after a 'try' block regardless of whether an exception was thrown"},
        {"prompt": "What is Big O Notation used for in computer science?",
         "options": ["To determine the running time of a program in the worst-case scenario",
                     "To calculate the exact running time of a program", "To measure the space used by a program",
                     "To determine the correctness of a program"],
         "correct_answer": "To determine the running time of a program in the worst-case scenario"},
        {"prompt": "What is the output of the following Java code snippet?<br><code>int a = 10; <br>int b = ++a; <br>System.out.println(b);</code>",
            "options": ["10", "11", "12", "13"], "correct_answer": "11"},
        {"prompt": "What is the correct way to declare an array in Java?",
         "options": ["int array[ ]", "int array = new int[ ]", "int[ ] array = new int[ ]", "array[ ] = new int"],
         "correct_answer": "int[ ] array = new int[ ]"},
        {"prompt": "What feature of Java allows objects to hide their internal state and expose behavior?",
         "options": ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"], "correct_answer": "Encapsulation"},
        {"prompt": "What does it mean to 'override' a method in Java?",
         "options": ["To change the method's return type", "To provide a new method with the same name in a subclass",
                     "To remove the method from a subclass", "To rename a method in the superclass"],
         "correct_answer": "To provide a new method with the same name in a subclass"},
        {"prompt": "Which Java keyword is used to inherit from a class?",
         "options": ["super", "this", "class", "extends"], "correct_answer": "extends"},
        {"prompt": "What does the expression <br><code>int[] arr = {1, 2, 3};<br>System.out.println(arr[2]);</code> output?",
            "options": ["1", "2", "3", "An error"], "correct_answer": "3"},
        {"prompt": "Which loop will continue to execute as long as its condition remains true?",
         "options": ["for loop", "do-while loop", "while loop", "switch statement"], "correct_answer": "while loop"},
        {"prompt": "What is an example of polymorphism in Java?",
         "options": ["A class has multiple methods with the same name but different parameters",
                     "A class has multiple methods with the same name",
                     "A class can implement multiple methods from multiple interfaces",
                     "A class can extend multiple classes"],
         "correct_answer": "A class has multiple methods with the same name but different parameters"},
        {"prompt": "What is the return type of a method that does not return a value?",
         "options": ["int", "void", "null", "double"], "correct_answer": "void"},
        {"prompt": "What is the base class of all classes in Java?", "options": ["Main", "Class", "Object", "Root"],
         "correct_answer": "Object"},
        {"prompt": "Which method can modify the value of a private variable of a class?",
         "options": ["A class method", "A getter method", "A setter method", "A final method"],
         "correct_answer": "A setter method"},
        {"prompt": "What is the correct syntax to create an object in Java?",
         "options": ["ClassName obj = new ClassName( )", "ClassName obj = ClassName( )", "obj = new ClassName( )",
                     "new obj = ClassName( )"], "correct_answer": "ClassName obj = new ClassName( )"},
        {"prompt": "How do you handle exceptions in Java?",
         "options": ["try-catch block", "throws statement", "try-throw block", "throw-catch statement"],
         "correct_answer": "try-catch block"},
        {"prompt": "What is the use of the `final` keyword in Java?",
         "options": ["To finalize the implementation of the class", "To declare constants", "To prevent inheritance",
                     "To indicate the last variable of a class"], "correct_answer": "To declare constants"},
        {"prompt": "Which component is not part of Java's Collection Framework?",
         "options": ["List", "Set", "Map", "Array"], "correct_answer": "Array"},
        {"prompt": "What is the default layout manager for a JPanel in Java?",
         "options": ["FlowLayout", "BorderLayout", "GridLayout", "CardLayout"], "correct_answer": "FlowLayout"},
        {"prompt": "Which of the following is a valid interface in Java?",
         "options": ["Runnable", "Run", "Executable", "Throw"], "correct_answer": "Runnable"}
    ]

    create_canvas_exam(course_id, exam_title, exam_questions)

if __name__ == "__main__":
    main()

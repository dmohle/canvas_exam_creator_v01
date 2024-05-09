# create a PDF with the final exam questions
# dH 5/7/24
from fpdf import FPDF

# Creating instance of FPDF class
pdf = FPDF()

# Adding a page
pdf.add_page()

# Setting font: Arial, bold, 12
pdf.set_font("Arial", 'B', 12)

# Full list of questions
questions = [
    {"prompt": "What does the '++' operator do in Java?", "options": ["Increment a value by one", "Decrement a value by one", "Multiply a value by two", "None of the above"], "correct_answer": "Increment a value by one"},
    {"prompt": "What is the output of the following Java code snippet?<br><code>System.out.println(1 + 5);</code>", "options": ["6", "15", "1", "5"], "correct_answer": "6"},
    {"prompt": "How do you read a line of text from a file in Java using 'BufferedReader'?", "options": ["bufferedReader.read( )", "bufferedReader.readLine( )", "bufferedReader.readFile( )", "bufferedReader.readLines( )"], "correct_answer": "bufferedReader.readLine( )"},
    {"prompt": "What does the 'static' keyword do when applied to a variable within a class in Java?", "options": ["Makes the variable belong to instances of the class", "Makes the variable belong to the class, rather than any instance", "Makes the variable change every time it is accessed", "Deletes the variable after the program executes"], "correct_answer": "Makes the variable belong to the class, rather than any instance"},
    {"prompt": "In Java, what does the 'new' keyword do?", "options": ["Deletes an existing object", "Creates a new object", "Declares a new variable", "Initializes a static variable"], "correct_answer": "Creates a new object"},
    {"prompt": "Which method in Java is used to write a single character to a file?", "options": ["FileWriter.writeChar( )", "FileWriter.write( )", "FileWriter.saveChar( )", "FileWriter.save( )"], "correct_answer": "FileWriter.write( )"},
    {"prompt": "What is the purpose of 'finally' block in Java?", "options": ["To execute code after a 'try' block only if no exceptions were thrown", "To execute code after a 'try' block regardless of whether an exception was thrown", "To handle the exception thrown by 'try' block", "To declare variables that are used in 'try' and 'catch' blocks"], "correct_answer": "To execute code after a 'try' block regardless of whether an exception was thrown"},
    {"prompt": "What is Big O Notation used for in computer science?", "options": ["To determine the running time of a program in the worst-case scenario", "To calculate the exact running time of a program", "To measure the space used by a program", "To determine the correctness of a program"], "correct_answer": "To determine the running time of a program in the worst-case scenario"},
    {"prompt": "What is the output of the following Java code snippet?<br><pre>int a = 10;<br>int b = ++a;<br>System.out.println(b);</pre>", "options": ["10", "11", "12", "13"], "correct_answer": "11"},
    {"prompt": "What is the correct way to declare an array in Java?", "options": ["int array[ ]", "int array = new int[ ]", "int[ ] array = new int[ ]", "array[ ] = new int"], "correct_answer": "int[ ] array = new int[ ]"},
    {"prompt": "What feature of Java allows objects to hide their internal state and expose behavior?",
     "options": ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"], "correct_answer": "Encapsulation"},
    {"prompt": "What does it mean to 'override' a method in Java?",
     "options": ["To change the method's return type", "To provide a new method with the same name in a subclass",
                 "To remove the method from a subclass", "To rename a method in the superclass"],
     "correct_answer": "To provide a new method with the same name in a subclass"},
    {"prompt": "Which Java keyword is used to inherit from a class?",
     "options": ["super", "this", "class", "extends"], "correct_answer": "extends"},
    {
        "prompt": "What does the expression <br><code>int[] arr = {1, 2, 3};<br>System.out.println(arr[2]);</code> output?",
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

# Adding questions and answers to the PDF
for question in questions:
    pdf.cell(200, 10, txt=question["prompt"], ln=True)
    for index, option in enumerate(question["options"], start=1):
        pdf.cell(200, 10, txt=f"{index}. {option}", ln=True)
    pdf.cell(200, 10, txt=f"Correct answer: {question['correct_answer']}", ln=True)
    pdf.cell(200, 10, txt="", ln=True)  # Add a blank line for spacing

# Save the PDF to a file
pdf_output = "C:/2024_Spring/canvasAPIstuff/pdfSources/javaFinalExamQuestions.pdf"
pdf.output(pdf_output)

pdf_output


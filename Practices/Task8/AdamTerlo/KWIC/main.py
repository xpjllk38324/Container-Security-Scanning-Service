import subprocess

def main():
    # Titles for the KWIC index as an example
    titles = [
        "Design Patterns and Software Architecture and some other words",
        "Introduction to Advanced Computing is nice and quite long and has a lot of words",
        "Principles of Software Engineering",
        "this one is shorter",
        "Software Design for Performance",
        "Hello World",
        "A Quick Guide to Python Programming",
        "Advanced Topics in Machine Learning",
        "Web Development with Flask and Django",
        "An Exploration of Data Structures",
        "Understanding Algorithms and Complexity",
        "Creating User Interfaces with React",
        "The Art of Software Testing",
        "Effective Communication in Software Teams",
        "Building Scalable Applications in the Cloud",
        "Introduction to Cybersecurity Best Practices",
        "Optimizing Database Performance for Large Systems"
    ]

    # Set up the pipeline of processes using subprocess
    p1 = subprocess.Popen(['python3', 'input_filter.py'] + titles, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['python3', 'shift_filter.py'], stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(['python3', 'alphabetize_filter.py'], stdin=p2.stdout, stdout=subprocess.PIPE)
    p4 = subprocess.Popen(['python3', 'output_filter.py', '--pretty'], stdin=p3.stdout, stdout=subprocess.PIPE)

    # Capture and print the final output
    output, _ = p4.communicate()
    print(output.decode('utf-8'))

if __name__ == "__main__":
    main()

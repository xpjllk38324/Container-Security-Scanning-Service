import queue
import threading
from input_filter import input_filter
from shift_filter import shift_filter
from alphabetize_filter import alphabetize_filter
from output_filter import output_filter


def main():
    # Define queues (pipes)
    input_pipe = queue.Queue()
    shift_pipe = queue.Queue()
    alphabetize_pipe = queue.Queue()
    output_pipe = queue.Queue()

    # Titles to index
    titles = [
        "Design Patterns and Software Architecture",
        "Introduction to Advanced Computing",
        "Principles of Software Engineering",
        "Software Design for Performance"
    ]

    # Create threads for each filter
    input_thread = threading.Thread(target=input_filter, args=(titles, input_pipe))
    shift_thread = threading.Thread(target=shift_filter, args=(input_pipe, shift_pipe))
    alphabetize_thread = threading.Thread(target=alphabetize_filter, args=(shift_pipe, alphabetize_pipe))
    output_thread = threading.Thread(target=output_filter, args=(alphabetize_pipe,))

    # Start all threads
    input_thread.start()
    shift_thread.start()
    alphabetize_thread.start()
    output_thread.start()

    # Join threads to wait for their completion
    input_thread.join()
    shift_thread.join()
    alphabetize_thread.join()
    output_thread.join()


if __name__ == "__main__":
    main()

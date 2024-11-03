import sys


def alphabetize_filter():
    shifted_titles = [line.strip() for line in sys.stdin]

    # Sort titles based on the keyword (the second part of each line)
    sorted_titles = sorted(shifted_titles, key=lambda title: title.split('|')[1].strip())

    for title in sorted_titles:
        print(title)  # Output each sorted title as a line


if __name__ == "__main__":
    alphabetize_filter()

import sys


def shift_filter():
    for line in sys.stdin:
        words = line.strip().split()
        for i in range(len(words)):
            # Generate a circular shift
            pre_words = words[:i]  # Words before the keyword
            keyword = words[i]  # Keyword
            post_words = words[i + 1:]  # Words after the keyword

            # Print in the format: pre words | keyword | post words
            print(f"{' '.join(pre_words):<30} | {keyword:<20} | {' '.join(post_words)}")


if __name__ == "__main__":
    shift_filter()

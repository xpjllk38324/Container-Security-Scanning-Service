import sys
import argparse


def output_filter(pretty):
    sorted_titles = [line.strip() for line in sys.stdin]

    # Prepare to capture pre-words, keywords, and post-words for formatting
    pre_words = []
    keywords = []
    post_words = []

    for title in sorted_titles:
        parts = title.split('|')
        pre_words.append(parts[0].strip())
        keywords.append(parts[1].strip())
        post_words.append(parts[2].strip())

    if pretty:
        # Determine the maximum length for alignment
        max_pre_length = max(len(word) for word in pre_words)
        max_keyword_length = max(len(keyword) for keyword in keywords)

        # Print header
        print(f"{'Pre Words':<{max_pre_length}} | {'Keyword':<{max_keyword_length}} | Post Words")
        print('-' * (max_pre_length + max_keyword_length + 15))  # Adjust for separators

        # Print the formatted output
        for pre, keyword, post in zip(pre_words, keywords, post_words):
            print(f"{pre:>{max_pre_length}} | {keyword:<{max_keyword_length}} | {post}")
    else:
        # Plain text output without vertical bars
        for pre, keyword, post in zip(pre_words, keywords, post_words):
            print(f"{pre} {keyword} {post}".strip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a KWIC index.")
    parser.add_argument('--pretty', action='store_true', help="Display output in a nice table format.")
    args = parser.parse_args()

    output_filter(args.pretty)

# borrowed from NLTK - https://www.nltk.org/search.html?q=stopwords
import queue
import sys

STOP_WORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours',
              'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself',
              'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself',
              'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
              'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are',
              'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing',
              'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for',
              'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below',
              'to',
              'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
              'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most',
              'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
              's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're',
              've', 'y',
              'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't",
              'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',
              "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't",
              'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def input_filter(titles):
    for title in titles:
        words = [word for word in title.split() if word.lower() not in STOP_WORDS]
        print(" ".join(words))  # Output each processed title as a line


if __name__ == "__main__":
    # If titles are provided as arguments, use them; otherwise, read from stdin
    if len(sys.argv) > 1:
        titles = sys.argv[1:]
    else:
        titles = [line.strip() for line in sys.stdin]

    # Run the input filter
    input_filter(titles)

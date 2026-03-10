import re
import argparse
from collections import Counter


def extract_words(text: str) -> list:
    """
    Extracts normalized words from text.

    - Converts all text to lowercase
    - Removes punctuation and special characters
    - Returns a list of words
    """
    text = text.lower()

    # Extract alphabetic words only
    words = re.findall(r"\b[a-z]+(?:'[a-z]+)?\b", text)

    return words


def count_word_frequencies(words: list) -> Counter:
    """
    Counts word occurrences using Python's Counter.
    """
    return Counter(words)


def print_top_words(counter: Counter, top_n: int):
    """
    Prints the N most frequent words.
    """
    print(f"\nTop {top_n} most frequent words:\n")

    for word, count in counter.most_common(top_n):
        print(f"{word:<15} {count}")


def print_all_words(counter: Counter):
    """
    Prints all words sorted by frequency.
    """
    print("\nAll words sorted by frequency:\n")

    for word, count in counter.most_common():
        print(f"{word:<15} {count}")


def main():

    parser = argparse.ArgumentParser(
        description="Word Frequency Analyzer - counts word occurrences in a text file"
    )

    parser.add_argument(
        "file",
        help="Path to the input text file"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="Number of most frequent words to display (default: 10)"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Display all words instead of only the top N"
    )

    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        return

    words = extract_words(text)

    frequencies = count_word_frequencies(words)

    if args.all:
        print_all_words(frequencies)
    else:
        print_top_words(frequencies, args.top)


if __name__ == "__main__":
    main()

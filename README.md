# Word Frequency Analyzer

This program performs a **word frequency analysis** on a text file.

It reads an input text file, normalizes its content, and counts how many times each word appears. The program ignores punctuation and special characters and performs case-insensitive comparisons.

Finally, it displays the **most frequent words** found in the text.

---

# Features

- Case-insensitive word comparison
- Ignores punctuation and special characters
- Displays the **top 10 most frequent words** (or top N if specified)
- Option to display **all word frequencies**
- Simple command-line interface

---

# How It Works

The program processes the text in three main steps.

---

## 1. Text Normalization

The input text is first normalized to ensure consistent comparison:

- All characters are converted to lowercase.
- Punctuation and special characters are removed.
- Only alphabetic words are extracted.

This is done using a **regular expression**:

```python
words = re.findall(r"\b[a-z]+\b", text.lower())
```

This expression extracts only alphabetic words, ensuring that punctuation such as commas, periods, or special symbols are ignored.

---

## 2. Word Frequency Counting

After extracting the words, the program counts how many times each word appears.

This is implemented using Python's `Counter` from the `collections` module:

```python
frequencies = Counter(words)
```

`Counter` efficiently builds a dictionary-like structure where:

```
word -> number of occurrences
```

Example:

```
{
  "the": 15,
  "fox": 3,
  "quick": 4
}
```

---

## 3. Displaying Results

The program then sorts the words by frequency and displays the most common ones using:

```python
counter.most_common(n)
```

This returns the `n` most frequent words in descending order.

---

# Usage

Run the script from the command line.

### Basic Usage

```
python word_frequency.py <text_file>
```

Example:

```
python word_frequency.py sample.txt
```

Output:

```
Top 10 most frequent words:

the             6
fox             3
quick           3
was             3
very            2
dog             2
lazy            2
brown           1
jumps           1
over            1
```

---

# Optional Arguments

### Display a custom number of top words

```
python word_frequency.py sample.txt --top 20
```

---

### Display all word frequencies

```
python word_frequency.py sample.txt --all
```

Example output:

```
All words sorted by frequency:

the             6
fox             3
quick           3
was             3
very            2
dog             2
lazy            2
brown           1
jumps           1
over            1
```

---

# Example Input

Example `sample.txt` file:

```
The quick brown fox jumps over the lazy dog.
The fox was very quick and very clever.
The dog was lazy but the fox was quick.
```

---

# Project Structure

```
word-frequency-analyzer
│
├── word_frequency.py
├── sample.txt
└── README.md
```

---

# Notes

- The program ignores punctuation and special characters.
- Word comparisons are case-insensitive.
- Only alphabetic words are considered in the analysis.
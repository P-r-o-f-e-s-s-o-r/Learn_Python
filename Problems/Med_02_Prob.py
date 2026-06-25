import numpy as np
import string

# ---------- STEP 1 : Clean the text ----------
# Remove punctuation and convert to lowercase
# so "Hello" and "hello" are treated as the same word

def clean_text(text):
    text = text.lower()                          # "Hello World" → "hello world"
    text = text.translate(                       # removes . , ! ? etc.
        str.maketrans("", "", string.punctuation)
    )
    return text

# ---------- STEP 2 : Tokenise ----------
# Split the cleaned sentence into a list of words

def tokenise(text):
    words = text.split()    # "hello world hello" → ["hello", "world", "hello"]
    return words

# ---------- STEP 3 : Build frequency dict ----------
# Loop through words, skip if already seen

def build_frequency(word_list):
    freq = {}
    for word in word_list:
        if word not in freq:            # only process new words               #NICE MOVE
            freq[word] = word_list.count(word)
    return freq

# ---------- STEP 4 : NumPy analysis ----------
# Convert frequencies to a NumPy array for powerful math operations

def numpy_analysis(freq_dict):
    words   = list(freq_dict.keys())          # ["hello", "world", "python"]
    counts  = np.array(list(freq_dict.values())) # np.array([3, 1, 2])

    # np.argsort → returns indices that would sort the array (ascending)
    # [::-1]     → reverses it to get descending (highest first)
    sorted_indices = np.argsort(counts)[::-1]

    sorted_words  = [words[i]  for i in sorted_indices]
    sorted_counts = counts[sorted_indices]

    # Unique values and how many times each appears
    unique_words, unique_counts = np.unique(words, return_counts=True)

    # Basic stats using NumPy
    total_words  = np.sum(counts)
    avg_freq     = np.mean(counts)
    max_freq     = np.max(counts)
    min_freq     = np.min(counts)

    # Most & least repeated — find index of max/min in counts array
    most_repeated  = words[np.argmax(counts)]
    least_repeated = words[np.argmin(counts)]

    return {
        "sorted_words"   : sorted_words,
        "sorted_counts"  : sorted_counts,
        "total_words"    : total_words,
        "avg_freq"       : avg_freq,
        "most_repeated"  : most_repeated,
        "least_repeated" : least_repeated,
        "unique_count"   : len(unique_words),
    }

# ---------- STEP 5 : Display bar chart (text-based) ----------
# Draws a simple bar using string multiplication — no library needed

def display_bar_chart(sorted_words, sorted_counts, top_n=10):
    print("\n" + "=" * 45)
    print(f"  Top {top_n} Words — Frequency Bar Chart")
    print("=" * 45)

    top_words  = sorted_words[:top_n]
    top_counts = sorted_counts[:top_n]

    for word, count in zip(top_words, top_counts):
        bar = "█" * int(count)              # each █ = 1 occurrence
        print(f"  {word:<15} | {bar} {count}")

# ---------- STEP 6 : Display full report ----------

def display_report(result):
    print("\n" + "=" * 45)
    print("  Text Analysis Report")
    print("=" * 45)
    print(f"  Total words       : {result['total_words']}")
    print(f"  Unique words      : {result['unique_count']}")
    print(f"  Average frequency : {result['avg_freq']:.2f}")
    print(f"  Most repeated     : '{result['most_repeated']}'")
    print(f"  Least repeated    : '{result['least_repeated']}'")
    print("=" * 45)

    display_bar_chart(result["sorted_words"], result["sorted_counts"])

# ---------- MAIN ----------

def main():
    print("*" * 5, "Word Frequency Counter & Text Analyser", "*" * 5)
    text = input("\nEnter your text : ")

    cleaned   = clean_text(text)         # step 1
    word_list = tokenise(cleaned)        # step 2

    if not word_list:
        print("No words found. Please try again.")
        return

    freq_dict = build_frequency(word_list)   # step 3
    result    = numpy_analysis(freq_dict)    # step 4
    display_report(result)                   # step 5 + 6

main()
import string

# Recursive function to process words
def process_words(words, freq):
    # Base case: no words left
    if not words:
        return freq

    # Take the first word
    word = words[0]

    # Update frequency dictionary
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

    # Recursive call for the rest of the list
    return process_words(words[1:], freq)


# Main function
def word_frequency_counter(text):
    # Handle empty input
    if not text.strip():
        print("No text provided.")
        return {}

    # Remove punctuation and convert to lowercase
    cleaned_text = text.lower().translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = cleaned_text.split()

    # Dictionary to store frequencies
    frequency = {}

    # Process words recursively
    frequency = process_words(words, frequency)

    # Print results
    print("=== WORD FREQUENCY ===")
    for word, count in frequency.items():
        print(f"{word}: {count}")

    return frequency


# Example usage
text_input = "Hello world! This is a test. Hello again, world."
word_frequency_counter(text_input)


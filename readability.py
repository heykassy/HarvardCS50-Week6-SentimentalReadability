# TODO
from cs50 import get_string


def main():
    # Prompt the user for text
    text = get_string("Text: ")

    # Calculate the amount of letters, words and sentences
    num_letters = count_letters(text)
    num_words = count_words(text)
    num_sentences = count_sentences(text)

    # Find the letter average and sentence average
    L = num_letters / num_words * 100
    S = num_sentences / num_words * 100

    # Calculate and print the grade
    index = round(0.0588 * L - 0.296 * S - 15.8)
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


# Function that counts the number os letters and returns the sum
def count_letters(text):
    sum = 0
    for i in range(len(text)):
        if str.isalpha(text[i]):
            sum += 1
    return sum

# Function that counts the number os words and returns the sum


def count_words(text):
    sum = 0
    for i in range(len(text)):
        if text[i] == ' ':
            sum += 1
    sum += 1
    return sum

# Function that counts the number os sentences and returns the sum


def count_sentences(text):
    sum = 0
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            sum += 1
    return sum


# Call main
if __name__ == "__main__":
    main()
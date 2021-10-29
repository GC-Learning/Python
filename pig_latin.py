"""Generates a pig latin word."""
VOWELS = "aeiou"

def main():
    """Asks for a word and convert it to pig latin."""
    while True:
        word = input("Type a word: ")
        starts_with_vowel = VOWELS.__contains__(word[:1])

        if starts_with_vowel:
            print(f"{word}way")
        else:
            print(f"{word[1:len(word) - 1]}{word[:1]}ay")

        try_again = input("\n\nTry again? (Press Enter to try again, else n to quit)\n")

        if try_again == 'n':
            break

    input("Press Enter to exit.")

if __name__ == "__main__":
    main()

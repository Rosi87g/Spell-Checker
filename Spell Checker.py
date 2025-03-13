import difflib
import re

class SpellChecker:
    def __init__(self, word_list):
        self.word_list = set(word_list)

    def clean_word(self, word):
        return re.sub(r'[^a-zA-Z]', '', word).lower()

    def check_word(self, word):
        word = self.clean_word(word)
        if word in self.word_list:
            return (word, True)
        else:
            suggestions = difflib.get_close_matches(word, self.word_list)
            return (word, False, suggestions)

    def check_text(self, text):
        words = text.split()
        results = []
        for word in words:
            result = self.check_word(word)
            results.append(result)
        return results

# Sample word list (you can expand this)
word_list = ["apple", "banana", "orange", "grape", "watermelon", "pineapple"]

spell_checker = SpellChecker(word_list)

# Example usage
text = input("Enter a sentence: ")
results = spell_checker.check_text(text)

for word, is_correct, *suggestions in results:
    if is_correct:
        print(f"{word} is spelled correctly.")
    else:
        print(f"{word} is misspelled.")
        if suggestions:
            print(f"Suggestions: {', '.join(suggestions[0])}")

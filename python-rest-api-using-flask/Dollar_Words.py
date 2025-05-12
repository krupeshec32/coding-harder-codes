'''

problem statement:
Given a list of all words, find the words where the sum
of alphabetical positions of their letters equals 100 and
print them in order from shortest to longer.

Example

stower
tsoris
'''


def calculate_word_value(word):
    sum = 0
    for char in word:
        if char.isalpha():
            sum = sum + ord(char.lower()) - 96
        return sum


def validation_parantheses(input):
    reference_dict = {')': '(', ']': '[', '}': '{'}
    holder = []
    if input[0] not in reference_dict.values():
        return False
    for ch in input:
        if not holder:
            holder.append(ch)
        else:
            get_ch = reference_dict[ch]
            if get_ch in holder:
                holder.pop()
            else:
                return False
    if not holder:
        return True
    else:
        return False


def solve_dollar_words(n, words):
    dollar_words = []
    for word in words:
        if calculate_word_value(word) == 100:
            dollar_words.append(word)
    return sorted(dollar_words)


def main():  # How to read HackerEarth input
    assert(validation_parantheses("()[]"))
    n = int(input())  # of input words
    words = [input().strip() for _ in range(n)]  # List of words
    dollar_words = solve_dollar_words(n, words)
    for word in dollar_words:
        print(word)


if __name__ == "__main__":
    main()

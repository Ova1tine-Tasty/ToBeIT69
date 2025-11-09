def find_longest_word(text):
    words = text.split()
    longest = max(words, key=len)
    return longest

user_input = input("")
if user_input.strip():
    result = find_longest_word(user_input)
    print(f"{result}")
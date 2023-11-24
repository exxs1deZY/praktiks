class StringUtils:
    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]

word = "радар"
print(f"Является ли '{word}' палиндромом? {StringUtils.is_palindrome(word)}")

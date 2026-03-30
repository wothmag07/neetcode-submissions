class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return
        
            letters = digit_to_letters[int(digits[index]) - 2]
            for letter in letters:
                backtrack(index + 1, path + letter)

        result = []
        backtrack(0, "")
        return result

        